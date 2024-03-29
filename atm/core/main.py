from core import auth
from core import accounts
from core import logger
from core import transaction
from core.auth import login_required

import time

# 创建日志记录器
trans_logger = logger.logger('transaction')
access_logger = logger.logger('access')

exit_flat = False

# 临时账户数据
user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}


def account_info(acc_data):
    print(acc_data)


@login_required
def repay(acc_data):
    """
    打印当前余额，用户还款
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
        elif repay_amount == 'b':
            back_flag = True
        else:
            print("[%s] is not valid amount, only accept integer!" % repay_amount)


def withdraw(acc_data):
    """
    打印当前余额，并让用户取款
    :param acc_data:
    :return:
    """
    # 从数据库中获取当前用户的账户数据
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = '''--------BALANCE INFO--------
            Credit: %s
            Balance: %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("Input withdraw amount:").strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)
            if new_balance:
                print("New balance: %s" % new_balance['balance'])
        elif withdraw_amount == 'b':
            back_flag = True
        else:
            print("[%s] is not valid amount, only accept integer!" % withdraw_amount)


def transfer(acc_data):
    """
    用户转账
    :param acc_data:
    :return:
    """
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = """--------Balance Info--------
            Credit: %s
            Balance: %s""" % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        transfer_amount = input("Input transfer amount:").strip()
        if len(transfer_amount) > 0 and transfer_amount.isdigit():
            data = transaction.make_transaction(trans_logger, account_data, 'transfer', transfer_amount)
            if data:
                print("New balance after transfer: %s" % data['balance'])
            else:
                print("Transfer Failed!")
        elif transfer_amount == 'b':
            back_flag = True
        else:
            print("[%s] is not invalid amount, only accept integer!" % transfer_amount)


def pay_check(acc_data):
    """
    用户查询账单
    :param acc_data:
    :return:
    """
    account_data = acc_data['account_data']
    bill_info = """--------Bill Info--------
        Credit: {credit}
        Balance: {balance}
        Enroll_date: {enroll_date}
        Expire_date: {expire_date}
        Pay_day: {pay_day}"""
    print(bill_info.format(credit=account_data['credit'], balance=account_data['balance'],
                           enroll_date=account_data['enroll_date'], expire_date=account_data['expire_date'],
                           pay_day=account_data['pay_day']))


def logout(acc_data):
    """
    用户退出菜单
    :param acc_data:
    :return:
    """
    global exit_flat
    exit_flat = True
    return exit_flat


def interactive(acc_data):
    """
    ATM机用户交互界面
    :param acc_data:
    :return:
    """
    # 界面菜单
    menu = u'''
    -------- PEOPLE BANK --------
    1. 账户信息
    2. 还款
    3. 取款
    4. 转账
    5. 查账单
    6. 退出
    '''

    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout
    }

    global exit_flat
    exit_flat = False
    while not exit_flat:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)
        else:
            print("Option is not exist!")


def run():
    """
    程序启动后会调用该函数，处理用户交互
    :return:
    """
    acc_data = auth.acc_login(user_data, access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)
