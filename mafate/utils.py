from climaf.api import *
import xarray as xr
import numpy as np
from varexpe import Expe, Variable


def define_CLIMAF_project(name, rootdirs, file_pattern):
    '''
    Define a new CLIMAF project by setting :
      - attributes
      - data localization
    '''
    cproject(name, 'model', 'experiment', 'member', 'variable', 'table')
    dataloc(project = name, organization = 'generic', url = [rdir+'/'+file_pattern for rdir in rootdirs])


def define_CLIMAF_projects():
    '''
    Define a set of CLIMAF projects
    '''
    name = 'myCMIP6'
    rootdirs = []
    rootdirs.append('/cnrm/amacs/USERS/stmartin/NO_SAVE/CMIP6/sorties/*/${model}_${experiment}_r${member}i1p1*')
    file_pattern = '${variable}_${table}_${model}_${experiment}_r${member}i1p1*_YYYYMM-YYYYMM.nc'
    define_CLIMAF_project(name, rootdirs, file_pattern)
    name = 'CPL6214'
    rootdir = '/cnrm/amacs/USERS/stmartin/data3/sorties/PRE6'
    locadirs = ['${model}_${experiment}/X/monthly/${model}_${experiment}_arpsfx_monthly_${variable}_YYYY-YYYY.nc', '${model}_${experiment}/X/${model}_${experiment}_arpsfx_monthly_${variable}_YYYY-YYYY.nc']
    define_CLIMAF_project(name, rootdirs, file_pattern)
    # temporary ?
    name = 'tmpCMIP6'
    rootdirs = []
    rootdirs.append('/home/stmartin/work/lxamacs/data')
    rootdirs.append('/cnrm/amacs/USERS/stmartin/data3/sorties/STAB/CLIMAF')
    file_pattern = '${model}_${experiment}_r${member}_${variable}_${table}.gmean.annual.nc'
    define_CLIMAF_project(name, rootdirs, file_pattern)
    name = 'zonCMIP6'
    rootdirs = []
    rootdirs.append('/home/stmartin/work/lxamacs/data')
    rootdirs.append('/cnrm/amacs/USERS/stmartin/data3/sorties/STAB/CLIMAF')
    file_pattern = '${model}_${experiment}_r${member}_${variable}_${table}.zmean.annual.nc'
    define_CLIMAF_project(name, rootdirs, file_pattern)
    name = 'multiCMIP5'
    rootdirs = []
    rootdirs.append('/cnrm/cmip/CMIP5/Atmos/Origin/*/${model}/${experiment}/mon/atmos/r${member}i1p1')
    file_pattern = '${variable}_${table}_${model}_${experiment}_r${member}i1p1_YYYYMM-YYYYMM.nc'
    define_CLIMAF_project(name, rootdirs, file_pattern)
    name = 'STAB'
    rootdirs = []    
    rootdirs.append('/cnrm/amacs/USERS/stmartin/data3/sorties/STAB/${model}_${experiment}_r${member}i1p1*')
    file_pattern = '${variable}_${table}_${model}_${experiment}_r${member}i1p1*_YYYYMM-YYYYMM.nc'
    define_CLIMAF_project(name, rootdirs, file_pattern)


def add_expe_dict(my_dict, my_expe):
    '''
    Simply add a expe in a dictionary
    '''
    my_dict[my_expe.expid()] = my_expe


def dict_expes_CMIP5_piControl(project_name):
    '''
    Define the specific dict of Expe-s for CMIP-5 piControl-related studies
    '''
    dict_allexpes = {}
    expe_name = 'piControl'
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='bcc-csm1-1', name=expe_name, member=1, ybeg=1, yend=500))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='BNU-ESM', name=expe_name, member=1, ybeg=1450, yend=2008))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CanESM2', name=expe_name, member=1, ybeg=2015, yend=3010))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CCSM4', name=expe_name, member=1, ybeg=250, yend=1300))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CNRM-CM5', name=expe_name, member=1, ybeg=1850, yend=2699))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CSIRO-Mk3-6-0', name=expe_name, member=1, ybeg=1, yend=500))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='FGOALS-s2', name=expe_name, member=1, ybeg=1850, yend=2350))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='GFDL-ESM2M', name=expe_name, member=1, ybeg=1, yend=500))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='HadGEM2-ES', name=expe_name, member=1, ybeg=1860, yend=2434))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='inmcm4', name=expe_name, member=1, ybeg=1860, yend=2349))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='IPSL-CM5A-LR', name=expe_name, member=1, ybeg=1800, yend=2799))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MIROC5', name=expe_name, member=1, ybeg=2000, yend=2699))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MPI-ESM-LR', name=expe_name, member=1, ybeg=1850, yend=2849))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MRI-CGCM3', name=expe_name, member=1, ybeg=1851, yend=2350))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='NorESM1-M', name=expe_name, member=1, ybeg=700, yend=1200))
    return dict_allexpes


def dict_expes_CMIP5_abrupt4xCO2(project_name):
    '''
    Define the specific dict of Expe-s for CMIP-5 abrupt4xCO2-related studies
    '''
    dict_allexpes = {}
    expe_name = 'abrupt4xCO2'
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='bcc-csm1-1', name=expe_name, member=1, ybeg=160, yend=309))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='BNU-ESM', name=expe_name, member=1, ybeg=1850, yend=1999))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CanESM2', name=expe_name, member=1, ybeg=1850, yend=1999))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CCSM4', name=expe_name, member=1, ybeg=1850, yend=1999))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CNRM-CM5', name=expe_name, member=1, ybeg=1850, yend=1999))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='CSIRO-Mk3-6-0', name=expe_name, member=1, ybeg=1, yend=150))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='FGOALS-s2', name=expe_name, member=1, ybeg=1850, yend=1999))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='GFDL-ESM2M', name=expe_name, member=1, ybeg=1, yend=150))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='HadGEM2-ES', name=expe_name, member=1, ybeg=1860, yend=2009))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='inmcm4', name=expe_name, member=1, ybeg=2090, yend=2239))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='IPSL-CM5A-LR', name=expe_name, member=1, ybeg=1850, yend=1999))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MIROC5', name=expe_name, member=1, ybeg=2100, yend=2250))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MPI-ESM-LR', name=expe_name, member=1, ybeg=1850, yend=1999))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='MRI-CGCM3', name=expe_name, member=1, ybeg=1851, yend=2000))
    add_expe_dict(dict_allexpes, Expe(project=project_name, model='NorESM1-M', name=expe_name, member=1, ybeg=1, yend=150))
    return dict_allexpes


def dict_expes_stab_article(project_name):
    '''
    Define the specific dict of Expe-s for stabilization study
    '''
    dict_allexpes = {}
    eCTL = Expe(project=project_name, model='CNRM-CM6-1', name='piControl', member=1, ybeg=1850, yend=2349, marker=',', color='silver')
    eCTL.expe_control = eCTL  
    dict_allexpes[eCTL.expid()] = eCTL
    e = Expe(project=project_name, model='CNRM-CM6-1', name='abrupt-4xCO2', member=1, ybeg=1850, yend=2762, expe_control=eCTL, marker=',', color='dimgray')
    dict_allexpes[e.expid()] = e
    e = Expe(project=project_name, model='CNRM-CM6-1', name='abrupt-2xCO2', member=1, ybeg=1850, yend=2189, expe_control=eCTL, marker=',', color='black')
    dict_allexpes[e.expid()] = e
    # e = Expe(project=project_name, model='CNRM-CM6-1', name='stab-1p4xCO2-dab', member=1, ybeg=1969, yend=2263, expe_control=eCTL, marker='.', color='purple')
    e = Expe(project=project_name, model='CNRM-CM6-1', name='stab-1p4xCO2-dab', member=1, ybeg=1969, yend=2203, expe_control=eCTL, marker='.', color='purple')
    dict_allexpes[e.expid()] = e
    # e = Expe(project=project_name, model='CNRM-CM6-1', name='stab-2xCO2-dab', member=1, ybeg=2137, yend=2356, expe_control=eCTL, marker='.', color='orangered')
    e = Expe(project=project_name, model='CNRM-CM6-1', name='stab-2xCO2-dab', member=1, ybeg=2137, yend=2277, expe_control=eCTL, marker='.', color='orangered')
    dict_allexpes[e.expid()] = e
    # e = Expe(project=project_name, model='CNRM-CM6-1', name='stab-2p8xCO2-dab', member=1, ybeg=2424, yend=2636, expe_control=eCTL, marker='.', color='orange')
    e = Expe(project=project_name, model='CNRM-CM6-1', name='stab-2p8xCO2-dab', member=1, ybeg=2424, yend=2576, expe_control=eCTL, marker='.', color='orange')
    dict_allexpes[e.expid()] = e
    # e = Expe(project=project_name, model='CNRM-CM6-1', name='expo-2xCO2', member=1, ybeg=1850, yend=2096, expe_control=eCTL, marker='.', color='dodgerblue')
    e = Expe(project=project_name, model='CNRM-CM6-1', name='expo-2xCO2', member=1, ybeg=1850, yend=2017, expe_control=eCTL, marker='.', color='dodgerblue')
    dict_allexpes[e.expid()] = e
    # e = Expe(project=project_name, model='CNRM-CM6-1', name='stab-2xCO2-tab8x', member=1, ybeg=2000, yend=2093, expe_control=eCTL, marker='.', color='green')
    e = Expe(project=project_name, model='CNRM-CM6-1', name='stab-2xCO2-tab8x', member=1, ybeg=2000, yend=2033, expe_control=eCTL, marker='.', color='green')
    dict_allexpes[e.expid()] = e
    return dict_allexpes


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


def avg_var(modvar) :
    modvar_spcavg = space_average(modvar)
    serie = ccdo(modvar_spcavg,operator='yearavg')
    return serie


def avg_zon(x) :
    u = ccdo(x, operator='zonmean')
    y = ccdo(u, operator='yearavg')
    return y


def Id(x) :
    return x


def load_datas(dictexpes, dictvars, operation, dir_target=None, writeFiles=False, verbose=False):
    '''
    Get data from : 
    - a specific dict of Expe-s : dictexpes
    - a specific dict of Var-s : dictvars

    Apply function operation = {avg_var, avg_zon} to data

    Rq : the option dir_target/writeFiles is temporary (it is only used to quickly copy the CliMAF cache : use for lx and px PCs)

    > Return a dictionary with a 3-element tuple (exp.expid(), varname, vartype='brut/mean/anom') keys
    '''
    datasets = {}
    # -- read datas
    for exp in dictexpes.values():
        if verbose:
            print exp.name, exp.member
        for var in dictvars.values():
            f = ds(project=exp.project, variable=var.name, table=var.table, gridtype=var.grid, model=exp.model, experiment=exp.name, member=exp.member, period=exp.period())
            if f.listfiles() is not None:
                if writeFiles:
                    if operation == avg_var:
                        cfile(operation(f), target=dir_target+'/'+exp.expid()+'_'+var.varid()+'.gmean.annual.nc')
                    elif operation == avg_zon:
                        cfile(operation(f), target=dir_target+'/'+exp.expid()+'_'+var.varid()+'.zmean.annual.nc')
                    else:
                        print operation, 'not known'
                        return
                else:
                    xds = xr.open_dataset(cfile(operation(f)))
                    datasets[(exp.expid(), var.varid(), 'brut')] = xds[var.name]
                if verbose:
                    print(f.listfiles())
            else:
                print var.name, ' not in ', exp.name
    if writeFiles:
        return
    # -- add 'temporal' mean value
    for exp in dictexpes.values():
        for var in dictvars.values():
            if (datasets.has_key((exp.expid(), var.varid(), 'brut'))):
                datasets[(exp.expid(), var.varid(), 'mean')] = np.mean(datasets[(exp.expid(), var.varid(), 'brut')], axis=0)
    # -- add anomaly-from-the-control-temporal-mean value
    # -- add new var 'rnet' from rsdt, rsut and rlut values
    for exp in dictexpes.values():
        for var in dictvars.values():
            if (datasets.has_key((exp.expid(), var.varid(), 'brut'))):
                datasets[(exp.expid(), var.varid(), 'anom')] = datasets[(exp.expid(), var.varid(), 'brut')] - datasets[(exp.expe_control.expid(), var.varid(), 'mean')]
        for x in ['brut', 'mean', 'anom']:
            if (datasets.has_key((exp.expid(), 'rsdt_Amon', 'brut'))):
                datasets[(exp.expid(), 'rnet', x)] = datasets[(exp.expid(), 'rsdt_Amon', x)] - datasets[(exp.expid(), 'rsut_Amon', x)] - datasets[(exp.expid(), 'rlut_Amon', x)]
    return datasets
