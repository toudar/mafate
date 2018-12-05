from climaf.api import *
from mafate import *

# -- Define specific CLIMAF projects
define_CLIMAF_projects()

# -- Define dict of expes and of vars
# -- Use predefined dictionnaries
dictexps = {}
#_ dictexps.update(dict_expes_historical_CNRMCM('tmpCMIP6', 'CNRM-CM6-1', ybeg=1850, yend=2014, with_piControl=True))
dictexps.update(dict_exp(Expe(project='tmpCMIP6', model='bcc-csm1-1', name='historical', number=1, ybeg=1850, yend=2005)))    
dictexps.update(dict_exp(Expe(project='tmpCMIP6', model='bcc-csm1-1', name='piControl', number=1, ybeg=1, yend=500)))
dictexps.update(dict_exp(Expe(project='tmpCMIP6', model='GFDL-ESM2M', name='piControl', ybeg=1, yend=500)))
# dictexps.update(dict_exp(Expe(project='tmpCMIP6', model='CNRM-CM6-1', name='piControl', number=1, ybeg=1850, yend=2349)))

dictvars = {}
dictvars.update(dict_var('tas', 'Amon'))
dictvars.update(dict_var('rsdt', 'Amon'))

# dictvars.update(dict_var('tas', 'Amon'))

# -- Load data (with operation fld_year_avg)
datasets = load_datas(dictexps, dictvars, operation=cdogen, list_cdops=['zonmean', 'yearavg'], verbose=True, computeMean=False, computeAnom=False, add_rnet=False)

ds = datasets['piControl']
y = ds.sel(member=1, model='bcc-csm1-1').isel(time=np.arange(0,10))['tas'].values
print(y)

# selection
ds = datasets['piControl']
y = ds.sel(member=1, model='GFDL-ESM2M').isel(time=np.arange(0,10))['rsdt'].values
print(y)

# reduction
y = ds.sel(member=1, model='GFDL-ESM2M').mean(dim='time')
print(y)

if ds['rsut'] is not None:
    ds['toto'] = ds['tas'] + ds['rsut']

print(ds)

exit()

# ds['tas'].plot(col="member", col_wrap=3)
# y = ds.sel(lon=slice(-11, 3), lat=slice(35, 45)).sel(member=1, model='GFDL-ESM2M').mean(dim='time')
