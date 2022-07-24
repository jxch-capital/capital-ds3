import core.bs_base as bs_base


def query_names_by_codes(codes):
    return [bs_base.query_name_by_code(code) for code in codes]






