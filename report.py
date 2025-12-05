file = open("day1_20.txt", "r")
buffer = file.readlines()
file.close()

MSFT = buffer[0].strip().split(",")

AMZN = buffer[1].strip().split(",")
  
NVDA = buffer[2].strip().split(",")


MSFT.pop(0)
print(MSFT)
AMZN.pop(0)
print(AMZN)
NVDA.pop(0)
print(NVDA)


for i in range(len(MSFT)):
    MSFT [i] =int( MSFT [i])

for i in range(len(AMZN)):
    AMZN [i] =int( AMZN [i])
    
for i in range(len(NVDA)):
    NVDA [i] =int( NVDA [i])


    
MSFT1 = sum(MSFT) / len(MSFT)
AMZN1 = sum(AMZN) / len(MSFT)
NVDA1 = sum(NVDA) / len(NVDA)

print(MSFT1)
print(AMZN1)
print(NVDA1)




file = open("day21_40.txt", "r")
buffer = file.readlines()
file.close()

MSFT = buffer[0].strip().split(",")

AMZN = buffer[1].strip().split(",")
  
NVDA = buffer[2].strip().split(",")


MSFT.pop(0)
print(MSFT)
AMZN.pop(0)
print(AMZN)
NVDA.pop(0)
print(NVDA)


for i in range(len(MSFT)):
    MSFT [i] =int( MSFT [i])

for i in range(len(AMZN)):
    AMZN [i] =int( AMZN [i])
    
for i in range(len(NVDA)):
    NVDA [i] =int( NVDA [i])


    
MSFT2 = sum(MSFT) / len(MSFT)
AMZN2 = sum(AMZN) / len(MSFT)
NVDA2 = sum(NVDA) / len(NVDA)

print(MSFT2)
print(AMZN2)
print(NVDA2)

buys = []

if MSFT1 < MSFT2: 
    buys.append("MSFT")
    
if AMZN1 < AMZN2: 
    buys.append("AMZN")

if NVDA1 < NVDA2: 
    buys.append("NVDA")
    
buffer = []
line0 = f"MSFT average 1: {MSFT1} average 2: {MSFT2}\n" 
line1 = f"AMZN average 1: {AMZN1} average 2: {AMZN2}\n" 
line2 = f"NVDA average 1: {NVDA1} average 2: {NVDA2}\n" 
line3= f"buys:{buys}"
buffer = [line0,line1,line2,line3]
file = open("report.txt", "w")
file.writelines(buffer)
file.close()