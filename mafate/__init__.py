version = '0.1'

print('mafate version = '+version)

from .utils import fld_year_avg, zon_year_avg, Id, define_CLIMAF_projects, add_expe_dict, dict_reanalyses, dict_expes_CMIP5_piControl, dict_expes_CMIP5_historical, dict_expes_CMIP5_abrupt4xCO2, dict_expes_stab_article, dict_expes_historical_CNRMCM, dict_var, dict_vars_T, dict_vars_NT, dict_vars_heatc, load_datas, load_HadCRU_data
from .varexpe import Expe, Variable
