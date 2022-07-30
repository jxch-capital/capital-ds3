from datetime import datetime, date
from config import date_fmt_config


def json_dumps_grafana_date(obj):
    if isinstance(obj, datetime):
        return obj.strftime(date_fmt_config.grafana_fmt)
    elif isinstance(obj, date):
        return obj.strftime(date_fmt_config.grafana_fmt)
    else:
        return obj
