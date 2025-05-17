ch=0

bank=dict()
#dictionary for storing account number and value as name,type of account and deposit

faq=dict()
#dictionary for storing customer service using account number as key and the query(string)as value

pin=dict()
#dictionary for storing password using account number as key and the password as value

bankpin=4802

import random 
#using the module(random)for generating account number

while(ch!=14):
    print("\t\t\t**********************")
    print("\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t**********************")

    print("\tMAIN MENU")
    print("\t1.NEW ACCOUNT")
    print("\t2.DEPOSIT AMOUNT")
    print("\t3.WITHDRAW AMOUNT")
    print("\t4.ACCOUNT TRANSFER")
    print("\t5.CHECK MY ACCOUNT")
    print("\t6.ALL ACCOUNT HOLDER LIST")
    print("\t7.CLOSE AN ACCOUNT")
    print("\t8.MODIFY AN ACCOUNT")
    print("\t9.DELETE ALL ACCOUNTS")
    print("\t10.CUSTOMER SERVICE")
    print("\t11.STATUS OF COMPLAINT")
    print("\t12.CHANGE MY PIN")
    print("\t13.LIST OF ALL COMPLAINTS")
    print("\t14.EXIT")
    
    print("\t\nSelect Your Option (1-14) \n")
    
    ch=int(input("Enter your choice:"))


    #creating account
    #using the dict bank and using the module random for creating account number. using accno as key and [n,t,d](list) as value
    #using the dict pin for adding password
    if(ch==1):
        a=random.randint(100000000,1000000000)
        if(a not in bank):
            n=input("Name of user:")
            t=input("Type of account(c/s):")
            d=float(input("enter the amount to be deposited:"))
            
            if(d>=0):
                p=int(input("Create your secret pin:"))
                pin[a]=p
                bank[a]=[n,t,d]
                print("\n\nYour account number is :",a)
                print("Account created successfully")
            else:
                print("Deposit cannout be negative")
        else:
            print("Bank is facing a problem,Please try again")
            

    #deposit
    #checking whether acc exist and adding the desired amount using index number and making sure it is positive
    #verifying using the dict pin
    elif(ch==2):
        print("\n")
        b=int(input("Enter your account number:"))
        if( b in bank):
            pincheck=int(input("Enter your pin:"))
            pi=(pin.get(b))
            if(pi==pincheck):
                z=(bank.get(b))
                y=float(input("Enter the amount to be deposited:₹"))
                if(y<=0):
                    print("Deposit cannout be negative or zero")
                else:        
                    z[2]+=y
                    print("The amount has been deposited successfully")
                    print("Updated balence=₹",z[2])
            else:
                print("Incorrect pin")
        else:
            print("Account does not exist")
            

    #withdraw
    #checking whether acc exist and subtracting the desired amount using index number and making sure it is lesser than deposit
    #verifying using the dict pin
    elif(ch==3):
        print("\n")
        b=int(input("Enter your account number:"))
        if( b in bank):
            pincheck=int(input("Enter your pin:"))
            pi=(pin.get(b))
            if(pi==pincheck):
                z=(bank.get(b))
                y=float(input("Enter the amount to be withdrawn:₹"))
                if(y>0):
                    if (z[2]<y):
                        print("Insufficient balance")
                    else:
                        z[2]-=y
                        print("Amount has been withdrawn successfully")
                        print("Updated balance=₹",z[2])
                else:
                    print("Withdraw cannot be in negative or zero")
            else:
                print("Incorrect pin")
        else:
            print("Account does not exist")
            

    #account transfer
    #using deposit+withdraw as an option to perform account to account transfer
    #subtracting the amount using index number and adding the amount to other account using index number
    #verifying using the dict pin
    elif(ch==4):
        print("\n")
        b=int(input("Enter your account number:"))
        if( b in bank):
            e=int(input("Enter The resiptiant's account number :"))
            if(e in bank):
                if(e==b):
                    print("Amount can not be transferred from the same account")
                else:
                    pincheck=int(input("Enter your pin:"))
                    pi=(pin.get(b))
                    if(pi==pincheck):
                        z=(bank.get(b))
                        y=float(input("Enter the amount to be Transfered:₹ "))
                        if(y>0):
                            if(z[2]<y):
                                print("Insufficieent balance")
                            else:
                                z[2]-=y
                                f=(bank.get(e))
                                f[2]+=y
                                print("AMOUNT TRANSFERED SUCCESSFULLY")
                                print("Updated account balance:₹",z[2])
                        else:
                            print("Transfer cannot be equal to zero or negative")

                    else:
                        print("Incorrect pin")
            else:
                print("Account Transfer failed(Account of the other user does not exist)")
        else:
            print("Account does not exist")
            

    #checking the account
    #printing the dict bank using account number and get keys of the dict
    #verifying using the dict pin
    elif(ch==5):
        print("\n")
        b=int(input("Enter your account number:"))
        if( b in bank):
            pincheck=int(input("Enter your pin:"))
            pi=(pin.get(b))
            if(pi==pincheck):
                z=(bank.get(b))
                print("Account Number:\n",b)
                print("Name of the user:\n",z[0])
                print("Type of account:\n",z[1])
                print("Account balence:\n₹",z[2])
            else:
                print("Incorrect pin")
        else:
            print("Account does not exist")
            

    #printing all the accounts registered in the bank
    #using special pin only for bank usage to see th data
    #veryfing using bank pin
    elif(ch==6):
        print("\n")
        if(len(bank)!=0):
            pincheckbnk=int(input("Enter the bank pin to verify:"))
            if(pincheckbnk==bankpin):
                print("AccNO Name Type Balence\n")
                for i in bank:
                    print(i,end="\t")
                    t=bank[i]
                    for j in t:
                        print(j,end="\t")
                    print("\n")
                print("Total number of registered accounts=",len(bank))
            else:
                print("Incorrect pin")
        else:
            print("No account registered")
            

    #deleting an account
    #using the built in function (del)for deleting the specific element from the dictionary bank
    #verify using the dict pin
    elif(ch==7):
        print("\n")
        b=int(input("Enter your account number:"))
        if( b in bank):
            pincheck=int(input("Enter your pin:"))
            pi=(pin.get(b))
            print("\n")
            if(pi==pincheck):
                del bank[b]
                del pin[b]
                print("Account deleted successfully")
                print("\n")
            else:
                print("Incorrect pin")
        else:
            print("Account does not exist")
            

    #modifying an account
    #getting new input for the element in the dictionary bank
    #verifying using the dict pim
    elif(ch==8):
        print("\n")
        b=int(input("Enter your account number:"))
        if( b in bank):
            pincheck=int(input("Enter your pin:"))
            pi=(pin.get(b))
            if(pi==pincheck):
                n=input("Name of user:")
                t=input("Type of account(c/s):")
                bank[b]=[n,t,d]
                print("\n")
                print("Account modifyed successfully")
            else:
                print("Incorrect pin")
        else:
            print("Account does not exist")

    
    #delete the entire dict bank,pin and faq
    #verifying using bank pin
    #using the built in function (clear)
    elif(ch==9):
        print("\n")
        pincheckbnk=int(input("Enter the bank pin:"))
        if(pincheckbnk==bankpin):
            if(len(bank)!=0):
                bank.clear()
                pin.clear()
                faq.clear()
                print("All Accounts has been deleted")
            else:
                print("No account has been registered")
        else:
            print("Incorrect pin")
            

    #customer service
    #using the new dict faq
    #using accno as key and the query as value
    #veryfing using the pin 
    elif(ch==10):
        print("\n")
        check=int(input("Enter your account number:"))
        if(check in bank):
            pincheck=int(input("Enter your pin:"))
            print("\n")
            pi=(pin.get(check))
            if(pi==pincheck):
                query=input("Enter your query:")
                print("\n")
                print("Your query has been raised successfully,Thank you")
                faq[check]=(query)
            else:
                print("Incorrect pin")
        else:
            print("\n")
            print("Account does not exist")
            

    #check my query
    #using the dict faq
    #printing the key of the elemenet from the dict faq
    #veryfing using the pin 
    elif(ch==11):
        print("\n")
        abc=int(input("Enter your account number:"))
        if(abc in faq):
            pincheck=int(input("Enter your pin:"))
            print("\n")
            pi=(pin.get(abc))
            if(pi==pincheck):
                print("Your queryis :",faq.get(abc))
                print("\n\nYour query is under process")
                print("Thank you")
            else:
                print("Incorrect pin")
        else:
            print("Query does not exist")
            

    #changing pin
    #changing the key of the dict pin for an specific element
    elif(ch==12):
        print("\n")
        abc=int(input("Enter your account number:"))
        if(abc in bank):
            pincheck=int(input("Enter your pin:"))
            print("\n")
            pi=(pin.get(abc))
            if(pi==pincheck):
                changepin=int(input("Enter your new pin:"))
                pin[abc]=changepin
                print("Your pin has been changed successfully")
            else:
                print("Incorrect pin")
        else:
            print("\n")
            print("Account does not exist")
            

    #printing all query
    #verify using bank key
    #printing the dict faq
    elif(ch==13):
        print("\n")
        if(len(faq)!=0):
            pincheckbnk=int(input("Enter the bank pin to verify:"))
            print("\n")
            if(pincheckbnk==bankpin):
                for i in faq:
                    print(i,end="\t")
                    t=faq[i]
                    for j in t:
                        print(j,end="")
                    print("\n")
                print("Total number of registered accounts=",len(faq))
            else:
                print("Incorrect pin")
        else:
            print("No account registered")

    
    #end whileloop
    elif(ch==14):
        print("\n")
        print("Thank you!!!!!")

        
    #invalid choice
    else:
        print("\n")
        print("Enter a valid choice!!!!")   
