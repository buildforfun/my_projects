class BankAccount():
    """ This is the parent class"""
    # Abstraction - this class hides complex operations that are generic to all BankAccounts
    def __init__(self, account_number, balance=0):
        # OOP Encapsulation - single underscore means it's protected - not accessible outside the class.
        # self._ means it's private. They can be accessed publicly using functions e.g withdraw.
        self._account_number = account_number
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    def withdraw(self, amount):
        if 0 <= amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

class CheckingAccount(BankAccount):
    """This is a child class"""
    # OOP Inheritance - This class inherits from BankAccount
    def __init__(self, account_number, balance, overdraft_limit=100):
        # runs __init__ object of parent class
        super().__init__(account_number, balance)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """OOP Polymorphism - this func has the same name as withdraw func in
        BankAccount but has overwriten the function. """
        if 0 <= amount <= (self._balance + self._overdraft_limit):
            self._balance -= amount
            return True
        return False

class SavingAccount(BankAccount):
    """This is a child class"""
    def __init__(self, account_number, balance):
        # call the parent class's constructor
        super().__init__(account_number, balance)
        interest_rate = 1
        self.interest_rate = interest_rate
    
    def add_interest(self):
        #TODO add interest rate to account
        # will be polymorphism as it is adding a function to an inherited class
        pass


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_type, account_number, initial_balance = 0):
        if account_type == "checking":
            account = CheckingAccount(account_number, initial_balance)
        elif account_type == "savings":
            account = SavingAccount(account_number, initial_balance)
        else:
            return False

        # adds to dict of existing accounts
        self.accounts[account_number] = account

        return True

    def deposit(self, account_number, amount):
        # retreives account object using account number
        account  = self.accounts.get(account_number)
        if account:
            return account.deposit(amount)
    
    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            return account.withdraw(amount)
    
    def get_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.balance


if __name__ == "__main__":

    # creates a bank object
    bank = Bank()

    bank.create_account("checking", "12345", 999)
    bank.create_account("savings", "4567", 100)

    bank.deposit("12345", 500)
    bank.withdraw("12345", 250)
    print(bank.get_balance("12345"))