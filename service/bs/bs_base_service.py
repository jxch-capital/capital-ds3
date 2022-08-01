import json

import core.bs_base as bs_base


def query_names_by_codes(codes):
    return [bs_base.query_name_by_code(code) for code in codes]


def query_codes_by_names(names):
    return [bs_base.query_code_by_name(name) for name in names]


def codes_names_json(codes, names):
    return json.dumps({'codes': codes, 'names': names}, ensure_ascii=False)


def query_stock_industry():
    return bs_base.query_stock_industry().to_dict('records')
