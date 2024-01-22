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
            print("Account [%s] has expired" % account)
        else:
            return data
    else:
        print("Account ID or password is incorrect")


def acc_login(user_data, log_obj):
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input("account:").strip()
        password = input("password:").strip()
        auth = acc_auth(account, password)
        if auth:
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            return auth
        retry_count += 1
    else:
        log_obj.error("account [%s] attempts to login too many times" % account)
        exit()
