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
    def diposit(self,amt):
        self.balance+=amt
        return self.balance
    def check_balance(self):
        print("The status of your acc is:")
        print(self.acc_no)
        print(self.balance)
    def isAllowed(self,amt):
        if self.balance<amt:
            return 1
        else:
            return 0
    def pass_gen(self):
        letters=ascii_letters
        string_length=2
        password=''
        for i in range(string_length):
            password+=choice(letters)
        return password
obj=[]
passwords=[]
f=1
while f==1:
    print("1.new user\n2.existing user\n3.exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        acc_no=int(input("Enter your acc no:"))
        balance=int(input("Enter your balance:"))
        objj=user(acc_no,balance)
        obj.append(objj)
        print("Account created successfully")
        passcode=objj.pass_gen()
        print("Your password is:",passcode)
        passwords.append(passcode)

    elif ch==2:
        t=0
        ac_no = int(input("Enter your acc no:"))
        pass_input=(input("Enter your passcode:"))
        pass
        for i in range(len(obj)):
            if obj[i].acc_no==ac_no and passwords[i]==pass_input:
                ac=i
                t=1
                break
        if t==0:


            print("Sorry, no acc found")
            continue
        k=1
        while k==1:
            print("1.withdrawal\n2.deposit\n3.check balance\n4.exit")
            c=int(input("Enter your choice:"))
            if c==1:
                amtt=int(input("Enter the amount you want to withdrawn"))
                if obj[ac].isAllowed(amtt)==1:
                    print("Sorry not allowed")
                    continue
                obj[ac].withdrawal(amtt)
                obj[ac].check_balance()
                break
            elif c==2:
                amtt=int(input("Enter th amount you want to diposit:"))
                obj[ac].diposit(amtt)
                obj[ac].check_balance()
                break
            elif c==3:
                obj[ac].check_balance()
                break
            elif c==4:
                print("Wrong choice")
                break
    elif ch==3:
        f=0