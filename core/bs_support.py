import baostock as bs
import functools


def login(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        try:
            bs.login()
            return func(*args, **kw)
        finally:
            bs.logout()

    return wrapper
