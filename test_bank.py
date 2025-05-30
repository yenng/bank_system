from banking import *
import unittest

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.bank.accounts = {"Jack": Account("Jack", 10000.0),
                              "Rose": Account("Rose", 8888.0),
                              "Tim": Account("Tim", 168888.0),
                              "Ming": Account("Ming", 3000.0)}
        self.acc_yen = Account("Ng Yen Aeng", 300.0)
    
    # Test Accout.deposit
    def test_account_deposit(self):
        self.acc_yen.deposit(1000.0)

        self.assertEqual(self.acc_yen.balance, 1300.0)

    # Test Accout.deposit error with negative amount
    def test_account_deposit_err(self):
        with self.assertRaises(ValueError) as err:
            self.acc_yen.deposit(-1000.0)

        self.assertIn("Deposit amount must be positive", str(err.exception))

    # Test Accout.withdraw
    def test_account_withdraw(self):
        self.acc_yen.withdraw(250.0)
        self.assertEqual(self.acc_yen.balance, 50.0)

    # Test Accout.withdraw error with negative amount
    def test_account_withdraw_err(self):
        with self.assertRaises(ValueError) as err:
            self.acc_yen.withdraw(-1000.0)

        self.assertIn("Withdraw amount must be positive", str(err.exception))

    # Test Accout.withdraw error with not enough balance
    def test_account_withdraw_balance_not_enough(self):
        with self.assertRaises(ValueError) as err:
            self.acc_yen.withdraw(1000.0)

        self.assertIn("Balance not enough.", str(err.exception))

    # Test Bank.create_account
    def test_bank_create_account(self):
        self.bank.create_account("Ng Yen Aeng", 300.0)

        self.assertEqual(self.bank.accounts["Ng Yen Aeng"].name, "Ng Yen Aeng")
        self.assertEqual(self.bank.accounts["Ng Yen Aeng"].balance, 300.0)

    # Test Bank.create_account duplicated
    def test_bank_create_duplicate_account(self):
        self.bank.create_account("Ng Yen Aeng", 300.0)
        with self.assertRaises(ValueError) as err:
            self.bank.create_account("Ng Yen Aeng", 300.0)
        
        self.assertIn("Account was created.", str(err.exception))

    # Test Bank.deposit
    def test_bank_deposit(self):
        self.bank.deposit("Ming", 520.0)

        self.assertEqual(self.bank.accounts["Ming"].balance, 3520.0)

    # Test Bank.deposit with account not found.
    def test_bank_deposit_err(self):
        with self.assertRaises(ValueError) as err:
            self.bank.deposit("Ng Yen Aeng", 520.0)
        
        self.assertIn("Account not created.", str(err.exception))

    # Test Bank.withdraw
    def test_bank_withdraw(self):
        self.bank.withdraw("Tim", 68888.0)

        self.assertEqual(self.bank.accounts["Tim"].balance, 100000.0)

    # Test Bank.transfer
    def test_bank_transfer(self):
        self.bank.transfer("Jack", "Rose", 1112.0)

        self.assertEqual(self.bank.accounts["Jack"].balance, 8888.0)
        self.assertEqual(self.bank.accounts["Rose"].balance, 10000.0)

    # Test csv reader and loader.
    def test_csv(self):
        self.bank.save_to_csv("accounts.csv")
        new_bank = Bank()

        new_bank.load_from_csv("accounts.csv")
        self.assertCountEqual(self.bank.accounts.keys(), new_bank.accounts.keys())
        self.assertEqual(self.bank.accounts["Jack"].balance, new_bank.accounts["Jack"].balance)

if __name__ == '__main__':
    unittest.main()