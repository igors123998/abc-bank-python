from abcbank.transaction import Transaction
from datetime import datetime

CHECKING = 0
SAVINGS = 1
MAXI_SAVINGS = 2


class Account:

    def __init__(self, accountType):
        self.accountType = accountType
        self.transactions = []
        self.amount = 0.

    def deposit(self, amount, t=None):
        t = datetime.now() if t is None else t
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(amount, t))
            self.amount += amount

    def withdraw(self, amount, t=None):
        t = datetime.now() if t is None else t
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(-amount, t))
            self.amount -= amount

    def interestEarned(self):
        if len(self.transactions) == 0:
            return 0.
        if len(self.transactions) == 1 and not self.transactions[0].withdraw:
            t = self.transactions[0]
            return self.interest(t.amount, t.age)
        interest = 0.
        last_amount = 0.
        sorted_transactions = sorted(self.transactions,
                                     key = lambda x: x.transactionDate)
        for i, t in enumerate(sorted_transactions):
            last_amount += t.amount
            if i == 0:
                continue
            wd = self.withdrawalsInLastNDays(sorted_transactions[:i+1])
            days_since_last_transaction = sorted_transactions[i-1].age - t.age
            interest += self.interest(last_amount - t.amount,
                                      days_since_last_transaction, wd)
        wd = self.withdrawalsInLastNDays(sorted_transactions, current=True)
        interest += self.interest(last_amount, t.age, wd)
        return interest
        
    def interest(self, amount, days, withdrawals=False):
        if self.accountType == SAVINGS:
            if (amount <= 1000):
                result = amount * 0.001
            else:
                result = 1 + (amount - 1000) * 0.002
        elif self.accountType == MAXI_SAVINGS:
            if withdrawals:
                result = amount * 0.001
            else:
                result = amount * 0.05
        else:
            result = amount * 0.001
        return result * float(days)/365

    def withdrawalsInLastNDays(self, transactions, N=10, current=False):
        last = 0 if current else transactions[-1].age
        for i, t in enumerate(reversed(transactions)):
            if not current and i == 0:
                continue
            if t.age - last > N:
                return False
            elif t.withdraw:
                return True
        return False

    def sumTransactions(self, checkAllTransactions=True):
        return sum([t.amount for t in self.transactions])
