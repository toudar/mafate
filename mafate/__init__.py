version = '0.3'

print('mafate version = '+version)

from .utils import cdogen, define_CLIMAF_project, dict_exp, dict_var, load_datas

from .varexpe import Expe, Variable

from .dicts import define_CLIMAF_projects, dict_reanalyses, dict_expes_CMIP5_piControl, dict_expes_CMIP5_historical, dict_expes_CMIP5_abrupt4xCO2, dict_expes_stab_article, dict_expes_stab_article_0, dict_expes_historical_CNRMCM, dict_vars_T, dict_vars_NT, dict_vars_heatc, load_HadCRU_data, extract_from_exp, compute_anom_from_control
