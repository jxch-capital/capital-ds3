import core.bs_daily as bs_daily
import core.bs_base as bs_base
from utils import date_utils


def query_daily_index_by_codes(codes, start, end=date_utils.now_date_str()):
    return [{'code': code,
             'name': bs_base.query_name_by_code(code),
             'k': bs_daily.query_daily_by_code(code, start, end).to_dict('records')
             } for code in codes]




