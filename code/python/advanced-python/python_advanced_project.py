# Banking App
# x Class Based
# x Withdrawal Deposit
# x Write transactions to file
# While true:
# input
# x classes
# x open()
# x method
# x properties

from json.decoder import JSONDecodeError
import sys
import random
import json

def round_cent(amount):
    round_amount = "{:.2f}".format(amount)
    return round_amount

class Account:
    # dictionary to hold account numbers : names
    bank = {}

    # initialize account
    def __init__(self, acct_num, name):
        self.acct_num = acct_num
        self.name = name
        self.acct_file = str(acct_num) + '.txt'
        Account.get_accounts()
        self.update_balance()

    # create account
    def open_account(self):
        # add acct#/name to bank dictionary
        Account.bank[self.acct_num] = self.name
        self.transcribe_account()

        # initialize account balance
        self.balance = 20.00
        # write new account to file
        self.transcribe_transaction("account created", round_cent(self.balance))

        # print details to user
        print(f"""Welcome, {self.name}!
Your account number is #{self.acct_num}
Please record this number!!!
A complimentary $20.00 has been deposited into your account.
Thank you for banking with us.""")
        self.check_balance()


    # generate unique account number
    def gen_acct_num():
        acct_num = random.randint(1000, 9999)
        # update account dictionary
        Account.get_accounts()
        # recursively call method in case acct_num already exists
        if acct_num in Account.bank:
            return Account.gen_acct_num()
        return acct_num

    # get current balance
    def update_balance(self):
        try:
            with open(self.acct_file, 'r') as file:
                last_line = file.readlines()[-1]
                i = last_line.index('$') + 1
                self.balance = float(last_line[i:])
        except Exception:
            self.balance = 0.00
            return

    # print balance
    def check_balance(self):
        print(f"Acct #{self.acct_num} balance: ${round_cent(self.balance)}\n")

    # debit balance
    def withdrawal(self):
        debit = input("Enter withdrawal amount: ")
        print("\n")
        #check for valid debit number/type
        try:
            debit = float(debit)
            debit >= 0
        except ValueError:
            print("Invalid amount")
            return

        # debit account
        self.balance -= debit
        cent_debit = round_cent(debit)
        print(f"Withrawal ${cent_debit}")

        # print balance to user
        self.check_balance()

        # write transaction to file
        tran_debit = "-" + cent_debit
        self.transcribe_transaction("debit", tran_debit)

    # credit balance
    def deposit(self):
        credit = input("Enter deposit amount: ")
        print("\n")

        # check for valid credit number/type
        try:
            credit = float(credit)
            credit >= 0
        except ValueError:
            print("Invalid amount")
            return

        #credit account
        self.balance += credit
        cent_credit = round_cent(credit)
        print(f"Deposit ${cent_credit}")

        # print balance to user
        self.check_balance()

        # write transaction to file
        self.transcribe_transaction("credit", cent_credit)

    # record transaction to file
    def transcribe_transaction(self, type, amount):
        with open(self.acct_file, 'a') as file:
            file.write(f"{type} : ${amount}\n")
            file.write(f"balance : ${round_cent(self.balance)}\n")

    # record account to dictionary of accounts
    def transcribe_account(self):
        with open("bank.txt", 'w+') as file:
            try:
                Account.bank = json.load(file)
            except JSONDecodeError:
                json.dumps({})
            file.seek(0)
            json.dump(Account.bank, file, indent = 4)

    def get_accounts():
        try:
            with open("bank.txt", 'r') as file:
                Account.bank = json.load(file)
        except Exception:
            Account.bank = {}

    # check that account exists
    def is_account(acct_num):
        Account.get_accounts()

        if Account.bank[acct_num]:
            return True
        else:
            return False

# prompt for account number or start new account
def main_menu():
    acct_selection = None
    # Select main page option
    while acct_selection != 'X':
        try:
            acct_selection = input("""Enter selection:
  [A]ccess existing account
  [O]pen new account
  [C]lose account
  [H]elp
  e[X]it
  """)[0].upper()
            print("")
        # Check for valid main page input
        except:
            print("invalid selection\n")
            continue
        # Exit program
        if acct_selection == 'X':
            print("Exiting...")
            sys.exit()
        # Access existing account
        elif acct_selection == 'A':
            acct_num = input("Enter account number: ")
            try:
                len(acct_num) == 4
                int(acct_num)
            except Exception:
                print ("Invalid account number")
                continue
            if Account.is_account(acct_num):
                acct = Account(acct_num, Account.bank[acct_num])
            else:
                print("Invalid account number")
                continue
            print(f"\nWelcome, {acct.name}!")
            return acct
        # Open account
        elif acct_selection == 'O':
            try:
                surname = input("Enter surname: ")
                first_initial = input("Enter first initial: ")[0].upper()
                str(surname)
                str(first_initial)
            except Exception:
                print("Invalid name\n")
                continue
            print("")
            name = first_initial + '. ' + surname
            acct_num = Account.gen_acct_num()
            acct = Account(acct_num, name)
            acct.open_account()
            return acct
        # Close account or Request help
        elif acct_selection == 'C' or acct_selection == 'H':
            print("Please speak with a customer service representative")
            # :P
        # Valid string, but not an option
        else:
            print("Invalid selection\n")

# Account page selection
while True:
    acct = main_menu()
    selection = None
    while selection != 'R':
        try:
            selection = input("""Enter selection:
  [W]ithdrawal
  [D]eposit
  [B]alance
  [R]eturn
  e[X]it
  """)[0].upper()
            print("")
        except:
            print("Invalid selection\n")
            continue

        if selection == 'X':
            print("Exiting...")
            sys.exit()
        elif selection == 'R':
            break
        elif selection == 'B':
            acct.check_balance()
        elif selection == "W":
            acct.withdrawal()
        elif selection == 'D':
            acct.deposit()
        else:
            print("Invalid selection\n")
