import numpy as np
from .varexpe import Expe, Variable
from .utils import *

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
    file_patterns.append('${model}/${variable}_${model}_YYYY-YYYY.monthly.nc')
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
    name = 'fldmeanCMIP6' # temporary ?
    root_dirs = []
    root_dirs.append('/home/stmartin/work/lxamacs/data')
    root_dirs.append('/cnrm/amacs/USERS/stmartin/CLIMAF/EXPORT/STAB')
    file_patterns = []
    file_patterns.append('${model}_${experiment}_r${member}_${variable}.yearmean.fldmean.nc')
    define_CLIMAF_project(name, root_dirs, file_patterns)
    #--
    name = 'zonmeanCMIP6' # temporary ?
    root_dirs = []
    root_dirs.append('/home/stmartin/work/lxamacs/data')
    root_dirs.append('/cnrm/amacs/USERS/stmartin/CLIMAF/EXPORT/STAB')
    file_patterns = []
    file_patterns.append('${model}_${experiment}_r${member}_${variable}.yearmean.zonmean.nc')
    define_CLIMAF_project(name, root_dirs, file_patterns)
    name = 'idCMIP6' # temporary ?
    root_dirs = []
    root_dirs.append('/home/stmartin/work/lxamacs/data')
    root_dirs.append('/cnrm/amacs/USERS/stmartin/CLIMAF/EXPORT/STAB')
    file_patterns = []
    file_patterns.append('${model}_${experiment}_r${member}_${variable}.nc')
    define_CLIMAF_project(name, root_dirs, file_patterns)


def dict_reanalyses(project_name):
    '''
    Define a specific dict of reanalyses
    '''
    dict_allexpes = {}
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='ERA-I', name='erai', ybeg=2008, yend=2012, is_Obs=True)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='MERRA', name='merra', ybeg=2008, yend=2013, is_Obs=True)))
    return dict_allexpes


def dict_expes_CMIP5_piControl(project_name):
    '''
    Define a specific dict of Expe-s for CMIP-5 piControl-related studies
    '''
    dict_allexpes = {}
    expe_name = 'piControl'
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='bcc-csm1-1', name=expe_name, ybeg=1, yend=500)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='BNU-ESM', name=expe_name, ybeg=1450, yend=2008)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='CanESM2', name=expe_name, ybeg=2015, yend=3010)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='CCSM4', name=expe_name, ybeg=250, yend=1300)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='CNRM-CM5', name=expe_name, ybeg=1850, yend=2699)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='CSIRO-Mk3-6-0', name=expe_name, ybeg=1, yend=500)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='FGOALS-s2', name=expe_name, ybeg=1850, yend=2350)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='GFDL-ESM2M', name=expe_name, ybeg=1, yend=500)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='HadGEM2-ES', name=expe_name, ybeg=1860, yend=2434)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='inmcm4', name=expe_name, ybeg=1860, yend=2349)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='IPSL-CM5A-LR', name=expe_name, ybeg=1800, yend=2799)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='MIROC5', name=expe_name, ybeg=2000, yend=2699)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='MPI-ESM-LR', name=expe_name, ybeg=1850, yend=2849)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='MRI-CGCM3', name=expe_name, ybeg=1851, yend=2350)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='NorESM1-M', name=expe_name, ybeg=700, yend=1200)))
    return dict_allexpes


def dict_expes_CMIP5_historical(project_name):
    '''
    Define a specific dict of Expe-s for CMIP-5 historical-related studies
    '''
    dict_allexpes = {}
    expe_name = 'historical'
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='bcc-csm1-1', name=expe_name, member=[1,2,3], ybeg=1850, yend=2005)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='BNU-ESM', name=expe_name, member=[1], ybeg=1850, yend=2005)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='CanESM2', name=expe_name, member=[1,2,3,4,5], ybeg=1850, yend=2005)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='CCSM4', name=expe_name, member=[1,2,3,4,5,6], ybeg=1850, yend=2005)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='CSIRO-Mk3-6-0', name=expe_name, member=[1,2,3,4,5,6,7,8,9,10], ybeg=1850, yend=2005)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='FGOALS-s2', name=expe_name, member=[1,2,3], ybeg=1850, yend=2005)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='GFDL-ESM2M', name=expe_name, member=[1], ybeg=1850, yend=2005)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='HadGEM2-ES', name=expe_name, member=[1,2,3,4], ybeg=1850, yend=2005)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='inmcm4', name=expe_name, member=[1], ybeg=1850, yend=2005)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='IPSL-CM5A-LR', name=expe_name, member=[1,2,3,4,5,6], ybeg=1850, yend=2005)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='MIROC5', name=expe_name, member=[1,2,3,4], ybeg=1850, yend=2005)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='MPI-ESM-LR', name=expe_name, member=[1], ybeg=1850, yend=2005)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='MRI-CGCM3', name=expe_name, member=[1,2,3], ybeg=1850, yend=2005)))
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='NorESM1-M', name=expe_name, member=[1,2,3], ybeg=1850, yend=2005)))
    return dict_allexpes


def dict_expes_CMIP5_abrupt4xCO2(project_name):
    '''
    Define the specific dict of Expe-s for CMIP-5 abrupt4xCO2-related studies
    '''
    dict_allexpes = {}
    expe_name_CTL = 'piControl'
    expe_name = 'abrupt4xCO2'
    eCTL = Expe(project=project_name, model='bcc-csm1-1', name=expe_name_CTL, ybeg=1, yend=500)
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='bcc-csm1-1', name=expe_name, expe_control=eCTL, ybeg=160, yend=309)))
    eCTL = Expe(project=project_name, model='BNU-ESM', name=expe_name_CTL, ybeg=1450, yend=2008)
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='BNU-ESM', name=expe_name, expe_control=eCTL, ybeg=1850, yend=1999)))
    eCTL = Expe(project=project_name, model='CanESM2', name=expe_name_CTL, ybeg=2015, yend=3010)
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='CanESM2', name=expe_name, expe_control=eCTL, ybeg=1850, yend=1999)))
    eCTL = Expe(project=project_name, model='CCSM4', name=expe_name_CTL, ybeg=250, yend=1300)
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='CCSM4', name=expe_name, expe_control=eCTL, ybeg=1850, yend=1999)))
    eCTL = Expe(project=project_name, model='CNRM-CM5', name=expe_name_CTL, ybeg=1850, yend=2699)
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='CNRM-CM5', name=expe_name, expe_control=eCTL, ybeg=1850, yend=1999)))
    eCTL = Expe(project=project_name, model='CSIRO-Mk3-6-0', name=expe_name_CTL, ybeg=1, yend=500)
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='CSIRO-Mk3-6-0', name=expe_name, expe_control=eCTL, ybeg=1, yend=150)))
    eCTL = Expe(project=project_name, model='FGOALS-s2', name=expe_name_CTL, ybeg=1850, yend=2350)
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='FGOALS-s2', name=expe_name, expe_control=eCTL, ybeg=1850, yend=1999)))
    eCTL = Expe(project=project_name, model='GFDL-ESM2M', name=expe_name_CTL, ybeg=1, yend=500)
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='GFDL-ESM2M', name=expe_name, expe_control=eCTL, ybeg=1, yend=150)))
    eCTL = Expe(project=project_name, model='HadGEM2-ES', name=expe_name_CTL, ybeg=1860, yend=2434)
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='HadGEM2-ES', name=expe_name, expe_control=eCTL, ybeg=1860, yend=2009)))
    eCTL = Expe(project=project_name, model='inmcm4', name=expe_name_CTL, ybeg=1860, yend=2349)
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='inmcm4', name=expe_name, expe_control=eCTL, ybeg=2090, yend=2239)))
    eCTL = Expe(project=project_name, model='IPSL-CM5A-LR', name=expe_name_CTL, ybeg=1800, yend=2799)
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='IPSL-CM5A-LR', name=expe_name, expe_control=eCTL, ybeg=1850, yend=1999)))
    eCTL = Expe(project=project_name, model='MIROC5', name=expe_name_CTL, ybeg=2000, yend=2699)
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='MIROC5', name=expe_name, expe_control=eCTL, ybeg=2100, yend=2250)))
    eCTL = Expe(project=project_name, model='MPI-ESM-LR', name=expe_name_CTL, ybeg=1850, yend=2849)
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='MPI-ESM-LR', name=expe_name, expe_control=eCTL, ybeg=1850, yend=1999)))
    eCTL = Expe(project=project_name, model='MRI-CGCM3', name=expe_name_CTL, ybeg=1851, yend=2350)
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='MRI-CGCM3', name=expe_name, expe_control=eCTL, ybeg=1851, yend=2000)))
    eCTL = Expe(project=project_name, model='NorESM1-M', name=expe_name_CTL, ybeg=700, yend=1200)
    dict_allexpes.update(dict_exp(Expe(project=project_name, model='NorESM1-M', name=expe_name, expe_control=eCTL, ybeg=1, yend=150)))
    return dict_allexpes


def dict_expes_stab_article(project_name, rootdir='/cnrm/amacs/USERS/stmartin/DATA', extra_expes=False):
    '''
    Define the specific dict of Expe-s for stabilization study
    '''
    model_name = 'CNRM-CM6-1'
    dict_allexpes = {}
    eCTL = Expe(project=project_name, model=model_name, name='piControl', ybeg=1850, yend=2349, marker=',', color='silver')
    dict_allexpes.update(dict_exp(eCTL))
    expes = {}
    expes['abrupt-4xCO2'] = [1850, 2849, '.', 'dimgray', 'abrupt-4xCO2']
    expes['abrupt-2xCO2'] = [1850, 2599, ',', 'black', 'abrupt-2xCO2']
    expes['stab-1p4xCO2-dab'] = [1969, 2468, '.', 'purple', 'FF-1p4xCO2']
    expes['stab-2xCO2-dab'] = [2137, 2636, '.', 'orangered', 'FF-2xCO2']
    expes['stab-2p8xCO2-dab'] = [2424, 2923, '.', 'orange', 'FF-2p8xCO2']
    expes['expo-2xCO2'] = [1850, 2349, '.', 'dodgerblue', 'expo-2xCO2']
    expes['stab-2xCO2-tab8x'] = [2000, 2399, '.', 'green', 'FF-2xCO2-3step']
    if extra_expes:    
        expes['stab-4xCO2-tab8x'] = [2074, 2303, '.', 'crimson', 'FF-4xCO2-3step']
        #@ expes['expo-4xCO2'] = [1850, 2049, '.', 'dodgerblue', 'expo-2xCO2']
        expes['expo-4xCO2'] = [1850, 2049, '.', 'dodgerblue', 'expo-2xCO2']
    for e_ in expes.keys():
        ybeg = expes[e_][0]
        yend = expes[e_][1]
        marker = expes[e_][2]
        color = expes[e_][3]
        label = expes[e_][4]
        dict_allexpes.update(dict_exp(Expe(project=project_name, model=model_name, name=e_, ybeg=ybeg, yend=yend, adds=dict(root=rootdir), expe_control=eCTL, marker=marker, color=color, label=label)))
    return dict_allexpes


def dict_expes_historical_CNRMCM(project_name, model_name, n_member=10, ybeg=1850, yend=2014, yend_piControl=0):
    '''
    Define a specific dict of Expe-s for CNRM-CM6-1 (or CNRM-CM5) historical simulations
    '''
    dict_allexpes = {}
    eCTL = None
    if yend_piControl > 0:
        # -- add piControl experiment to the dict of Expe-s
        eCTL = Expe(project=project_name, model=model_name, name='piControl', ybeg=1850, yend=yend_piControl, marker=',', color='silver')
        dict_allexpes.update(dict_exp(eCTL))
    for n in range(n_member):
        dict_allexpes.update(dict_exp(Expe(project=project_name, model=model_name, name='historical', number=n+1, ybeg=ybeg, yend=yend, expe_control=eCTL, marker=',', color='dimgray')))
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
    datasets[(name, 'tas', 'brut')] = xds[varname]
