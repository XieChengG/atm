from atm.core import auth
from atm.core import accounts
from atm.core import logger
from atm.core import transaction
from auth import login_required

import time

# 创建日志记录器
trans_logger = logger.logger('transaction')
access_logger = logger.logger('access')

# 临时账户数据
user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}


def account_info(acc_data):
    print(user_data)


def repay(acc_data):
    """
    打印当前余额，用户支付账单
    :param acc_data:
    :return:
    """
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = '''--------BALANCE INFO--------
                 Credit: %s
                 Balance: %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input("Input repay amount:").strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'repay', repay_amount)
            if new_balance:
                print("New balance: %s" % new_balance['balance'])
        else:
            print("[%s] is not valid amount, only accept integer!"%repay_amount)

        if repay_amount == 'b':
            back_flag = True


