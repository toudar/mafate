# MAFATE : CliMAF Automatic Treatment Extension

A Python package for extending CliMAF application

**Requirements**

`mafate` only requires [`climaf`](http://climaf.readthedocs.org), [`numpy`](http://numpy.org) and [`xarray`](http://xarray.pydata.org)

**Contents**

* `varexpe.py` : definition of classes Expe and Var
* `utils.py` : provide some useful utilities
* `example.py` : a simple example to getting started

**Getting started**

> Define specific CLIMAF projects
```python
from climaf.api import *
from mafate import *

define_CLIMAF_projects()
```

> Define a specific dict of experiments and of vars : use predefined dictionnaries...
```python
dictexps = {}
dictexps.update(dict_expes_CMIP5_historical('multiCMIP5'))
dictexps.update(dict_expes_historical_CNRMCM('multiCMIP5', 'CNRM-CM5', ybeg=1850, yend=2010, with_piControl=True))
dictexps.update(dict_expes_historical_CNRMCM('CMIP6', 'CNRM-CM6-1', ybeg=1850, yend=2014, with_piControl=True))

dictvars = {}
dictvars.update(dict_vars_T())
```

> ...or use your own experiment-s and variable-s
```python
eCTL = Expe(project='CMIP6', model='CNRM-CM6-1', name='piControl', ybeg=1850, yend=2349, marker=',', color='silver')
add_expe_dict(dictexps, eCTL)
add_expe_dict(dictexps, Expe(project='STAB', model='CNRM-CM6-1', name='expo-4xCO2', ybeg=1850, yend=2049, expe_control=eCTL, marker='.', color='dodgerblue'))

dictvars.update(dict_var('pr', 'Amon'))
```

> Load data (with operation fld_year_avg)
```python
datasets = load_datas(dictexps, dictvars, operation=fld_year_avg, verbose=True)
```
