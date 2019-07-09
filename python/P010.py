# problem 10: 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# we start with the Eratosthens method to find all the prime number.
import numpy as np


def EratosPrime(n):
    tempArray = [True]*n
    for i in range(2, int(np.sqrt(n))):
        if tempArray[i] is True:
            j = i
            while j < len(tempArray)-i: 
                tempArray[j+i] = False
                j += i
    sumOfPrime = 0
    for i in range(2, len(tempArray)):
        if tempArray[i] is True:
            sumOfPrime += i

    print("\n the sum of the primes below {} is : {}".format(n, sumOfPrime))


if __name__ == "__main__":
    EratosPrime(2000000)
