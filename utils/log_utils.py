import functools
import logging


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        logging.info(f'func: {func}, args: {args}, kw: {kw}')
        return func(*args, **kw)

    return wrapper
