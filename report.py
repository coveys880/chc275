file = open("day1_20.txt", "r")
buffer = file.readlines()
file.close()

MSFT = buffer[0].strip().split(",")
AMZN = buffer[1].strip().split(",")
NVDA = buffer[2].strip().split(",")

MSFT.pop(0)
print(MSFT)
AMZN.pop(1)
print(AMZN)
NVDA.pop(2)
print(NVDA)

