from random import *
from string import *

class user:
    acc_no=0
    balance=0

    def __init__(self,acc_no,balance):
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
    obj=[]
    passwords=[]
    f=1
    print("_______BANKING-SYSTEM_______");
    while f==1:
        print("\n1.Create account\n2.Already have an account\n3.Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            acc_no=int(input("Enter your account no: "))
            balance=int(input("Enter your balance: "))
            objj=user(acc_no,balance)
            obj.append(objj)
            print("Account created successfully")
            passcode=objj.pass_gen()
            print("Your password is:", passcode)
            print("Don't forget this password. If you forget this you will lose control of your account.")
            passwords.append(passcode)

        elif ch==2:
            t=0
            ac_no = int(input("Enter your account no: "))
            pass_input=(input("Enter your password: "))
            pass
            for i in range(len(obj)):
                if obj[i].acc_no==ac_no and passwords[i]==pass_input:
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
                    if obj[ac].isAllowed(amtt)==1:
                        print("Sorry, not allowed!!")
                        continue
                    obj[ac].withdrawal(amtt)
                    obj[ac].check_balance()
                    break

                elif c==2:
                    amtt=int(input("Enter the amount you want to deposit: "))
                    obj[ac].deposit(amtt)
                    obj[ac].check_balance()
                    break

                elif c==3:
                    obj[ac].check_balance()
                    break

                elif c==4:
                    pass_new=input("Enter your new password: ")
                    pass_con=input("Confirm your password: ")
                    if pass_new==pass_con:
                        passwords[ac]=pass_new;
                    else:
                        print("Failed!!")
                        break
                    print("Your password is changed successfully\nYour new password is:", passwords[ac])
                    break

                elif c==5:
                    print("Wrong choice!!")
                    break

        elif ch==3:
            print("Thank you....visit again....")
            f=0