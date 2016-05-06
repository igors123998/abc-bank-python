from datetime import datetime


class Transaction:

    def __init__(self, amount, transaction_time=None):
        self.amount = amount
        self.transactionDate = datetime.now() if transaction_time is None\
                               else transaction_time
        self.withdraw = True if amount < 0 else False

    @property
    def age(self):
        return (datetime.now() - self.transactionDate).days
