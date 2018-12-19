# MAFATE : CliMAF Automatic Treatment Extension

A Python package for extending CliMAF application

**Requirements**

`mafate` only requires [`climaf`](http://climaf.readthedocs.org), [`numpy`](http://numpy.org) and [`xarray`](http://xarray.pydata.org).
It can also require [`iris`](https://scitools.org.uk/iris/docs/latest).

**Contents**

* `varexpe.py` : definition of classes Expe and Var
* `utils.py` : provide some useful utilities
* `examples.py` : simple examples to getting started

**Getting started**

> Define specific CLIMAF projects
```python
from climaf.api import *
from mafate import *

define_CLIMAF_projects()
```

> Define a specific dict of experiments and of vars : use predefined dictionnaries...
```python
dictvars = {}
dictvars.update(dict_vars_T())

dictvars = {}
dictvars.update(dict_var('tas', 'Amon'))
```

> to access to the Var object : dictvars[var.name], e.g. dictvars['tas']
```python
print(type(dictvars['tas']))
print(dictvars['tas'])
```

> Define a specific dict of experiments (or use pre-defined dictionnaries)
```python
dictexps = {}
dictexps.update(dict_expes_historical_CNRMCM('CMIP5', 'CNRM-CM5', n_member=3, ybeg=1981, yend=2010, yend_piControl=2349))
dictexps.update(dict_expes_historical_CNRMCM('CMIP6', 'CNRM-CM6-1', n_member=3, ybeg=1981, yend=2010, yend_piControl=2349))
dictexps.update(dict_exp(Expe(project='CMIP6', model='CNRM-CM6-1', name='expo-2xCO2', number=1, adds=dict(root='/cnrm/amacs/USERS/stmartin/DATA'), ybeg=1850, yend=1879)))
```

> to access to the Expe object : dictexps[exp.expid()], e.g. dictexps['CNRM-CM5_historical_r2']
```python
print(type(dictexps['CNRM-CM5_historical_r2']))
print(dictexps['CNRM-CM5_historical_r2'])
```

> Load data
```python
dict_datasets = load_datas(dictexps, dictvars, operation=cdogen, list_cdops=['fldmean'], verbose=True)
```

> dict_datasets is a python dictionnary of xarray Datasets or iris objects
> dict_datasets['expe.name'], e.g. dict_datasets['historical'] contains all variables/members/models relatives to experiment 'historical'
```python
print(dict_datasets['historical'])
```

> examples of use of xarray dataset
> to select a Dataset specific to an specific experiment
```python
ds = extract_from_exp(dict_datasets, dictexps['CNRM-CM5_historical_r2'])
print(type(ds))
ds = dict_datasets['piControl'].sel(model='CNRM-CM6-1', member=1)
print(ds)
```

> to compute DJF seasonal mean for all variables/members/models
```python
ds = dict_datasets['historical'].groupby('time.season').mean(dim='time').sel(season='DJF')
print(ds)
```

> to compute ensemble mean for a specific model
```python
ds = dict_datasets['historical'].sel(model='CNRM-CM6-1').mean(dim='member')
print(ds)
```

> selection by index and selection by labels
```python
arr = dict_datasets['piControl'].sel(member=1, model='CNRM-CM5').isel(lon=0, lat=0, time=np.arange(0,10))['tas'].values
print(arr)
```

> add a variable in the dataset
```python
dict_datasets['historical']['tas_deg'] = dict_datasets['historical']['tas'] - 273.15
print(dict_datasets['historical']['tas_deg'])
```
