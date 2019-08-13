from random import *
from string import *

class user:
    name=''
    acc_no=0
    balance=0

    def __init__(self,name, acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance

    def withdrawal(self,amt):
        self.balance-=amt
        return self.balance

    def deposit(self,amt):
        self.balance+=amt
        return self.balance

    def check_balance(self):
        print("\nCurrent status of your account is:")
        print("User's name: ", self.name)
        print("Account No:", self.acc_no)
        print("Balance:", self.balance)
        print();

    def isAllowed(self,amt):
        if self.balance<amt:
            return 1
        else:
            return 0

    def pass_gen(self):
        letters=ascii_letters+digits
        string_length=2
        password=''
        for i in range(string_length):
            password+=choice(letters)
        return password

if __name__== "__main__":
    def isValid(acc_no):
        for i in obj:
            if i.acc_no==acc_no:
                return 0
        return 1
    obj={}
    f=1
    print("_______BANKING-SYSTEM_______");
    while f==1:
        print("\n1.Create account\n2.Already have an account\n3.Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            name=input("Enter your name: ")
            acc_no=int(input("Enter your account no: "))
            if isValid(acc_no)==0:
                print("Sorry, this account number already has been used")
                continue
            else:
                balance=int(input("Enter your balance: "))
                objj=user(name, acc_no, balance)
                passcode=objj.pass_gen()
                obj[objj]=passcode
                print("Account created successfully")
                print("Your password is:", passcode)
                print("Don't forget this password. If you forget this you will lose control of your account.")

        elif ch==2:
            t=0
            acc_no = int(input("Enter your account no: "))
            pass_input=(input("Enter your password: "))
            pass
            for i in obj:
                if i.acc_no==acc_no and obj[i]==pass_input:
                    ac=i
                    t=1
                    break
            if t==0:
                print("Sorry, no account found!!")
                continue
            k=1
            while k==1:
                print("\n1.Withdrawal\n2.Deposit\n3.Check balance\n4.Change password\n5.Exit")
                c=int(input("Enter your choice:"))
                if c==1:
                    amtt=int(input("Enter the amount you want to withdrawn: "))
                    if ac.isAllowed(amtt)==1:
                        print("Sorry, not allowed!!")
                        continue
                    ac.withdrawal(amtt)
                    ac.check_balance()
                    break

                elif c==2:
                    amtt=int(input("Enter the amount you want to deposit: "))
                    ac.deposit(amtt)
                    ac.check_balance()
                    break

                elif c==3:
                    ac.check_balance()
                    break

                elif c==4:
                    pass_new=input("Enter your new password: ")
                    pass_con=input("Confirm your password: ")
                    if pass_new==pass_con:
                        obj[ac]=pass_new;
                    else:
                        print("Failed!!")
                        break
                    print("Your password has been changed successfully\nYour new password is:", obj[ac])
                    break

                elif c==5:
                    print("Wrong choice!!")
                    break

        elif ch==3:
            print("Thank you....visit again....")
            f=0