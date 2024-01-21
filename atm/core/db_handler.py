# handle all the database transaction

import json
import os
import time

from atm.conf import settings


def file_db_handle(conn_params):
    print("db:", conn_params)
    return file_execute


def db_handler():
    conn_params = settings.DATABASE
    if conn_params['engine'] == 'file_storage':
        return file_db_handle(conn_params)
    elif conn_params['engine'] == 'mysql':
        pass


def file_execute(sql, **kwargs):
    conn_params = settings.DATABASE
    db_path = "%s/%s" % (conn_params['path'], conn_params['name'])

    print(sql, db_path)
    sql_list = sql.split("where")
    print(sql_list)

    # select 查询账户信息并返回账户信息数据
    if sql_list[0].startswith("select") and len(sql_list) > 1:  # select and where
        column, val = sql_list[1].strip().split("=")

        if column == "account":
            account_file = "%s/%s.json" % (db_path, val)
            print(account_file)
            if os.path.isfile(account_file):
                with open(account_file, 'r') as f:
                    account_data = json.load(f)
                    return account_data
            else:
                exit("Account %s is not exist!" % val)

    # update 更新账户数据
    elif sql_list[0].startswith("update") and len(sql_list) > 1:  # update and where
        column, val = sql_list[1].strip().split("=")
        if column == "account":
            account_file = "%s/%s.json" % (db_path, val)
            if os.path.isfile(account_file):
                account_data = kwargs.get('account_data')
                with open(account_file, 'w') as f:
                    json.dump(account_data, f)
                return True
