
# problem 5: 
# the sum of squared of first 10 numbers: 
#           1^2 + 2^2 + 3^2 + .....+10^2 = 385 
# the square of the sum of the first 10 numbers: 
#           (1 + 2 + ...+10)^2 = 3025 
# hence the difference is 3025 - 385 = 2640

# find the difference between sum of squares 1st one hundred natural numbers 
# and the square of the sum

import time


def sumOfSquare(n): 
    sumVal = 0 
    for i in range(1,n+1):
        sumVal += i*i 
    return sumVal
    
    
def squareOfSum(n): 
    sumVal = 0 
    for i in range(1, n+1):
        sumVal += i 
    return sumVal * sumVal


# much faster then the previous
def sumOfSquare2(n):
    return (n*(n+1)*(2*n+1))/6
    

def squareOfSum2(n):
    return ((n*(n+1))/2)**2


if __name__=="__main__":
    start_time = time.time()
    # for 10,000,000 numbers it took 2.2 Secs
    print(squareOfSum2(100) - sumOfSquare2(100))
    duration = time.time()- start_time
    print("it took {} secs".format(duration))






# using the formulas 
# sum of natural numbers = (n*(n+1))/2 
# sum of squares of natural numbers = (n(n+1)(2n+1))/6

