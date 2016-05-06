from tests import bank_tests, customer_tests, transaction_tests


def run():
    print 'Running bank tests...'
    b_tests = [getattr(bank_tests, obj) for obj in dir(bank_tests)
               if 'test_' in obj]
    for func in b_tests:
        func()
    print 'Running customer tests...'
    c_tests = [getattr(customer_tests, obj) for obj in dir(customer_tests)
               if 'test_' in obj]
    for func in c_tests:
        func()
    print 'Running transactions tests...'
    t_tests = [getattr(transaction_tests, obj)
               for obj in dir(transaction_tests) if 'test_' in obj]
    for func in t_tests:
        func()
    print 'Done'

if __name__ == '__main__':
    run()
