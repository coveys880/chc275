x = input("what is x")
x = int (x)
check = False 
while check == False:
    if x % 2 == 0:
        x = x/2
        print(x)
    else: 
        x = x * 3 + 1
        print (x)
    if x == 1:
        check = True