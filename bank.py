names = []
balences = []
check = False 
while check == False: 
    x = input("do you want to see the menu?")
    if x == "yes": 
        print("1. add account")
        print("2. balence")
        print("3. deposit")
        print("4. withdraw")
        print("5. transfer")
        print("6. remove account")

        action = input ("what do you want to do today?")
        if action == ("add account"):
            print("what is your name?")
        
    elif action == "deposit":
        acctname = input("what account will you like to deposit into?")
    
    elif action == "withdraw": 
        acctname = input("what account will you want to withdraw from?")
        
    elif action == "transfer": 
        acctname= input("what account do you want to transfer too?")
        
    elif action == "remove account": 
        acctname = input("what account do you wish to remove?")    
        
         
        
    elif action == "quit": 
            Check = True 
            
           