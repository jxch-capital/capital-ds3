import baostock as bs
import pandas as pd
import service.bs.bs_base_service as bs_base_service
import controller.grafana.a_base_api as a_base_api
import core.bs_base as bs_base

df = a_base_api.stock_industry_sw()

print(df)