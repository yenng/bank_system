import csv

class Account:
    def __init__(self, name: str, balance: float=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount


    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Balance not enough.")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
  
        self.balance -= amount
        

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name: str, balance: float=0.0):
        if name in self.accounts:
            raise ValueError("Account was created.")

        self.accounts[name] = Account(name,balance)

    def deposit(self, name: str, amount: float):
        self._get_account_by_name(name).deposit(amount)

    def withdraw(self, name: str, amount: float):
        self._get_account_by_name(name).withdraw(amount)

    def transfer(self, from_name: str, to_name: str, amount: float):
        from_acc = self._get_account_by_name(from_name)
        to_acc = self._get_account_by_name(to_name)
        from_acc.withdraw(amount)
        to_acc.deposit(amount)

    def _get_account_by_name(self, name: str):
        if name not in self.accounts:
            raise ValueError("Account not created.")
        
        return self.accounts[name]

    def save_to_csv(self, file_name: str):
        with open(file_name, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'balance'])
            for name, acc in self.accounts.items():
                writer.writerow([name, acc.balance])

    def load_from_csv(self, file_name: str):
        self.accounts = {}
        try:
            with open(file_name, mode='r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.create_account(row['name'], float(row['balance']))
        except FileNotFoundError:
            pass
