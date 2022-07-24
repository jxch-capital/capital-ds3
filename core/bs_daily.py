from functools import lru_cache

import baostock as bs
import pandas as pd

import core.bs_base as bs_base
import core.k_index as k_index


@lru_cache(maxsize=10000, typed=True)
def query_daily_by_code(code, start_date_str, end_date_str):
    rs = bs.query_history_k_data_plus(code,
                                      "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,"
                                      "tradestatus,pctChg,isST",
                                      start_date=start_date_str, end_date=end_date_str, frequency="d",
                                      adjustflag="3")
    df = bs_base.rs_to_dataframe(rs)
    df["open"] = pd.to_numeric(df["open"])
    df["high"] = pd.to_numeric(df["high"])
    df["low"] = pd.to_numeric(df["low"])
    df["close"] = pd.to_numeric(df["close"])
    df["preclose"] = pd.to_numeric(df["preclose"])
    df["volume"] = pd.to_numeric(df["volume"])
    df["amount"] = pd.to_numeric(df["amount"])
    df["adjustflag"] = pd.to_numeric(df["adjustflag"])
    df["turn"] = pd.to_numeric(df["turn"])
    df["tradestatus"] = pd.to_numeric(df["tradestatus"])
    df["pctChg"] = pd.to_numeric(df["pctChg"])
    df["isST"] = pd.to_numeric(df["isST"])
    codes = df['code']
    df.drop(columns=['code'])
    df = k_index.stockstats_default(df)
    df['code'] = codes
    return df
