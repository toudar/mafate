from climaf.api import *
import xarray as xr
import numpy as np
from varexpe import Expe, Variable


def cdogen(x, list_cdops):
    '''
    Apply successively a list of cdo operations, list_cdops
    '''
    if list_cdops == None:
        return x
    else:
        for op in list_cdops:
            x = ccdo(x, operator=op)
        return x


def define_CLIMAF_project(name, root_dirs, file_patterns):
    '''
    Define a new CLIMAF project by setting :
      - a name : name
      - attributes
      - a data localization : full combination of root_dirs and file_patterns lists
    '''
    cproject(name, 'model', 'experiment', 'member', 'realization', 'variable', 'table')
    dataloc(project = name, organization = 'generic', url = [d+'/'+f for d in root_dirs for f in file_patterns])


def dict_exp(my_expe):
    '''
    Define a dict of one single Expe my_expe
    '''
    dict_expe = {}
    dict_expe[my_expe.expid(my_expe.number)] = my_expe
    return dict_expe


def dict_var(name, table='*', grid='gr'):
    '''
    Define a dict of one single variable with name, table and grid
    '''
    dict_vars = {}
    v = Variable(name=name, table=table, grid=grid)
    dict_vars[v.name] = v
    return dict_vars


def open_and_expand_dataset(my_file, dict_add_dims):
    '''
    Auxiliary function to extend the use of xarray function open_dataset
    Add new dimensions defined by dict_add_dims
    '''
    xds = xr.open_dataset(my_file)
    for d in dict_add_dims.keys():
        print d, dict_add_dims[d]
        xds = xds.expand_dims(d)
        xds[d] = dict_add_dims[d]
    return xds


def convert_climaf_dataset(datasets, var, exp, exp_number, climaf_ds, operation, list_cdops, dir_target, writeFiles, verbose, computeMean, computeAnom):
    '''
    Auxiliary function to convert a CliMAF dataset/object to :
        - either a target file
        - either a xarray dataset
    '''
    exp_id = exp.expid(exp_number)
    if climaf_ds is not None:
        if verbose:
            if hasattr(climaf_ds, 'listfiles'):
                print 'Loading data from files : ', climaf_ds.listfiles()
            else:
                print 'Loading data from CliMAF dataset : '; climaf_ds
        if writeFiles:
            if operation == cdogen:
                suffix = '.nc'
                for cdop in list_cdops:
                    suffix = '.' + cdop + suffix
                cfile(operation(climaf_ds, list_cdops), target=dir_target+'/'+exp_id+'_'+var.varid()+suffix)
            else:
                print operation, ' not known...'
                return
        else:
            xds = open_and_expand_dataset(cfile(operation(climaf_ds, list_cdops)), {'model':[exp.model], 'member':np.array([exp.number])})
            if verbose:
                print 'Loading data for : ', (exp_id, var.varid(), 'brut')
            if datasets.has_key(exp.name):
                datasets[exp.name] = xr.merge([datasets[exp.name], xds[var.name]])
            else:
                datasets[exp.name] = xds[var.name]
            #@ if computeMean:
            #@    # -- add 'temporal' mean value
            #@    datasets[(exp_id, var.varid(), 'mean')] = np.mean(datasets[(exp_id, var.varid(), 'brut')], axis=0)
            #@ if computeAnom:
            #@    # -- add anomaly-from-the-control-temporal-mean value
            #@    if exp.expe_control is not None:
            #@        datasets[(exp_id, var.varid(), 'anom')] = datasets[(exp_id,  var.varid(), 'brut')] - datasets[(exp.expe_control.expid(number='_r1'), var.varid(), 'mean')]
            #@    # -- control is the expe itself if expe_control not specified
            #@    else:
            #@        datasets[(exp_id, var.varid(), 'anom')] = datasets[(exp_id,  var.varid(), 'brut')] - datasets[(exp_id, var.varid(), 'mean')]
    else:
        print 'Data not found for : ', (var.varid(), exp_id)


def load_datas(dictexpes, dictvars, operation, list_cdops=None, dir_target='.', writeFiles=False, verbose=False, computeMean=False, computeAnom=False, add_rnet=True):
    '''
    Get data from : 
    - a specific dict of Expe-s : dictexpes
    - a specific dict of Var-s : dictvars

    Apply a list of cdo operation (list_cdops) to data

    Rq : the option dir_target/writeFiles is temporary (it is only used to quickly copy the CliMAF cache : use for lx and px PCs)

    > Return a dictionary of xarray's Dataset indexed by the experiment name:
        All the models/members/variables are grouped in a single Dataset for each experiment
    '''
    my_datasets = {}
    for var in dictvars.values():
        for exp in dictexpes.values():
            m = exp.number
            if exp.expe_control is not None:
                ex = exp.expe_control
                f = ds(project=ex.project, variable=var.name, table=var.table, gridtype=var.grid, model=ex.model, experiment=ex.name, realization='r1i1p1f2', member=m, period=ex.period(), **exp.adds)
                convert_climaf_dataset(my_datasets, var, ex, '_r1', f, operation, list_cdops, dir_target, writeFiles, verbose, computeMean, computeAnom)
            f = ds(project=exp.project, variable=var.name, table=var.table, gridtype=var.grid, model=exp.model, experiment=exp.name, realization='r'+str(m)+'i1p1f2', member=m, period=exp.period(), **exp.adds)
            convert_climaf_dataset(my_datasets, var, exp, '_r'+str(m), f, operation, list_cdops, dir_target, writeFiles, verbose, computeMean, computeAnom)
    if writeFiles:
        return
    if add_rnet:
        # -- add new var 'rnet' from rsdt, rsut and rlut values        
        if 'rsdt' in my_datasets.variables:
            my_datasets['rnet'] = my_datasets['rsdt'] - my_datasets['rsut'] - my_datasets['rlut']
        #@for (exp_id, var_id, var_type)  in my_datasets.keys():
        #@    if var_id == 'rsdt':
        #@        my_datasets[(exp_id, 'rnet', var_type)] = my_datasets[(exp_id, 'rsdt', var_type)] - my_datasets[(exp_id, 'rsut', var_type)] - my_datasets[(exp_id, 'rlut', var_type)]
    return my_datasets
