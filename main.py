from banking import *

# Initialize new bank
bank = Bank()

# Read from accounts.csv
bank.load_from_csv("accounts.csv")

# Create new account for Charlie
bank.create_account("Charlie", 5000)

# Deposit 2000 to Charlie's account
bank.deposit("Charlie", 2000)

# Charlie withdraw 1000 from his account
bank.withdraw("Charlie", 1000)

# Charlie transfer 1000 to Ming's account
bank.transfer("Charlie", "Ming", 1000)

# Update the account.csv
bank.save_to_csv("accounts.csv")

