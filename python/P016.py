# Problem 16: 
# 2^15 = 32768  and the sum of the digits 3+2+7+6+8 = 26 
# what is the sum of the digits for 2^1000

listOfNum = list((str(2**1000)))

sumOfNum = 0 

for i in listOfNum:
    sumOfNum += int(i)

print(sumOfNum)

