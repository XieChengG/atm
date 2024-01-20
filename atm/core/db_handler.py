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

    if sql_list[0].startswith("select") and len(sql_list) > 1:  # select and where
        column, val = sql_list[1].strip().split("=")
