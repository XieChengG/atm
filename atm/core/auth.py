import time

from atm.core import db_handler
from atm.core import logger
from atm.conf import settings


def acc_auth(account, password):
    """
    账户认证
    :param account:
    :param password:
    :return:
    """
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account)

    if data['password'] == password:
        exp_time_stamp = time.mktime(time.strptime(data['expire_date'], "%Y-%m-%d"))
        if time.time() > exp_time_stamp:
            print("Account [%s] has expired" %account)
        else:
            return data
    else:
        print("Account ID or password is incorrect")







