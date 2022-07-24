import datetime, time

default_fmt = '%Y-%m-%d'


def now_date_str(fmt=default_fmt):
    return datetime.date.today().strftime(fmt)


def time_to_str(the_time, fmt=default_fmt):
    return time.strftime(fmt, time.localtime(the_time))


def str_to_time(date_str, fmt=default_fmt):
    time_arr = time.strptime(date_str, fmt)
    return int(time.mktime(time_arr))
