import baostock as bs
import service.bs.bs_base_service as bs_base_service
import service.bs.bs_daily_index_service as bs_daily_index_service

df = bs_daily_index_service.query_daily_index_by_codes(['sh.601318'], '2022-07-01')
# df = bs_base_service.bs_daily_index_service(['sh.000001','sh.601318'])
print(df)
