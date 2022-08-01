from flask import Blueprint, request
from pre_request import pre, Rule

import core.bs_base as bs_base
import service.bs.bs_base_service as bs_base_service

a_base_api = Blueprint('a_base_api', __name__)


@a_base_api.route("/grafana/codes_to_names", methods=["GET"])
@pre.catch(get={"codes": Rule(type=list, required=True, dest="codes")})
def codes_to_names():
    codes = request.args.getlist('codes')
    names = bs_base_service.query_names_by_codes(codes)
    return bs_base_service.codes_names_json(codes, names)


@a_base_api.route("/grafana/names_to_codes", methods=["GET"])
@pre.catch(get={"names": Rule(type=list, required=True, dest="names")})
def names_to_codes():
    names = request.args.getlist('names')
    codes = bs_base_service.query_codes_by_names(names)
    return bs_base_service.codes_names_json(codes, names)


@a_base_api.route("/grafana/stock_basic_by_code", methods=["GET"])
@pre.catch(get={"code": Rule(type=str, required=True, dest="code")})
def stock_basic_by_code():
    code = request.args['code']
    return bs_base.query_stock_basic_by_code(code).to_json(orient='records', force_ascii=False)


@a_base_api.route("/grafana/stock_basic_by_name", methods=["GET"])
@pre.catch(get={"name": Rule(type=str, required=True, dest="name")})
def stock_basic_by_name():
    name = request.args['name']
    return bs_base.query_stock_basic_by_name(name).to_json(orient='records', force_ascii=False)


@a_base_api.route("/grafana/stock_industry_sw", methods=["GET"])
def stock_industry_sw():
    return bs_base.query_stock_industry().to_json(orient='records', force_ascii=False)
