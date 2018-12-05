from climaf.api import *
from mafate import *

# -- Define specific CLIMAF projects
define_CLIMAF_projects()

# -- Define dict of expes and of vars
# -- Use predefined dictionnaries
dictexps = {}
dictexps.update(dict_exp(Expe(project='CMIP6', model='CNRM-CM6-1', name='piClim-control', number=1, adds=dict(root='/home/stmartin/work/lxamacs/data/brutes'), ybeg=1850, yend=1879)))
dictvars = {}
dictvars.update(dict_var('pr', 'Amon'))
dictvars.update(dict_var('tas', 'Amon'))

# -- Load data (with operation fld_year_avg)
datasets = load_datas(dictexps, dictvars, operation=cdogen, list_cdops=['fldmean'], verbose=True, computeMean=False, computeAnom=False, add_rnet=False)

ds = datasets['piClim-control']
print(ds)
# ds.to_netcdf('test.nc')

z = ds.groupby('time.month').mean(dim='time')
print(z)

z = ds.groupby('time.season').mean(dim='time')
print(z)

exit()
