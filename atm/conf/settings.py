import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': "%s/db" % BASE_DIR
}

LOG_LEVEL = logging.INFO
LOG_TYPE = {
    'transaction': 'transaction.log',
    'access': 'access.log'
}

TRANSACTION_TYPE = {
    'repay': {'action': 'plus', 'interest': 0},  # 还款
    'withdraw': {'action': 'minus', 'interest': 0.05},  # 取款
    'transfer': {'action': 'minus', 'interest': 0.05},  # 转账
    'consume': {'action': 'minus', 'interest': 0}  # 刷卡消费
}
