from conf import settings
from core import accounts
from core import logger


def make_transaction(log_obj, account_data, tran_type, amount, **others):
    """
    :param log_obj:
    :param account_data: 用户账户数据
    :param tran_type: 交易类型
    :param amount: 交易金额
    :param others:
    :return:
    """
    amount = float(amount)
    if tran_type in settings.TRANSACTION_TYPE:
        interest = amount * settings.TRANSACTION_TYPE[tran_type]['interest']
        old_balance = account_data['balance']
        if settings.TRANSACTION_TYPE[tran_type]['action'] == "plus":
            new_balance = old_balance + amount + interest
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == "minus":
            new_balance = old_balance - amount - interest
            if new_balance < 0:
                print("Your credit [%s] is not enough for this transaction [-%s], current balance is [%s]" % (
                    account_data['credit'], (amount + interest), old_balance))
                return
        account_data['balance'] = new_balance
        accounts.dump_account(account_data)
        log_obj.info("account:%s action:%s amount:%s interest:%s" % (account_data['id'], tran_type, amount, interest))
        return account_data
    else:
        print("Transaction type [%s] is not exists" % tran_type)
