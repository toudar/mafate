from climaf.api import *
from mafate import *

# -- Define specific CLIMAF projects
define_CLIMAF_projects()

# -- Define dict of expes and of vars
# -- Use predefined dictionnaries
dictexps = {}
dictexps.update(dict_expes_CMIP5_piControl('multiCMIP5'))
dictexps.update(dict_expes_historical_CNRMCM('multiCMIP5', 'CNRM-CM5', ybeg=1850, yend=2010, with_piControl=True))
dictexps.update(dict_expes_historical_CNRMCM('CMIP6', 'CNRM-CM6-1', ybeg=1850, yend=2014, with_piControl=True))

dictvars = {}
dictvars.update(dict_vars_T())

# -- Or use your own experiment-s and variable-s
eCTL = Expe(project='CMIP6', model='CNRM-CM6-1', name='piControl', ybeg=1850, yend=2349, marker=',', color='silver')
add_expe_dict(dictexps, eCTL)
add_expe_dict(dictexps, Expe(project='STAB', model='CNRM-CM6-1', name='expo-4xCO2', ybeg=1850, yend=2049, expe_control=eCTL, marker='.', color='dodgerblue'))

dictvars.update(dict_var('pr', 'Amon'))

# -- Load data (with operation fld_year_avg)
datasets = load_datas(dictexps, dictvars, operation=fld_year_avg, verbose=True)

exit()
