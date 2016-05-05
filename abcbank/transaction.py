from datetime import datetime


class Transaction:

    def __init__(self, amount):
        self.amount = amount
        self.transactionDate = datetime.now()
        self.withdraw = True if amount < 0 else False

    @property
    def age(self):
        return (datetime.now() - self.transactionDate).days
