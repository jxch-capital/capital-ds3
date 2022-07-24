import json

from flask import Blueprint, request
import service.bs.bs_daily_index_service as bs_daily_index_service
from pre_request import pre, Rule
import utils.date_utils as date_utils

a_daily_index_api = Blueprint('a_daily_index_api', __name__)


@a_daily_index_api.route("/grafana/daily_index_by_codes", methods=["POST"])
@pre.catch(post={
    "codes": Rule(type=list, required=True, dest="codes"),
    "start": Rule(type=int, required=True, dest="start"),
    "end": Rule(type=int, required=True, dest="end")
})
def daily_index_by_codes():
    codes = request.json.get('codes')
    start = date_utils.time_to_str(request.json.get('start'))
    end = date_utils.time_to_str(request.json.get('end'))
    k_list = bs_daily_index_service.query_daily_index_by_codes(codes, start, end)
    return json.dumps(k_list, ensure_ascii=False)
