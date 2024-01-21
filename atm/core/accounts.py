import json
import time

from atm.core import db_handler


def load_current_balance(account_id):
    """
    加载当前账户余额
    :param account_id:
    :return:
    """
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account_id)
    return data


def dump_account(account_data):
    """
    更新账户数据到数据库文件
    :param account_data:
    :return:
    """
    db_api = db_handler.db_handler()
    data = db_api("update accounts where account=%s" % account_data['id'], account_data=account_data)
    return True
