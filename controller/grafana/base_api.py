import logging

from flask import Blueprint
from flask import request

from controller.grafana.a_base_api import a_base_api
from controller.grafana.a_daily_index_api import a_daily_index_api
from controller.grafana.us_daily_k_api import us_daily_k_api

base_api = Blueprint('base_api', __name__)


@base_api.route("/grafana/", methods=["get"])
def grafana_root():
    return '{"status":"success"}'


@us_daily_k_api.before_request
@a_daily_index_api.before_request
@a_base_api.before_request
def before_request():
    logging.info(f"----> request: {request}")


@us_daily_k_api.after_request
@a_daily_index_api.after_request
@a_base_api.after_request
def after_request(resp):
    logging.info(f"<---- request: {request}")
    return resp
