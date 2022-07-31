import pandas_datareader as pdr
from functools import lru_cache

from core import k_index
from utils.log_utils import log


@lru_cache(maxsize=10000, typed=True)
@log
def query_daily_by_code(code, start, end):
    df = pdr.get_data_stooq(code, start, end)
    df = k_index.stockstats_default(df)
    df['date'] = df['Date']
    return df

