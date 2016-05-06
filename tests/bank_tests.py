from nose.tools import assert_equals, assert_almost_equals
import datetime

from abcbank.account import Account, CHECKING, MAXI_SAVINGS, SAVINGS
from abcbank.bank import Bank
from abcbank.customer import Customer


def test_customer_summary():
    bank = Bank()
    john = Customer("John").openAccount(Account(CHECKING))
    bank.addCustomer(john)
    assert_equals(bank.customerSummary(),
                  "Customer Summary\n - John (1 account)")


def test_checking_account():
    bank = Bank()
    checkingAccount = Account(CHECKING)
    bill = Customer("Bill").openAccount(checkingAccount)
    bank.addCustomer(bill)
    year_behind = datetime.datetime.now() - datetime.timedelta(365)
    checkingAccount.deposit(100.0, year_behind)
    assert_equals(bank.totalInterestPaid(), 0.1)


def test_savings_account():
    bank = Bank()
    checkingAccount = Account(SAVINGS)
    bank.addCustomer(Customer("Bill").openAccount(checkingAccount))
    year_behind = datetime.datetime.now() - datetime.timedelta(365)
    checkingAccount.deposit(1500.0, year_behind)
    assert_equals(bank.totalInterestPaid(), 2.0)


def test_maxi_savings_account():
    bank = Bank()
    checkingAccount = Account(MAXI_SAVINGS)
    bank.addCustomer(Customer("Bill").openAccount(checkingAccount))
    year_behind = datetime.datetime.now() - datetime.timedelta(365)
    checkingAccount.deposit(3000.0, year_behind)
    assert_equals(bank.totalInterestPaid(), 150.0)


def test_maxi_savings_account_without_withdrawals():
    bank = Bank()
    checkingAccount = Account(MAXI_SAVINGS)
    bank.addCustomer(Customer("Bill").openAccount(checkingAccount))
    year_behind = datetime.datetime.now() - datetime.timedelta(365)
    eleven_days_behind = datetime.datetime.now() - datetime.timedelta(11)
    checkingAccount.deposit(3000.0, year_behind)
    checkingAccount.withdraw(1000.0, eleven_days_behind)
    assert_almost_equals(bank.totalInterestPaid(), 148.49, places=2)


def test_maxi_savings_account_with_withdrawals():
    bank = Bank()
    checkingAccount = Account(MAXI_SAVINGS)
    bank.addCustomer(Customer("Bill").openAccount(checkingAccount))
    year_behind = datetime.datetime.now() - datetime.timedelta(365)
    five_days_behind = datetime.datetime.now() - datetime.timedelta(5)
    checkingAccount.deposit(3000.0, year_behind)
    checkingAccount.withdraw(1000.0, five_days_behind)
    assert_almost_equals(bank.totalInterestPaid(), 147.97, places=2)
