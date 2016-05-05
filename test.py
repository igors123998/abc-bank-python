from tests import bank_tests, customer_tests, transaction_tests


def run():
    print 'Running bank tests...'
    bank_tests.test_customer_summary()
    bank_tests.test_checking_account()
    bank_tests.test_savings_account()
    bank_tests.test_maxi_savings_account()
    bank_tests.test_maxi_savings_account_with_withdrawals()
    print 'Running customer tests...'
    customer_tests.test_statement()
    customer_tests.test_oneAccount()
    customer_tests.test_twoAccounts()
    customer_tests.test_threeAccounts()
    customer_tests.test_transferAmountBelowZero()
    customer_tests.test_transferNotEnoughFunds()
    customer_tests.test_transferAmount()
    print 'Running transactions tests...'
    transaction_tests.test_type()
    transaction_tests.test_withdraw()
    print 'Done'

if __name__ == '__main__':
    run()
