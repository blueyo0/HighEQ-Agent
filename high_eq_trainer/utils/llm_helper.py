import time
import logging


def timer(func):
    def func_in(*args, **kw):
        start_time = time.time()
        ret = func(*args, **kw)
        end_time = time.time()
        spend_time = (end_time - start_time)
        logging.info("spent {} s".format(spend_time))
        return ret
    return func_in


