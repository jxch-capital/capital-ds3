import logging

import baostock as bs
from flask import Blueprint
from flask import request

from controller.grafana.a_base_api import a_base_api
from controller.grafana.a_daily_api import a_daily_api

logging.basicConfig(level=logging.INFO)

base_api = Blueprint('base_api', __name__)


@base_api.route("/grafana/", methods=["get"])
def grafana_root():
    return '{"status":"success"}'


@a_daily_api.before_request
@a_base_api.before_request
def bs_daily_api_before_request():
    if request.method == "POST":
        logging.info(f"----> request_path: {request.path}, request: {request.json}")
    elif request.method == "GET":
        logging.info(f"----> request_path: {request.path}, request: {request.args}")
    bs.login()


@a_daily_api.before_request
@a_base_api.after_request
def bs_daily_api_after_request(resp):
    bs.logout()
    if request.method == "POST":
        logging.info(f"<---- request_path: {request.path}, request: {request.json}")
    elif request.method == "GET":
        logging.info(f"----> request_path: {request.path}, request: {request.args}")
    return resp
