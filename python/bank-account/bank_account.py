class BankAccount(object):
    # class variables
    total_amount = 0
    available = None

    def __init__(self):
        pass

    def get_balance(self):
        """Return the amount of money on bankacount if account is open"""
        if self.available:
            return self.total_amount
        else:
            raise ValueError('This bank account is closed')

    def open(self):
        """Opens the account by setting the available to true"""
        self.available = True

    def deposit(self, amount):
        """
        Deposit a amount of money on an account.
        Returns the amount of money on the account
        """
        if self.available:
            self.total_amount += amount
            return self.total_amount
        else:
            raise ValueError('This bank account is closed')

    def withdraw(self, amount):
        """
        Withdraws an amount of money from the account.
        Checks if there is enough money on the account
        then returns the amount of money still left on the account
        """
        if self.available:
            if (self.total_amount - amount) > 0:
                self.total_amount -= amount
                return "Your total amount is now ", self.total_amount
            else:
                raise ValueError("You don't have enough money on your account")
        else:
            return 'Bank is closed'

    def close(self):
        """Closes the account by setting available to false"""
        self.available = False

