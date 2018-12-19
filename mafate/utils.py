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
    dict_expe[my_expe.expid()] = my_expe
    return dict_expe


def dict_var(name, table='*', grid='gr'):
    '''
    Define a dict of one single variable with name, table and grid
    '''
    dict_vars = {}
    v = Variable(name=name, table=table, grid=grid)
    dict_vars[v.name] = v
    return dict_vars


def extract_from_exp(datasets, expe):
    '''
    Get dataset from a single expe
    '''
    if expe is None:
        return None
    else:
        return datasets[expe.name].sel(model=expe.model, member=expe.number)


def compute_anom_from_control(datasets, dictexpes, dictvars):
    '''
    '''
    for var in list(dictvars.values()):
        for exp in list(dictexpes.values()):
            print(exp.name, var.name)
            compute_anom_from_control_varexpe(datasets, var, exp)


def compute_anom_from_control_varexpe(datasets, var, expe):
    '''
    '''
    ds_exp = extract_from_exp(datasets, expe)
    ds_ctl = extract_from_exp(datasets, expe.expe_control)
    datasets[expe.name][var.name+'_anom'] = xr.full_like(datasets[expe.name][var.name], fill_value=None)
    if ds_ctl is not None:
        ds_exp[var.name+'_anom'] = ds_exp[var.name] - ds_ctl[var.name].mean(dim='time')
        datasets[expe.name] = xr.merge([datasets[expe.name], ds_exp[var.name+'_anom']])


def harmonizingCoords(ds):
    '''
    Auxiliary function to standardize coordinate names
    '''
    _levs = ['levels', 'level']
    _lats = ['latitude']
    _lons = ['longitude']
    lev_ = 'plev'
    lat_ = 'lat'
    lon_ = 'lon'
    ds = renameCoords(ds, _levs, lev_)
    ds = renameCoords(ds, _lats, lat_)
    ds = renameCoords(ds, _lons, lon_)
    return ds


def renameCoords(ds, liste, name):
    for xname in liste:
        if xname in ds:
            ds = ds.rename({xname:name})
    return ds


def open_and_expand_dataset(my_file, dict_add_dims, module, harmonizeCoords, var=None):
    '''
    Auxiliary function to extend the use of xarray function open_dataset
    Add new dimensions defined by dict_add_dims
    '''
    if module == 'xarray':
        xds = xr.open_dataset(my_file)
        if harmonizeCoords:
            xds = harmonizingCoords(xds)
    if module == 'iris':
        import iris
        xds = iris.load(my_file)
        xds[0].attributes = {}
        xds[0].rename(var)
    for d in list(dict_add_dims.keys()):
        if module == 'xarray':
            xds = xds.expand_dims(d)
            xds[d] = dict_add_dims[d]
        if module == 'iris':
            import iris
            newdim = iris.coords.AuxCoord(dict_add_dims[d], long_name=d)
            xds[0].add_aux_coord(newdim)
    return xds


def convert_climaf_dataset(datasets, var, exp, climaf_ds, operation, list_cdops, dir_target, module, writeFiles, harmonizeCoords, verbose):
    '''
    Auxiliary function to convert a CliMAF dataset/object to :
        - either a target file
        - either a xarray dataset or a iris object
    '''
    exp_id = exp.expid()
    if climaf_ds is not None:
        if verbose:
            if hasattr(climaf_ds, 'listfiles'):
                print('Loading data from files : ', climaf_ds.listfiles())
            else:
                print('Loading data from CliMAF dataset : ', climaf_ds)
        if writeFiles:
            if operation == cdogen:
                suffix = '.nc'
                for cdop in list_cdops:
                    suffix = '.' + cdop + suffix
                cfile(operation(climaf_ds, list_cdops), target=dir_target+'/'+exp_id+'_'+var.varid()+suffix)
            else:
                print(operation, ' not known...')
                return
        else:
            xds = open_and_expand_dataset(cfile(operation(climaf_ds, list_cdops)), {'model':[exp.model], 'member':np.array([exp.number])}, module, harmonizeCoords, var.varid())
            if verbose:
                print('Loading data for expid::%s and for varid::%s'%(exp.expid(), var.varid()))
            if exp.name in datasets:
                if module == 'xarray':
                    datasets[exp.name] = xr.merge([datasets[exp.name], xds])
                if module == 'iris':
                    import iris
                    datasets[exp.name] = (datasets[exp.name] + xds).merge()
            else:
                datasets[exp.name] = xds
    else:
        print('Data not found for expid::%s and for varid::%s'%(exp.expid(), var.varid()))


def load_datas(dictexpes, dictvars, operation=cdogen, list_cdops=None, dir_target='.', module='xarray', writeFiles=False, computeAnom=False, add_rnet=True, harmonizeCoords=False, verbose=False):
    '''
    Get data from : 
    - a specific dict of Expe-s : dictexpes
    - a specific dict of Var-s : dictvars

    Apply a list of cdo operation (list_cdops) to data

    Rq : the option dir_target/writeFiles is temporary (it is only used to quickly copy the CliMAF cache : use for lx and px PCs)

    > Return a dictionary of xarray's Dataset or iris's object indexed by the experiment name:
        All the models/members/variables are grouped in a single Dataset for each experiment
    '''
    my_datasets = {}
    for var in list(dictvars.values()):
        for exp in list(dictexpes.values()):
            m = exp.number
            f = ds(project=exp.project, variable=var.name, table=var.table, gridtype=var.grid, model=exp.model, experiment=exp.name, realization='r'+str(m)+'i1p1*', member=m, period=exp.period(), **exp.adds)
            convert_climaf_dataset(my_datasets, var, exp, f, operation, list_cdops, dir_target, module, writeFiles, harmonizeCoords, verbose)
    if writeFiles:
        return
    if computeAnom:
        compute_anom_from_control(my_datasets, dictexpes, dictvars)
    if add_rnet:
        for e_ in list(my_datasets.keys()):
            ds_ = my_datasets[e_]
            # -- add new var 'rnet' from rsdt, rsut and rlut values
            if 'rsdt' in ds_.variables:
                ds_['rnet'] = ds_['rsdt'] - ds_['rsut'] - ds_['rlut']
                if computeAnom:
                    ds_['rnet_anom'] = ds_['rsdt_anom'] - ds_['rsut_anom'] - ds_['rlut_anom']
    return my_datasets
