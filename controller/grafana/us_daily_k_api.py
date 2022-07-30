import json
from flask import Blueprint, request
from pre_request import pre, Rule
import utils.date_utils as date_utils
from service.stoop import us_daily_k_service
from config import date_fmt_config
from utils import json_utils

us_daily_k_api = Blueprint('us_daily_k_api', __name__)


@us_daily_k_api.route("/grafana/us_daily_k_by_codes", methods=["POST"])
@pre.catch(post={
    "codes": Rule(type=list, required=True, dest="codes"),
    "start": Rule(type=int, required=True, dest="start"),
    "end": Rule(type=int, required=True, dest="end")
})
def us_daily_k_by_codes():
    codes = request.json.get('codes')
    start = date_utils.time_to_str(request.json.get('start'), date_fmt_config.stooq_fmt)
    end = date_utils.time_to_str(request.json.get('end'), date_fmt_config.stooq_fmt)
    k_list = us_daily_k_service.query_us_daily_k_by_codes(codes, start, end)
    return json.dumps(k_list, ensure_ascii=False, default=json_utils.json_dumps_grafana_date)
