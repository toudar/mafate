from climaf.api import *
from mafate import *

# -- Define specific CLIMAF projects
define_CLIMAF_projects()

# -- Define dict of expes and of vars
# -- Use predefined dictionnaries
dictexps = {}
dictexps.update(dict_exp(Expe(project='CMIP6', model='CNRM-CM6-1', name='piClim-control', adds=dict(root='/home/stmartin/work/lxamacs/data/brutes'), ybeg=1850, yend=1879)))
dictvars = {}
dictvars.update(dict_var('pr', 'Amon'))

# -- Load data (with operation fld_year_avg)
datasets = load_datas(dictexps, dictvars, operation=cdogen, list_cdops=['zonmean', 'yearavg'], writeFiles=True, verbose=True)

exit()
