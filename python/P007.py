
# Problem 7: 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10001st prime number?
import time


def isPrime(n): 

    if n <= 1: 
        return False; 
    if n == 2: 
        return True
        
    if n % 2 == 0: 
        return False 
    
    counter = 3
    while counter**2 <= n:
        if n % counter == 0:
            return False
        else:
            counter += 2
    return True 
    
    
if __name__ == "__main__":
    startTime = time.time()
    primeCount = 0
    numCount = 1
    currentPrimeNum = 1
    while primeCount < 10001:

        if isPrime(numCount):
            currentPrime = numCount
            primeCount+= 1
        numCount += 1
    duration = time.time()- startTime
    print ("it took {} sec".format(duration))
    print (" the {} the prime number is : {}".format(primeCount,currentPrime))
    
    
    

