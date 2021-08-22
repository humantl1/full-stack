# Banking App
# Class Based
# Withdrawal Deposit
# Write transactions to file
# While true:
# input
# classes
# open()
# method
# properties

def round_cent(amount):
    round_amount = "{:.2f}".format(amount)
    return round_amount

class Account:
    def __init__(self, acct_num):
        # check for valid account number
        self.acct_num = acct_num
        self.balance = 20.0
        print(f"Acct# {self.acct_num} initialized")
        self.check_balance()

    # print balance
    def check_balance(self):
        print(f"Acct #{self.acct_num} balance: {round_cent(self.balance)}")

    # debit balance
    def withdrawal(self, debit):
        #check for valid debit number/type
        self.balance -= debit
        cent_debit = round_cent(debit)
        print(f"Withrawel ${cent_debit}")
        self.check_balance()
        tran_debit = "-" + cent_debit
        self.transcribe("debit", tran_debit)

    # credit balance
    def deposit(self, credit):
        # check for valid credity number/type
        self.balance += credit
        cent_credit = round_cent(credit)
        print(f"Withrawel ${cent_credit}")
        self.check_balance()
        self.transcribe("credit", cent_credit)

    # record transaction to file
    def transcribe(self, type, amount):
        acct_file = str(self.acct_num) + ".txt"
        with open(acct_file, 'a') as file:
            file.write(f"{type} : ${amount}\n")
            file.write(f"balance : {round_cent(self.balance)}\n\n")

    # check that account exists
    def find_account(self):
        pass

# prompt for account number or start new account
#initialize balance if starting with new account
a = Account(13456)
a.deposit(30.01)
a.withdrawal(5.03)