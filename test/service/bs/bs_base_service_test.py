import baostock as bs
import service.bs.bs_base_service as bs_base_service


bs.login()

df = bs_base_service.query_names_by_codes(['sh.000001','sh.601318'])
print(df)

bs.logout()

