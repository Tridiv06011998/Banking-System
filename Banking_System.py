import  pymysql
from random import *
from string import *

class user:
    mydb=pymysql.connect(
        host='localhost',
        user='root',
        passwd='Tridiv1998',
        database='bank_acc'
    )
    mycursor=mydb.cursor()

    acc_no=0
    balance=0
    passcode=''
    def create_user(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance
        self.passcode=self.pass_gen()
        sql="INSERT INTO users(acc_no,balance,password) VALUES(%s,%s,%s)"
        val=(self.acc_no,self.balance,self.passcode)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        print("Account created successfully")
        print("Your password is:",self.passcode)

    def withdrawal(self,acc_no,passcode,amt):
        self.acc_no=acc_no
        self.passcode=passcode
        sql="UPDATE users SET balance=balance-%s WHERE acc_no=%s AND password=%s AND balance>=%s"
        val=(amt,self.acc_no,self.passcode,amt)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        print("Account updated successfully....to view your account details press 3")

    def isallowed(self,acc_no,passcode,amt):
        sql="SELECT * FROM users WHERE acc_no=%s AND password=%s"
        val=(acc_no,passcode)
        self.mycursor.execute(sql,val)
        myresult=self.mycursor.fetchall()
        if myresult[0][1]>=amt:
            return  1
        else:
            return  0

    def deposit(self,acc_no,password,amt):
        self.acc_no=acc_no
        self.passcode=password
        sql="UPDATE users SET balance=balance+%s WHERE acc_no=%s AND password=%s"
        val=(amt,self.acc_no,self.passcode)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        print("Account updated successfully.....to view your current status press 3")


    def check_balance(self,acc_no,passcode):
        self.acc_no=acc_no
        self.passcode=passcode
        sql="SELECT * FROM users WHERE acc_no=%s AND password=%s"
        val=(self.acc_no,self.passcode)
        self.mycursor.execute(sql,val)
        myresult=self.mycursor.fetchall()
        print("Your current account balance is:",myresult[0][1])

    def pass_gen(self):
        letters=ascii_letters+digits
        string_length=2
        password=''
        for i in range(string_length):
            password+=choice(letters)
        return password

    def acc_not_found(self,acc_no,passcode):
        sql="SELECT * FROM users"
        self.mycursor.execute(sql)
        myresult=self.mycursor.fetchall()
        for i in range(len(myresult)):
            if myresult[i][0]==acc_no and myresult[i][2]==passcode:
                return 1
        return 0

    def setPassword(self,acc_no,old_pass,new_pass):
        sql="UPDATE users SET password=%s WHERE acc_no=%s AND password=%s"
        val=(new_pass,acc_no,old_pass)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        print("You have successfully changed your password")
        print("Your new password is:",new_pass)

#******* __main__ ***********
if __name__=='__main__':
    f=1
    while f==1:
        print("1.create user\n2.Already an user\n3.exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            ac_no=int(input("Enter your account no:"))
            balance=float(input("Enter your starting balance:"))
            obj=user()
            obj.create_user(ac_no,balance)
        elif ch==2:
            ac_no=int(input("Enter your account no:"))
            password=input("Enter your password:")
            obj=user()
            if obj.acc_not_found(ac_no,password)==0:
                print("Sorry....no account found")
                continue
            k=1
            while k==1:
                print("1.withdrawal\n2.deposit\n3.check_balance\n4.change password\n5.exit")
                c=int(input("Enter your choice:"))
                if c==1:
                    amt=float(input("Enter the amount you want to withdrawal:"))
                    obj=user()
                    if obj.isallowed(ac_no,password,amt)==0:
                        print("Not allowed")
                        continue
                    obj.withdrawal(ac_no,password,amt)
                elif c==2:
                    amt = float(input("Enter the amount you want to deposit:"))
                    obj = user()
                    obj.deposit(ac_no, password, amt)
                elif c==3:
                    obj=user()
                    obj.check_balance(ac_no,password)
                elif c==4:
                    new_pass=input("Enter your new password:")
                    obj=user()
                    obj.setPassword(ac_no,password,new_pass)
                    password=new_pass
                    #print("You have to login with your new password to access your account")
                    #break
                elif c==5:
                    print("Thank you....")
                    k=0
        elif ch==3:
            print("Thank you....visit again")
            f=0