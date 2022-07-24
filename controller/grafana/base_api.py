import json
import logging

import baostock as bs
from flask import Blueprint
from flask import request

from controller.grafana.a_base_api import a_base_api
from controller.grafana.a_daily_index_api import a_daily_index_api

base_api = Blueprint('base_api', __name__)


@base_api.route("/grafana/", methods=["get"])
def grafana_root():
    return '{"status":"success"}'


@a_daily_index_api.before_request
@a_base_api.before_request
def before_request():
    logging.info(f"----> request: {request}")
    bs.login()


@a_daily_index_api.after_request
@a_base_api.after_request
def after_request(resp):
    bs.logout()
    logging.info(f"<---- request: {request}")
    return resp
