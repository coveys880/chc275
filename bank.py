names = ["Shane", "Josh", "Winrey"]
balences = [10, 20, 30]
check = False 
while check == False: 
    x = input("do you want to see the menu?")
    if x == "yes": 
        print("1. add account")
        print("2. print all accounts")
        print("3. deposit")
        print("4. withdraw")
        print("5. transfer")
        print("6. remove account")

        action = input ("what do you want to do today?")
        if action == ("add account"):
           acctname = input("what is your account name?")
           names.append(acctname)
           balences.append(0)
        elif action == "deposit":
            acctname = input("what account will you like to deposit into?")
            index = names.index(acctname)
            money = input ("how much would you want to deposit")
            money = int(money)
            balences [index] = balences [index] + money 
        elif action == "withdraw": 
            acctname = input("what account will you want to withdraw from?")
            index = names.index(acctname)
            money = input("how much do you want to withdraw?")
            money = int(money)
            balences [index] = balences [index] - money
        elif action == "transfer": 
            acctname= input("what account do you want to transfer too?")
            acctname1 = input("what is your second account name?")
            index = names.index(acctname)
            index1 = names.index(acctname1)
            money = input ("how much do you want to transfer from account 1 to 2?")
            money = int(money)
            balences [index]= balences [index] + money 
            balences [index1]= balences [index1] - money 
        elif action == "remove account": 
            acctname = input("what account do you wish to remove?")    
            index = names.index(acctname)
            names.pop(index)
            balences.pop(index)
        elif action == "print all accounts":
            for i in range(len(names)):
                print(f"account name: {names[i]} balences: {balences[i]}") 
               
            
        elif action == "quit": 
                Check = True 
                
           