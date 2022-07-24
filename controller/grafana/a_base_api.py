import logging

from flask import Blueprint, request

import service.bs.bs_base_service as bs_base

logging.basicConfig(level=logging.INFO)

a_base_api = Blueprint('a_base_api', __name__)


@a_base_api.route("/grafana/codes_to_names", methods=["GET"])
def codes_to_names():
    codes = request.args['codes']
    if codes is None:
        raise TypeError(f'codes is None, request: {request.json}')
    return bs_base.query_names_by_codes(codes)



