from climaf.api import *
from mafate import *

#-- Define specific CLIMAF projects
define_CLIMAF_projects()

# -- Define dict of expes and of vars
my_dictexps = {}
add_expe_dict(my_dictexps, Expe(project='tmpCMIP6', model='CNRM-CM6-1', name='historical', member=[1], ybeg=2000, yend=2000, marker=',', color='black'))

my_dictvars = {}
my_dictvars.update(dict_var('ua', 'Amon'))
my_dictvars.update(dict_var('va', 'Amon'))

# -- Load data
datasets = load_datas(my_dictexps, my_dictvars, Id, verbose=True)

exit()
