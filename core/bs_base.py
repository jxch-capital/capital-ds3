import baostock as bs
import pandas as pd
from functools import lru_cache
from core.bs_support import login
from utils.scheduler_utils import scheduler


def rs_to_dataframe(rs):
    data_list = []
    while (rs.error_code == '0') & rs.next():
        data_list.append(rs.get_row_data())
    return pd.DataFrame(data_list, columns=rs.fields)


@lru_cache(maxsize=10000)
@login
def query_stock_basic_by_code(code):
    rs = bs.query_stock_basic(code=code)
    return rs_to_dataframe(rs)


@lru_cache(maxsize=10000)
@login
def query_stock_basic_by_name(name):
    rs = bs.query_stock_basic(code_name=name)
    return rs_to_dataframe(rs)


@lru_cache(maxsize=10000)
@login
def query_name_by_code(code):
    rs = bs.query_stock_basic(code=code)
    df = rs_to_dataframe(rs)
    if df.empty is False:
        return df['code_name'][0]
    else:
        raise TypeError(f'找不到{code}对应的code_name, 搜索结果:{df}')


@lru_cache(maxsize=10000)
@login
def query_code_by_name(name):
    rs = bs.query_stock_basic(code_name=name)
    df = rs_to_dataframe(rs)
    if df.empty is False:
        return df['code'][0]
    else:
        raise TypeError(f'找不到{name}对应的code, 搜索结果:{df}')


@lru_cache(maxsize=1)
@login
def query_stock_industry():
    rs = bs.query_stock_industry()
    return rs_to_dataframe(rs)


@scheduler.scheduled_job('cron', id='bs_base:cache_clear', day_of_week='mon')
def cache_clear():
    query_stock_basic_by_code.cache_clear()
    query_stock_basic_by_name.cache_clear()
    query_name_by_code.cache_clear()
    query_code_by_name.cache_clear()
    query_stock_industry.cache_clear()
