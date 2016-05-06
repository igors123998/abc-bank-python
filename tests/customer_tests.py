from nose.tools import assert_equals, assert_almost_equals
from datetime import datetime

from abcbank.account import Account, CHECKING, SAVINGS, MAXI_SAVINGS
from abcbank.customer import Customer


def test_statement():
    checkingAccount = Account(CHECKING)
    savingsAccount = Account(SAVINGS)
    henry = Customer("Henry").openAccount(checkingAccount).\
        openAccount(savingsAccount)
    checkingAccount.deposit(100.0)
    savingsAccount.deposit(4000.0)
    savingsAccount.withdraw(200.0)
    assert_equals(henry.getStatement(),
                  "Statement for Henry" +
                  "\n\nChecking Account\n  deposit $100.00\nTotal $100.00" +
                  "\n\nSavings Account\n  deposit $4000.00\n  "
                  "withdrawal $200.00\nTotal $3800.00" +
                  "\n\nTotal In All Accounts $3900.00")


def test_oneAccount():
    oscar = Customer("Oscar").openAccount(Account(SAVINGS))
    assert_equals(oscar.numAccs(), 1)


def test_twoAccounts():
    oscar = Customer("Oscar").openAccount(Account(SAVINGS))
    oscar.openAccount(Account(CHECKING))
    assert_equals(oscar.numAccs(), 2)


def test_threeAccounts():
    oscar = Customer("Oscar").openAccount(Account(SAVINGS))
    oscar.openAccount(Account(CHECKING))
    oscar.openAccount(Account(MAXI_SAVINGS))
    assert_equals(oscar.numAccs(), 3)


def test_withdrawals():
    checkingAccount = Account(CHECKING)
    oscar = Customer("Oscar").openAccount(checkingAccount)
    checkingAccount.deposit(1000.0, datetime(2016, 4, 12))
    checkingAccount.deposit(1000.0, datetime(2016, 4, 15))
    checkingAccount.deposit(1000.0, datetime(2016, 4, 17))
    assert_almost_equals(oscar.totalInterestEarned(), 0.17, places=2)
    checkingAccount.withdraw(1000.0, datetime(2016, 4, 19))
    assert_almost_equals(oscar.totalInterestEarned(), 0.12, places=2)


def test_transferAmountBelowZero():
    checkingAccount = Account(CHECKING)
    savingsAccount = Account(SAVINGS)
    oscar = Customer("Oscar").openAccount(checkingAccount)
    oscar.openAccount(savingsAccount)
    try:
        oscar.transfer(checkingAccount, savingsAccount, -1)
    except ValueError as e:
        result = str(e)
    assert_equals(result, 'Incorrect amount, should be more than 0')


def test_transferNotEnoughFunds():
    checkingAccount = Account(CHECKING)
    savingsAccount = Account(SAVINGS)
    oscar = Customer("Oscar").openAccount(checkingAccount)
    oscar.openAccount(savingsAccount)
    try:
        oscar.transfer(savingsAccount, savingsAccount, 10)
    except ValueError as e:
        result = str(e)
    assert_equals(result, 'Incorrect amount, should be more than '
                          'source account amount')


def test_transferAmount():
    checkingAccount = Account(CHECKING)
    savingsAccount = Account(SAVINGS)
    oscar = Customer("Oscar").openAccount(checkingAccount)
    oscar.openAccount(savingsAccount)
    checkingAccount.deposit(100.0)
    transfered = oscar.transfer(checkingAccount, savingsAccount, 10)
    assert_equals(transfered, True)
    assert_equals(savingsAccount.amount, 10.)
