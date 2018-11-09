from climaf.api import *
import xarray as xr
import numpy as np
from varexpe import Expe, Variable


def fld_year_avg(x):
    '''
    Apply successively fldavg and yearavg cdo operations
    '''
    y = ccdo(x, operator='fldavg')
    z = ccdo(y, operator='yearavg')
    return z


def zon_year_avg(x):
    '''
    Apply successively fldavg and yearavg cdo operations
    '''
    y = ccdo(x, operator='zonmean')
    z = ccdo(y, operator='yearavg')
    return z


def Id(x):
    '''
    Identity function
    '''
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


def define_CLIMAF_projects():
    '''
    Define a set of CLIMAF projects
    '''
    name = 'multiCMIP5'
    root_dirs = []
    root_dirs.append('/cnrm/cmip/CMIP5/Atmos/Origin/*/${model}/${experiment}/mon/atmos/r${member}i1p1')
    file_patterns = []
    file_patterns.append('${variable}_${table}_${model}_${experiment}_r${member}i1p1_YYYYMM-YYYYMM.nc')
    define_CLIMAF_project(name, root_dirs, file_patterns)
    #--
    name = 'myOBS'
    root_dirs = []    
    root_dirs.append('/cnrm/amacs/USERS/stmartin/data2/climobs')
    file_patterns = []
    file_patterns.append('${experiment}/${variable}_${experiment}_YYYY-YYYY.monthly.nc')
    define_CLIMAF_project(name, root_dirs, file_patterns)
    #--
    name = 'myCMIP6'
    root_dirs = []
    root_dirs.append('/cnrm/amacs/USERS/stmartin/NO_SAVE/CMIP6/sorties/*/${model}_${experiment}_r${member}i1p1*')
    file_patterns = []
    file_patterns.append('${variable}_${table}_${model}_${experiment}_r${member}i1p1*_YYYYMM-YYYYMM.nc')
    define_CLIMAF_project(name, root_dirs, file_patterns)
    #--
    name = 'STAB'
    root_dirs = []
    root_dirs.append('/cnrm/amacs/USERS/stmartin/data3/sorties/STAB/${model}_${experiment}_r${member}i1p1*')
    file_patterns = []
    file_patterns.append('${variable}_${table}_${model}_${experiment}_r${member}i1p1*_YYYYMM-YYYYMM.nc')
    define_CLIMAF_project(name, root_dirs, file_patterns)
    #--
    name = 'CPL6214'
    root_dirs = []
    root_dirs.append('/cnrm/amacs/USERS/stmartin/data3/sorties/PRE6')
    file_patterns = []
    file_patterns.append('${model}_${experiment}/X/monthly/${model}_${experiment}_arpsfx_monthly_${variable}_YYYY-YYYY.nc')
    file_patterns.append('${model}_${experiment}/X/${model}_${experiment}_arpsfx_monthly_${variable}_YYYY-YYYY.nc')
    define_CLIMAF_project(name, root_dirs, file_patterns)
    #--
    name = 'tmpCMIP6' # temporary ?
    root_dirs = []
    root_dirs.append('/home/stmartin/work/lxamacs/data')
    root_dirs.append('/cnrm/amacs/USERS/stmartin/data3/sorties/STAB/CLIMAF')
    root_dirs.append('/cnrm/amacs/USERS/stmartin/CLIMAF/EXPORT')    
    file_patterns = []
    file_patterns.append('${model}_${experiment}_r${member}_${variable}_${table}.gmean.annual.nc')
    define_CLIMAF_project(name, root_dirs, file_patterns)
    #--
    name = 'zonCMIP6' # temporary ?
    root_dirs = []
    root_dirs.append('/home/stmartin/work/lxamacs/data')
    root_dirs.append('/cnrm/amacs/USERS/stmartin/data3/sorties/STAB/CLIMAF')
    root_dirs.append('/cnrm/amacs/USERS/stmartin/CLIMAF/EXPORT')
    file_patterns = []
    file_patterns.append('${model}_${experiment}_r${member}_${variable}_${table}.zmean.annual.nc')
    define_CLIMAF_project(name, root_dirs, file_patterns)
    name = 'tmpIdCMIP6' # temporary ?
    root_dirs = []
    root_dirs.append('/home/stmartin/work/lxamacs/data')
    root_dirs.append('/cnrm/amacs/USERS/stmartin/data3/sorties/STAB/CLIMAF')
    root_dirs.append('/cnrm/amacs/USERS/stmartin/CLIMAF/EXPORT')    
    file_patterns = []
    file_patterns.append('${model}_${experiment}_r${member}_${variable}_${table}.nc')
    define_CLIMAF_project(name, root_dirs, file_patterns)


def add_expe_dict(my_dict, my_expe):
    '''
    Simply add a expe in a dictionary
    '''
    my_dict[my_expe.expid()] = my_expe


def dict_reanalyses(project_name):
    '''
    Define a specific dict of reanalyses
    '''
    dict_allexpes = {}
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='ERA-I', name='erai', ybeg=2008, yend=2012, is_Obs=True))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MERRA', name='merra', ybeg=2008, yend=2013, is_Obs=True))
    return dict_allexpes


def dict_expes_CMIP5_piControl(project_name):
    '''
    Define a specific dict of Expe-s for CMIP-5 piControl-related studies
    '''
    dict_allexpes = {}
    expe_name = 'piControl'
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='bcc-csm1-1', name=expe_name, ybeg=1, yend=500))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='BNU-ESM', name=expe_name, ybeg=1450, yend=2008))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CanESM2', name=expe_name, ybeg=2015, yend=3010))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CCSM4', name=expe_name, ybeg=250, yend=1300))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CNRM-CM5', name=expe_name, ybeg=1850, yend=2699))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CSIRO-Mk3-6-0', name=expe_name, ybeg=1, yend=500))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='FGOALS-s2', name=expe_name, ybeg=1850, yend=2350))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='GFDL-ESM2M', name=expe_name, ybeg=1, yend=500))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='HadGEM2-ES', name=expe_name, ybeg=1860, yend=2434))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='inmcm4', name=expe_name, ybeg=1860, yend=2349))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='IPSL-CM5A-LR', name=expe_name, ybeg=1800, yend=2799))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MIROC5', name=expe_name, ybeg=2000, yend=2699))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MPI-ESM-LR', name=expe_name, ybeg=1850, yend=2849))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MRI-CGCM3', name=expe_name, ybeg=1851, yend=2350))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='NorESM1-M', name=expe_name, ybeg=700, yend=1200))
    return dict_allexpes


def dict_expes_CMIP5_historical(project_name):
    '''
    Define a specific dict of Expe-s for CMIP-5 historical-related studies
    '''
    dict_allexpes = {}
    expe_name = 'historical'
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='bcc-csm1-1', name=expe_name, member=[1,2,3], ybeg=1850, yend=2005))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='BNU-ESM', name=expe_name, member=[1], ybeg=1850, yend=2005))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CanESM2', name=expe_name, member=[1,2,3,4,5], ybeg=1850, yend=2005))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CCSM4', name=expe_name, member=[1,2,3,4,5,6], ybeg=1850, yend=2005))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CSIRO-Mk3-6-0', name=expe_name, member=[1,2,3,4,5,6,7,8,9,10], ybeg=1850, yend=2005))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='FGOALS-s2', name=expe_name, member=[1,2,3], ybeg=1850, yend=2005))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='GFDL-ESM2M', name=expe_name, member=[1], ybeg=1850, yend=2005))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='HadGEM2-ES', name=expe_name, member=[1,2,3,4], ybeg=1850, yend=2005))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='inmcm4', name=expe_name, member=[1], ybeg=1850, yend=2005))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='IPSL-CM5A-LR', name=expe_name, member=[1,2,3,4,5,6], ybeg=1850, yend=2005))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MIROC5', name=expe_name, member=[1,2,3,4], ybeg=1850, yend=2005))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MPI-ESM-LR', name=expe_name, member=[1], ybeg=1850, yend=2005))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MRI-CGCM3', name=expe_name, member=[1,2,3], ybeg=1850, yend=2005))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='NorESM1-M', name=expe_name, member=[1,2,3], ybeg=1850, yend=2005))
    return dict_allexpes


def dict_expes_CMIP5_abrupt4xCO2(project_name):
    '''
    Define the specific dict of Expe-s for CMIP-5 abrupt4xCO2-related studies
    '''
    dict_allexpes = {}
    expe_name_CTL = 'piControl'
    expe_name = 'abrupt4xCO2'
    eCTL = Expe(project=project_name, model='bcc-csm1-1', name=expe_name_CTL, ybeg=1, yend=500)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='bcc-csm1-1', name=expe_name, expe_control=eCTL, ybeg=160, yend=309))
    eCTL = Expe(project=project_name, model='BNU-ESM', name=expe_name_CTL, ybeg=1450, yend=2008)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='BNU-ESM', name=expe_name, expe_control=eCTL, ybeg=1850, yend=1999))
    eCTL = Expe(project=project_name, model='CanESM2', name=expe_name_CTL, ybeg=2015, yend=3010)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CanESM2', name=expe_name, expe_control=eCTL, ybeg=1850, yend=1999))
    eCTL = Expe(project=project_name, model='CCSM4', name=expe_name_CTL, ybeg=250, yend=1300)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CCSM4', name=expe_name, expe_control=eCTL, ybeg=1850, yend=1999))
    eCTL = Expe(project=project_name, model='CNRM-CM5', name=expe_name_CTL, ybeg=1850, yend=2699)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CNRM-CM5', name=expe_name, expe_control=eCTL, ybeg=1850, yend=1999))
    eCTL = Expe(project=project_name, model='CSIRO-Mk3-6-0', name=expe_name_CTL, ybeg=1, yend=500)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CSIRO-Mk3-6-0', name=expe_name, expe_control=eCTL, ybeg=1, yend=150))
    eCTL = Expe(project=project_name, model='FGOALS-s2', name=expe_name_CTL, ybeg=1850, yend=2350)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='FGOALS-s2', name=expe_name, expe_control=eCTL, ybeg=1850, yend=1999))
    eCTL = Expe(project=project_name, model='GFDL-ESM2M', name=expe_name_CTL, ybeg=1, yend=500)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='GFDL-ESM2M', name=expe_name, expe_control=eCTL, ybeg=1, yend=150))
    eCTL = Expe(project=project_name, model='HadGEM2-ES', name=expe_name_CTL, ybeg=1860, yend=2434)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='HadGEM2-ES', name=expe_name, expe_control=eCTL, ybeg=1860, yend=2009))
    eCTL = Expe(project=project_name, model='inmcm4', name=expe_name_CTL, ybeg=1860, yend=2349)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='inmcm4', name=expe_name, expe_control=eCTL, ybeg=2090, yend=2239))
    eCTL = Expe(project=project_name, model='IPSL-CM5A-LR', name=expe_name_CTL, ybeg=1800, yend=2799)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='IPSL-CM5A-LR', name=expe_name, expe_control=eCTL, ybeg=1850, yend=1999))
    eCTL = Expe(project=project_name, model='MIROC5', name=expe_name_CTL, ybeg=2000, yend=2699)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MIROC5', name=expe_name, expe_control=eCTL, ybeg=2100, yend=2250))
    eCTL = Expe(project=project_name, model='MPI-ESM-LR', name=expe_name_CTL, ybeg=1850, yend=2849)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MPI-ESM-LR', name=expe_name, expe_control=eCTL, ybeg=1850, yend=1999))
    eCTL = Expe(project=project_name, model='MRI-CGCM3', name=expe_name_CTL, ybeg=1851, yend=2350)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MRI-CGCM3', name=expe_name, expe_control=eCTL, ybeg=1851, yend=2000))
    eCTL = Expe(project=project_name, model='NorESM1-M', name=expe_name_CTL, ybeg=700, yend=1200)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='NorESM1-M', name=expe_name, expe_control=eCTL, ybeg=1, yend=150))
    return dict_allexpes


def dict_expes_stab_article(project_name):
    '''
    Define the specific dict of Expe-s for stabilization study
    '''
    model_name = 'CNRM-CM6-1'
    dict_allexpes = {}
    eCTL = Expe(project=project_name, model=model_name, name='piControl', ybeg=1850, yend=2349, marker=',', color='silver')
    add_expe_dict(dict_allexpes, eCTL)
    add_expe_dict(dict_allexpes, Expe(project=project_name, model=model_name, name='abrupt-4xCO2', ybeg=1850, yend=2849, expe_control=eCTL, marker=',', color='dimgray'))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model=model_name, name='abrupt-2xCO2', ybeg=1850, yend=2377, expe_control=eCTL, marker=',', color='black'))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model=model_name, name='stab-1p4xCO2-dab', ybeg=1969, yend=2272, expe_control=eCTL, marker='.', color='purple'))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model=model_name, name='stab-2xCO2-dab', ybeg=2137, yend=2451, expe_control=eCTL, marker='.', color='orangered'))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model=model_name, name='stab-2p8xCO2-dab', ybeg=2424, yend=2711, expe_control=eCTL, marker='.', color='orange'))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model=model_name, name='expo-2xCO2', ybeg=1850, yend=2172, expe_control=eCTL, marker='.', color='dodgerblue'))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model=model_name, name='expo-4xCO2', ybeg=1850, yend=2049, expe_control=eCTL, marker='.', color='dodgerblue'))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model=model_name, name='stab-2xCO2-tab8x', ybeg=2000, yend=2208, expe_control=eCTL, marker='.', color='green'))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model=model_name, name='stab-4xCO2-tab8x', ybeg=2074, yend=2174, expe_control=eCTL, marker='.', color='magenta'))
    return dict_allexpes


def dict_expes_historical_CNRMCM(project_name, model_name, n_member=10, ybeg=1850, yend=2014, with_piControl=True):
    '''
    Define a specific dict of Expe-s for CNRM-CM6-1 (or CNRM-CM5) historical simulations
    '''
    dict_allexpes = {}
    if with_piControl:
        # -- add piControl experiment to the dict of Expe-s
        eCTL = Expe(project=project_name, model=model_name, name='piControl', ybeg=1850, yend=2349, marker=',', color='silver')
        add_expe_dict(dict_allexpes, eCTL)
    else:
        eCTL = None
    add_expe_dict(dict_allexpes, Expe(project=project_name, model=model_name, name='historical', member=range(1, n_member+1), ybeg=ybeg, yend=yend, expe_control=eCTL, marker=',', color='dimgray'))
    return dict_allexpes


def dict_var(varname, vartable):
    '''
    Define a dict of one single variable with varname and vartable
    '''
    dict_vars = {}
    v = Variable(name=varname, table=vartable)
    dict_vars[v.name] = v
    return dict_vars


def dict_vars_T():
    '''
    Define the specific dict of Variable-s for N-T plot study
    '''
    dict_vars = {}
    v = Variable(name='tas', table='Amon')
    dict_vars[v.name] = v
    return dict_vars


def dict_vars_NT():
    '''
    Define the specific dict of Variable-s for N-T plot study
    '''
    dict_vars = {}
    v = Variable(name='tas', table='Amon')
    dict_vars[v.name] = v
    v = Variable(name='rsdt', table='Amon')
    dict_vars[v.name] = v
    v = Variable(name='rsut', table='Amon')
    dict_vars[v.name] = v
    v = Variable(name='rlut', table='Amon')
    dict_vars[v.name] = v
    return dict_vars


def dict_vars_heatc():
    '''
    Define the specific dict of Variable-s for heat contents
    '''
    dict_vars = {}
    v = Variable(name='hc2000', table='HOMOImon')
    dict_vars[v.name] = v
    v = Variable(name='hc700', table='HOMOImon')
    dict_vars[v.name] = v
    v = Variable(name='heatc', table='HOMOImon')
    dict_vars[v.name] = v
    v = Variable(name='hcont300', table='Emon')
    dict_vars[v.name] = v
    return dict_vars


def convert_climaf_dataset(datasets, var, exp, exp_number, climaf_ds, operation, dir_target, writeFiles, verbose, computeMean, computeAnom):
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
            if operation == fld_year_avg:
                cfile(operation(climaf_ds), target=dir_target+'/'+exp_id+'_'+var.varid()+'.gmean.annual.nc')
            elif operation == zon_year_avg:
                cfile(operation(climaf_ds), target=dir_target+'/'+exp_id+'_'+var.varid()+'.zmean.annual.nc')
            elif operation == Id:
                cfile(operation(climaf_ds), target=dir_target+'/'+exp_id+'_'+var.varid()+'.nc')
            else:
                print operation, ' not known...'
                return
        else:
            xds = xr.open_dataset(cfile(operation(climaf_ds)))
            if verbose:
                print 'Loading data for : ', (exp_id, var.varid(), 'brut')
            datasets[(exp_id, var.varid(), 'brut')] = xds[var.name]
            if computeMean:
                # -- add 'temporal' mean value
                datasets[(exp_id, var.varid(), 'mean')] = np.mean(datasets[(exp_id, var.varid(), 'brut')], axis=0)
            if computeAnom:
                # -- add anomaly-from-the-control-temporal-mean value
                if exp.expe_control is not None:
                    datasets[(exp_id, var.varid(), 'anom')] = datasets[(exp_id,  var.varid(), 'brut')] - datasets[(exp.expe_control.expid(number='_r1'), var.varid(), 'mean')]
                # -- control is the expe itself if expe_control not specified
                else:
                    datasets[(exp_id, var.varid(), 'anom')] = datasets[(exp_id,  var.varid(), 'brut')] - datasets[(exp_id, var.varid(), 'mean')]
    else:
        print 'Data not found for : ', (var.varid(), exp_id)


def load_datas(dictexpes, dictvars, operation, dir_target=None, writeFiles=False, verbose=False, computeMean=True, computeAnom=True, add_rnet=True):
    '''
    Get data from : 
    - a specific dict of Expe-s : dictexpes
    - a specific dict of Var-s : dictvars

    Apply function operation = {fld_year_avg, zon_year_avg, Id} to data

    Rq : the option dir_target/writeFiles is temporary (it is only used to quickly copy the CliMAF cache : use for lx and px PCs)

    > Return a dictionary with a 3-element tuple (exp.expid(), varname, vartype='brut/mean/anom') keys
    '''
    my_datasets = {}
    for var in dictvars.values():
        for exp in dictexpes.values():
            fens = None
            if len(exp.member) > 1:
                # -- if exp has more than 1 member, construct a CliMAF object of class cens (a dict of objects)
                fens = cens()
            for m in exp.member:
                # -- if not, load datas for exp.expe_control
                if exp.expe_control is not None and not my_datasets.has_key((exp.expe_control.expid(number='_r1'), var.varid(), 'brut')):
                    ex = exp.expe_control
                    f = ds(project=ex.project, variable=var.name, table=var.table, gridtype=var.grid, model=ex.model, experiment=ex.name, realization='r1i1p1f2', member=m, period=ex.period())
                    convert_climaf_dataset(my_datasets, var, ex, '_r1', f, operation, dir_target, writeFiles, verbose, computeMean, computeAnom)
                # -- load datas for each individual member of exp
                f = ds(project=exp.project, variable=var.name, table=var.table, gridtype=var.grid, model=exp.model, experiment=exp.name, realization='r'+str(m)+'i1p1f2', member=m, period=exp.period())
                convert_climaf_dataset(my_datasets, var, exp, '_r'+str(m), f, operation, dir_target, writeFiles, verbose, computeMean, computeAnom)
                if fens is not None:
                    fens['r'+str(m)+'i1p1f2'] = f
            if fens is not None:
                # -- load datas for ensemble mean of exp
                eavg = ccdo_ens(fens, operator='ensavg')
                convert_climaf_dataset(my_datasets, var, exp, '_rEM', eavg, operation, dir_target, writeFiles, verbose, computeMean, computeAnom)
    if writeFiles:
        return
    if add_rnet:
        # -- add new var 'rnet' from rsdt, rsut and rlut values
        for (exp_id, var_id, var_type)  in my_datasets.keys():
            if var_id == 'rsdt_Amon':
                my_datasets[(exp_id, 'rnet', var_type)] = my_datasets[(exp_id, 'rsdt_Amon', var_type)] - my_datasets[(exp_id, 'rsut_Amon', var_type)] - my_datasets[(exp_id, 'rlut_Amon', var_type)]
    return my_datasets


def load_HadCRU_data(datasets, version=4):
    '''
    '''
    name = 'HadCRUT'+str(version)
    xds = xr.open_dataset(name+'.gmean.annual.nc')
    if version == 4:
        varname='temperature_anomaly'
    elif version == 3:
        varname='temp'
    else:
        varname=None
    datasets[(name, 'tas_Amon', 'brut')] = xds[varname]
