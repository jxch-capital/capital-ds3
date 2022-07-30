from utils import date_utils
from core import stooq_daily


def query_us_daily_k_by_codes(codes, start, end=date_utils.now_date_str('%Y%m%d')):
    return [{'code': code,
             'k': stooq_daily.query_daily_by_code(code, start, end).to_dict('records')
             } for code in codes]
