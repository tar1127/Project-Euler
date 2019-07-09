# Problem 5: 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import time 



# bruit force very inefficient
# ans: 232792560
# took: 112 sec
def Prob5(n,m):
    x = 1
    notFound = True
    while notFound:
        for i in range(n,m):
            if x % i != 0:
                x += 1
                break 
            if i == m-1: 
                print (" found the number {}".format(x))
                notFound = False


# we only need numbers that are divisible by 20 so we don't need to increment by 1
# 1. All numbers have a unique prime factorization
# 2. All non-prime factors of a number, can be generated from the prime factors. 

# in this method we will use the lcm method 
# lcm is the least common multiple of 2 numbers 
# to do that we also need the GCD greatest common divisor of two numbers 
# this is much faster

def findGCD(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def lcm(a, b):
    return a / findGCD(a, b) * b



def Prob5_v2(n,m):
    res = 1
    for i in range(n, m):
        res = lcm(res, i)
    return res


if __name__ == "__main__":
    starttime = time.time()
    print(Prob5_v2(1, 21))
    elspTime = time.time()-starttime

