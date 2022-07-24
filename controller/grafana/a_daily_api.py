from flask import Blueprint, request
import baostock as bs
import logging

logging.basicConfig(level=logging.INFO)

a_daily_api = Blueprint('a_daily_api', __name__)





