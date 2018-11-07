# MAFATE

A Python package for extending CliMAF application (CliMAF Automatic Treatment Examples)

# References

https://github.com/senesis/climaf

# Quick Start

Define specific CLIMAF projects
```python
from climaf.api import *
from mafate import *

define_CLIMAF_projects()
```

Define a specific dict of experiments and of vars
```python
my_dictexps = {}
add_expe_dict(my_dictexps, Expe(project='CMIP6', model='CNRM-CM6-1', name='historical', member=[1], ybeg=2000, yend=2000, marker=',', color='black'))

my_dictvars = {}
my_dictvars.update(dict_var('ua', 'Amon'))
my_dictvars.update(dict_var('va', 'Amon'))
```

Load datas
```python
datasets = load_datas(my_dictexps, my_dictvars, Id, verbose=True)
```

