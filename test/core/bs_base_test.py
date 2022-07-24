import core.bs_base as bs_base
import baostock as bs


bs.login()

df = bs_base.query_name_by_code('sh.601318')

print(df)

bs.logout()

