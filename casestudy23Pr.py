# Case Study
from tabulate import tabulate
import datetime
import time
#Welcome
able=4
own=0
sig=0
flag=0
while True:

    print("Welcome to Murugan's Southern Paradise!")
    current_time = datetime.datetime.now()
    if len(str(current_time.minute))==1:
        o="0"
    else:
        o=""
    print("Current Time:",current_time.hour,":",o+str(current_time.minute))
    if current_time.hour==23:
        print("Sorry, the restraunt is closed :(")
        break
    elif current_time.hour<10:
        print("Sorry, the restraunt is closed :(")    
    else:
        if current_time.hour==22 and current_time.minute==55:
           print("Last order for today. 5 more minutes left for closure")
        
        print("--Menu--")

        menul=[["Item Code","Item","Cost in Rs"],["IDS","Idly Sambar (2pcs)",50],["VDS","Vada Sambar (2pcs)",50],["MLD","Masala Dosa",70],["RVD","Rava Dosa",75],["UTM","Uttapam",80],["RSM","Rasam",25]]
        menu={"IDS":["Idly Sambar (2pcs)",50],"VDS":["Vada Sambar (2pcs)",50],"MLD":["Masala Dosa",70],"RVD":["Rava Dosa",75],"UTM":["Uttapam",80],"RSM":["Rasam",25]}
        print(tabulate(menul))
        y=0
        order=[]
        while True:

            if y==1:
                break
            ask=input("Enter the item code(s) separated by a comma: ")
            #enter ADMIN to enter the owner's portal
            if ask.upper()=="ADMIN":
                own=99 #owners portal
                break
            if "," in ask:
                p=ask.split(",")
            else:
                p=ask.split()
            for i in range(len(p)):
                p[i]=p[i].strip()
                p[i]=p[i].upper()
            
            #list with no leading/ending spaces
            #taking order here
            for i in p:
                if i not in menu:
                    print("Item",i,"not found. Please enter it again.")
                    y=2
                    break
                else:
                    order.append(i)
                    y=1
            if y==2:
                continue
            
        #Owners portal here:
        if own==99:
           #password (already taken at first)
            while sig!=5:

               
                entrp=input("Enter your password: ")
                sig=sig+1
                if entrp=="Jupiter@5_washere": #some kind of password
                    print("Authenicated.")
                    flag="Green"
                    break
                else:
                    print("Incorrect Password entered.")
                    continue
                
                
            if sig==5:
                print("Please wait for 5 minutes and Try again later.")
                time.sleep(300)
                continue    
                
            else:
                print("Welcome to Admin portal")
                while True:
                    rnj=int(input("What would you like to perform?\n1. Make changes to the menu (cost, item)\n2. Add Items\n3. Give Discounts\n4. Close the Restraunt for today\n5. Change Timings\n6. Exit\n"))
                    if rnj==1:
                        
                        print(tabulate(menul))
                        itech=input("Enter the item(s) you want to modify (separated by a comma for multiple): ")
                        itech=itech.upper()
                        itech=itech.strip()
                        if "," in itech:
                            ittech=itech.split(",")
                        else:
                            ittech=itech.split()
                        for iffjj in ittech:
                            if iffjj not in menu:
                                print("Item",iffjj,"not in menu")
                                print('Try again')
                                break
                                flag="black"
                            else:
                                print("Okay.")
                                while True:
                                    print("a. Item Code:",iffjj,"b. Item Name:",menu[iffjj][0],"c. Cost in Rs:",menu[iffjj][1],"d. Exit",sep="\n")
                                    asking=input("Which one do you want to modify: ")
                                    
                                    if asking.lower()=="b":
                                        changee=input("Change the item name to: ")
                                        if changee.isalpha==False:
                                            print("Item Name can't be number!")
                                            continue
                                        for hfeuh in menu:
                                            if menu[hfeuh][0]==changee:
                                                print("Item Name already Exists")
                                        else:
                                            menu[iffjj][0]=changee
                                    elif asking.lower()=="c":
                                        changee=int(input("Change the item cost to: "))
                                        if changee.isalpha==False:
                                            print("Item Name can't be number!")
                                            continue
                                        for hfeuh in menu:
                                            if menu[hgeuh][0]==changee:
                                                print("Item Name already Exists")
                                        else:
                                            menu[iffjj][0]=changee
                                    else:
                                        break
                                        

                                
                        if flag==black:
                            continue #item not found, trying again
                                
                        
                    
                        
                








        else:      
            #customer side continues
            print("YOUR ORDER")
            tab=[["Item Code","Item","Cost in Rs"]]
            #order displayed
            #changes area
            tot=0
            for f in order:
                tot=tot+menu[f][1]
                tab.append([f,menu[f][0],menu[f][1]])
            tab.append(["","TOTAL:",tot])
            print(tabulate(tab))
        
         
            while True:
                cha=input("Do you want to make any changes? (Y/N): ")
                if cha.upper()=="Y":
                    print("1. Delete an Item","2. Modify an Item","3. Cancel the Order",sep="\n")
                    ut=int(input("Your choice: "))
                    if ut==1:
                        eli=input("Enter the item code(s) you want to remove (separated by a comma for multiple): ")
                        if "," in eli:
                            hi=eli.split(",")
                        else:
                            hi=eli.split()
                            print(hi)
                        for rem in hi:
                            remm=rem.strip()
                            if remm in menu:
                                for lyy in range(len(tab)):
                                    if tab[lyy][0]==remm:
                                        tab.pop(lyy)
                                        break
                            else:
                                print("Element",remm,"was not found.")
                            print("Updated Order")
                            tab.pop()
                            tot=tot-menu[remm][1]
                            tab.append(["","TOTAL:",tot])

                            print(tabulate(tab))
                            print()
                    elif ut==3:
                        print("Sorry to see you go :( Order Cancelled!")
                        print()
                        time.sleep(3)
                        break
                    elif ut==2:
                        itt=input("Which Item do you want to modify: ")
                        itt=itt.upper()
                        itit=itt.strip()
                        flag=100
                        for zsz in range(len(tab)):
                            if tab[zsz][0]==itit:                    
                                tot=tot-menu[itit][1]
                                tab.pop(zsz)
                                flag=8
                                break
                        if flag!=8:
                            print("Your entered item is absent in your order. Try again.")
                            continue
                            
                        jiji=input("What should replace it?: ")
                        jiji=jiji.upper()
                        jtt=jiji.strip()
                        if jtt in menu:
                            tab.pop()
                            tab.append([jtt,menu[jtt][0],menu[jtt][1]])
                            tot=tot+menu[jtt][1]
                            tab.append(["","TOTAL:",tot])
                            print("Updated Order")
                            print(tabulate(tab))
                            print()
                        else:
                            print("You entered something invalid. Try again.")
                            print()

                        
                if cha.upper()=="N":
                    able=able-1

                    print("Okay! Order under preparation")
                    time.sleep(2)
                
                    print(able,"vacant tables remaining")
                
                    if able==0:
                        print("Please wait till the table is free. We'll now take orders after 4 minutes")
                        time.sleep(240)
                    print()
                    break
                
                
                
        
