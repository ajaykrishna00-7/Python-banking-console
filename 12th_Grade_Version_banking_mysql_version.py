# IMPORTING ALL THE REQUIRED LIBRARIES :
import mysql.connector
import csv
import random
import os
#--------------------------------------------------------------------------------
#ESTABLISHING CONNECTION :
conn=mysql.connector.connect(host="localhost",user="root",passwd="yourpassword") #Enter your mysql password
cur=conn.cursor()
#---------------------------------------------------------------------------------
#CREATING DATABASE ABD TABLE :
cur.execute("CREATE DATABASE IF NOT EXISTS BANKSYSTEM")
cur.execute("USE BANKSYSTEM")
lacc=[]
lpin=["000"]#000 is bank's pin
cur.execute("CREATE TABLE IF NOT EXISTS CURR_ACC(ACCNO INT(11) PRIMARY KEY,ACCNAME VARCHAR(30)\
,PIN VARCHAR(30),BALANCE FLOAT(20,1),DATE_OF_TRANS DATE)")
cur.execute("CREATE TABLE IF NOT EXISTS TRANS_CURR(SNO INT PRIMARY KEY,ACCNO INT(11),NAME VARCHAR(30),PIN VARCHAR(30) ,TYPE_OF_TRANS VARCHAR(30),OLDBALANCE FLOAT(20,1),CURRBALANCE FLOAT(20,1),\
 DATE_OF_TRANS DATE,REMARKS CHAR(100))")
f=open('sno.txt','w')
sno=f.read()
if(len(sno)==0):
    f.write('0')
f.close()
#-------------------------------------------------
def recordtrans(accno,accname,pin,typ,oldb,curb,date,remarks):
    f=open('sno.txt','r')
    sno=f.read()
    sno=int(sno)
    f.close()
    f=open('sno.txt','w')
    sno+=1
    f.write(str(sno))
    f.close()
    tuple1=(sno,accno,accname,pin,typ,oldb,curb,date,remarks)
    insst="INSERT INTO TRANS_CURR VALUES"+str(tuple1)
    cur.execute(insst)
    conn.commit()
#----------------------------------------------------------------------------------
def checkbankpin():
    p=input("Enter BANK'S pin :")
    if p=="000":
        print("Bank pin verified")
        print("Access granted")
        return True
    else:
        print("INCORRECT PIN")
    
#----------------------------------------------------------------------------------
def accverify():
    accno=int(input("Enter account number :"))
    accheck="SELECT ACCNO FROM CURR_ACC WHERE ACCNO="+str(accno)
    cur.execute(accheck)
    for i in cur:
        for j in i:
            accheck=int(j)
    if(accno==accheck):
        pin=input("Enter pin to verify:")
        pincheck="SELECT PIN FROM CURR_ACC WHERE ACCNO="+str(accno)
        cur.execute(pincheck)
        for i in cur:
            for j in i:
                pincheck=j
        if(pin==pincheck):
            return accno
        else:
            print("Incorrect pin")
            return False
    else:
        f=open("allaccounts.txt","r")
        r=f.read()
        if str(accno) in r.split():
            return accno
        else:
            print("Account doesn't exist")
            return False
#######################
#CREATING A NEW ACCOUNT :
def create():
    global lacc
    global lpin
    acc_name=input("ENTER ACCOUNT HOLDER'S NAME :")
    while True:
        deposit=float(input("ENTER DEPOSIT AMOUNT :"))
        if deposit<0:
            print("Amount invalid !")
            print("Please try again")
        else:
            break
    print("Your account number is :\t",end="")
    while True:
        acc_no=random.randint(100000,1000000)
        if acc_no not in lacc:
            print(acc_no)
            lacc+=[acc_no]
            break  
    f2=open("allaccounts.txt","a+")
    f2.write(str(acc_no))
    f2.write("\n")
    f2.close()
    print("Create your own secret pin : \n ->",end="")
    while True:
        pin=input()
        if pin not in lpin:
            print("pin accepted")
            lpin+=[pin]
            break
        else:
            print("pin already exists")
            print("try a new pin")
            
    datest="SELECT CURDATE()"
    cur.execute(datest)
    for i in cur:
        for j in i:
            date=str(j)
    tuple1=(acc_no,acc_name,pin,deposit,date)
    insst="INSERT INTO CURR_ACC VALUES"+str(tuple1)
    cur.execute(insst)
    conn.commit()
    typ="acc created"
    remarks="Account created"
    recordtrans(acc_no,acc_name,pin,typ,0,deposit,date,remarks)
    print("We need your biodata to set up a record\nPlease enter the following details")
    details=[acc_name,acc_no]
    a1=input("age:")
    a2=input("date of birth:")
    a3=input("annual income:")
    a4=input("phone number:")
    details+=[a1,a2,a3,a4]
    file=open("BANK1.csv","a+",newline="")
    pointer=csv.writer(file,delimiter=",")
    pointer.writerow(details)
    print("Account created successfully")
    file.close()
#-----------------------------------------------------------------------------------------
# DEPOSIT :
def deposit():
    accno=accverify()
    if(accno!=False):
        deposit=float(input("Enter the amount to be depositted:"))
        balancest="SELECT BALANCE,PIN,ACCNAME FROM CURR_ACC WHERE ACCNO="+str(accno)     
        cur.execute(balancest)
        for i in cur:
            balance,pin,accname=i
        
        S='UPDATE CURR_ACC SET BALANCE=BALANCE+'+str(deposit)+'WHERE ACCNO='+str(accno)     
        cur.execute(S)
        remarks=input("REMARKS:")
        print("Amount Depositted successfully")
        conn.commit()
        typ="credit"
        datest="SELECT CURDATE()"
        cur.execute(datest)
        for i in cur:
            for j in i:
                date=str(j)
        recordtrans(accno,accname,pin,typ,balance,balance+deposit,date,remarks)
#######################
def withdraw():
    accno=accverify()
    if(accno!=False):
        withdraw=float(input("Enter the amount to be withdrawm:"))
        balancest="SELECT BALANCE,PIN,ACCNAME FROM CURR_ACC WHERE ACCNO="+str(accno)        
        cur.execute(balancest)
        for i in cur:
            balance,pin,accname=i
        if(balance<withdraw):
            print("Withdrawal not possible")
            print("balance<withdraw")
        else:
            remarks=input("REMARKS:")
            print("Amount withdrawn successfully")
            S='UPDATE CURR_ACC SET BALANCE=BALANCE-'+str(withdraw)+'WHERE ACCNO='+str(accno)     
            cur.execute(S)
            conn.commit()
            typ="withdraw"
            datest="SELECT CURDATE()"
            cur.execute(datest)
            for i in cur:
                for j in i:
                    date=str(j)
            recordtrans(accno,accname,pin,typ,balance,balance-withdraw,date,remarks)
#######################
def transfer():
    datest="SELECT CURDATE()"
    cur.execute(datest)
    for i in cur:
        for j in i:
            date=str(j)
    accno=accverify()
    if(accno!=False):
        newacc=int(input("ENter the recieptent's account number"))
        accheck="SELECT ACCNO FROM CURR_ACC WHERE ACCNO="+str(newacc)
        cur.execute(accheck)
        for i in cur:
            for j in i:
                accheck=int(j)
        
        if newacc==accno :
            while True:
                s=input("Do you want to transfer to your own account ?(Y/N)")
                if s=="Y" or s=="y":
                    print("Done successfully")
                    return
                elif s=="N" or s=="n":
                    print("ok try for deposit choice no :2")
                    return
                else:
                    print("invalid entry:(Y/N)")
                    print("Try Again")
                
        if(newacc==accheck) :
            transfer=float(input("Enter the amount to be transfered:"))
            balancest="SELECT BALANCE,PIN,ACCNAME FROM CURR_ACC WHERE ACCNO="+str(accno)        
            cur.execute(balancest)
            for i in cur:
                balance,pin,accname=i
            if(balance<transfer):
                print("Transfer not possible")
                print("balance<withdraw")
            else:
                S='UPDATE CURR_ACC SET BALANCE=BALANCE-'+str(transfer)+'WHERE ACCNO='+str(accno)       
                cur.execute(S)
                S='UPDATE CURR_ACC SET BALANCE=BALANCE+'+str(transfer)+'WHERE ACCNO='+str(newacc)       
                cur.execute(S)
                conn.commit()
                remarks="Amount transfered to"+str(newacc)
                remarks=str(remarks)
                print("Transferred successfully")
                recordtrans(accno,accname,pin,'Transfer(debit)',balance,balance-transfer,date,remarks)
                balancest="SELECT BALANCE,PIN,ACCNAME FROM CURR_ACC WHERE ACCNO="+str(newacc)        
                cur.execute(balancest)
                for i in cur:
                    balance1,pin1,accname1=i
                
                recordtrans(newacc,accname1,pin1,'Transfer(credit)',balance1-transfer,balance1,date,'Tranfered by'+str(accno))
        else:
            print("Recipient's account doesn't exist")
#------------------------------------------------------------------------------------------------------------
def bulktransfer():
    print("BULK TRANSFER")
    l=[]
    accno=accverify()
    n=int(input("Enter no. of accounts :"))
    datest="SELECT CURDATE()"
    cur.execute(datest)
    for i in cur:
        for j in i:
            date=str(j)
    if(accno!=False):
        while True:
            print("Enter account number of RECIPIENT no.",len(l)+1,end=":")
            newacc=int(input())
            accheck="SELECT ACCNO FROM CURR_ACC WHERE ACCNO="+str(newacc)
            cur.execute(accheck)
            for i in cur:
                for j in i:
                    accheck=int(j)
            if newacc==accno :
                while True:
                    s=input("Do you want to transfer to your own account ?(Y/N)")
                    if s=="Y" or s=="y":
                        print("Done successfully")
                        return
                    elif s=="N" or s=="n":
                        print("ok try for deposit choice no :2")
                        return
                    else:
                        print("invalid entry:(Y/N)")
                        print("Try Again")
            if(newacc==accheck):
                l.append(accheck)
                if len(l)==n:
                    break
            else:
                print("Such an account doesn't exist")
                print("TRY AGAIN !!!")
        transfer=float(input("Enter the amount to be transfered to each employee:"))
        balancest="SELECT BALANCE FROM CURR_ACC WHERE ACCNO="+str(accno)        
        cur.execute(balancest)
        for i in cur:
            for j in i:
                balance=float(j)
        if(balance<(transfer*len(l))):
            print("Transfer not possible")
            print("balance<withdraw")
        else:
            balancest="SELECT BALANCE,PIN,ACCNAME FROM CURR_ACC WHERE ACCNO="+str(accno) #       
            cur.execute(balancest)
            for i in cur:
                balance,pin,acc_name=i
            S='UPDATE CURR_ACC SET BALANCE=BALANCE-'+str(transfer*len(l))+'WHERE ACCNO='+str(accno)
            remarks="Bulk transfer.Transfered to"+str(l)
            recordtrans(accno,acc_name,pin,'Transfer(debit)',balance,balance-transfer*len(l),date,remarks)
            cur.execute(S)
            for i in range(len(l)):
                balancest="SELECT BALANCE,PIN,ACCNAME FROM CURR_ACC WHERE ACCNO="+str(l[i])        
                cur.execute(balancest)
                for J in cur:
                    balance1,pin1,acc_name1=J
                recordtrans(l[i],acc_name1,pin1,'Transfer(credit)',balance1,balance1-transfer,date,"Transfered by"+str(accno))

                a1=l[i]
                S='UPDATE CURR_ACC SET BALANCE=BALANCE+'+str(transfer)+'WHERE ACCNO='+str(a1)
                cur.execute(S)
            print("Amount Transferred successfully")
            conn.commit()
#------------------------------------------------------------------------------------------------------------
def close():
    print("ACCOUNT CLOSING") 
    accno=accverify()
    if(accno!=False):
        a=input("Enter CLOSE to close the account")
        if(a=='CLOSE' or a=='close'):
            balancest="SELECT BALANCE,PIN,ACCNAME FROM CURR_ACC WHERE ACCNO="+str(accno)        
            cur.execute(balancest)
            for i in cur:
                balance,pin,accname=i
            d="DELETE FROM CURR_ACC WHERE ACCNO="+str(accno)
            cur.execute(d)
            print("Account closed successfully")
            typ="acc closed"
            datest="SELECT CURDATE()"
            cur.execute(datest)
            for i in cur:
                for j in i:
                    date=str(j)
            recordtrans(accno,accname,pin,typ,balance,0,date,'acc closed')
        else:
            print("Deletion stopped successfully")
        conn.commit()
        
#-------------------------------------------------------------------------------------------------
# MODIFY :
def modify():
    print("ACCOUNT MODIFICATION")
    accno=accverify()
    if(accno!=False):
        while True:
            print("\t1.CHANGE NAME:")
            print("\t2.CHANGE PIN:")
            print("\t3.exit")
            c=int(input("enter choice:"))
            if c==1:
                n=input("Enter new name:")
                S='UPDATE CURR_ACC SET ACCNAME="'+n+'" WHERE ACCNO='+str(accno)
                cur.execute(S)
                f=open("BANK1.csv",'r+',newline='\n')
                f1=open("temp.csv","w+",newline="")
                w=csv.writer(f1)
                r=csv.reader(f)
                for i in r:
                    if i[1]==accno:
                        i[0]=n
                    w.writerow(i)
                f.close()
                f1.close()
                os.remove("BANK1.csv")
                os.rename("temp.csv","BANK1.csv")
            elif c==2:
                p=input("Enter new pin")
                Y='UPDATE CURR_ACC SET PIN="'+p+'" WHERE ACCNO='+str(accno)
                cur.execute(Y)
            elif c==3:
                break
            else:
                print("Enter correct choice")
                
        print("Modified successfully")
        conn.commit()
#--------------------------------------------------------------------------------------------------
# ALL ACCOUNT HOLDERS LIST :
def displayall():
    cur.execute("select * from curr_acc")
    print("ACC NUM \tNAME \tPIN \tBALANCE \tDATE_OF_TRANSACTION")
    for i in cur:
        for j in i:
            print(j,end="")
            if len(str(j))<25:
                print(" "*(25-len(str(j))),end="")
        print()
#--------------------------------------------------------------------------------------------------
# CUST DETAILS :
def custdetails():
    n=accverify()
    if n!=False:
        file=open("BANK1.csv","r",newline="\n")
        r=csv.reader(file)
        print("accno \taccname \tage \tDOB \tannual income\tphone no")
        for i in r:
            if i[1]==str(n):
                for j in i:
                    print(j,end="   ")
                print()
        file.close()
#--------------------------------------------------------------------------------------------------
# VIEW STATEMENT:    
def viewstatement():
    accno=accverify()
    if(accno!=False):
        a='SELECT ACCNO,TYPE_OF_TRANS,OLDBALANCE,CURRBALANCE,DATE_OF_TRANS,REMARKS FROM TRANS_CURR WHERE ACCNO='+str(accno)
        cur.execute(a)
        print("ACCNO  TYPE_OF_TRANS  OLDBALANCE  CURRBALANCE  DATE_OF_TRANS REMARKS ")
        for i in cur:
            for j in i:
                print(j,end="    ")
            print()
#--------------------------------------------------------------------------------------------------
#LIST OF COMPLAINTS:
def listcomp( ):
    f1=open("complaints.csv",'r',newline='\n')
    a=int(input("ENTER THE ACCOUNT NUMBER TO CHECK THE ACCOUNT HOLDER'S QUERIES:"))
    r=csv.reader(f1)
    print('QUERIES:')
    for i in r:
        if i[0]==str(a):
            print(i[1])
    else:
        print("No more records found")
    f1.close( )
#--------------------------------------------------------------------------------------------------
#ENTER QUERY :
def enterquery():
    f1=open("complaints.csv",'a+',newline='\n')
    b=accverify( )
    if b!= False:
        print('ENTER YOUR QUERY')
        q=input( )
        a=csv.writer(f1)
        a.writerow([b,q])
    else:
        print('NO ACCOUNT FOUND')
    f1.close( )
#--------------------------------------------------------------------------------------------------
def menu():
    print("#-"*40,end="\n\n")
    print("\t\t\tAKA BANK ",end="\n\n")
    ch=0
    while ch!=13:
        print("#-"*40)
        print("Menu options :--------For CUSTOMER TRANSACTIONS :")
        print("\t1.  CREATE A NEW ACCOUNT")
        print("\t2.  DEPOSIT AMOUNT")
        print("\t3.  WITHDRAW AMOUNT")
        print("\t4.  TRANSFER AMOUNT")
        print("\t5.  BULK TRANSFER")
        print("\t6.  MODIFY ACCOUNT")
        print("\t7.  CLOSE ACCOUNT")
        print("\t8.BANK STATEMENT")
        print("Menu options :--------For BANK DETAILS(AUTHORIZED PERSONS ONLY) :")
        print("\t9.  ALL ACCOUNT HOLDERS LIST")
        print("\t10.  CUSTOMER DETAILS")
        print("\t11.LIST OF ALL COMPLAINTS")
        print("Menu options :--------For CUSTOMER SERVICE:")
        print("\t12.ENTER THE QUERIES FOR THE ACCOUNT HOLDER")
        print("#-"*40)
        ch=int(input("\nENTER YOUR CHOICE :"))
        if ch==1:
            create()
        elif ch==2:
            deposit()
        elif ch==3:
            withdraw()
        elif ch==4:
            transfer()
        elif ch==5:
            bulktransfer()
        elif ch==6:
            modify()
        elif ch==7:
            close()
        elif ch==8:
            viewstatement()
        elif ch in (9,10,11): 
            for i in range(3):
                c=checkbankpin()
                if c:
                    if ch==9:
                        displayall()
                    elif ch==10:
                        custdetails()
                    elif ch==11:
                        listcomp()
                    break
            else:
                print("\n\t\t SECURITY BREACH !!!!!")
                ch=13
        elif ch==12:
            enterquery()
        elif ch==13:
            print("Thank You")
        else:
            print("invalid")
        
menu()



