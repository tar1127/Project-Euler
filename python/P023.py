# Problem 23:

# A perfect nber is a nber for which the sum of its proper divisors is

# exactly equal to the nber. For example, the sum of the proper divisors

# of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect

# number.

#

# A number n is called deficient if the sum of its proper divisors is

# less than n and it is called abundant if this sum exceeds n.

#

# As 12 is the smallest abundant nber, 1 + 2 + 3 + 4 + 6 = 16,

# the smallest nber that can be written as the sum of two abundant

# nbers is 24. By mathematical analysis, it can be shown that all

# integers greater than 28123 can be written as the sum of two abundant

# nbers. However, this upper limit cannot be reduced any further by

# analysis even though it is known that the greatest nber that cannot

# be expressed as the sum of two abundant nbers is less than this limit.

#

# Find the sum of all the positive integers which cannot be written

# as the sum of two abundant nbers.


# problem 23


# 1. we need a way to find divisors for a given number

# 2. compile a list of abundant numbers less then 28123

# 3. make a list of 1 to 28123 and remove any number that can result of adding

#    two numbers from the abdundent number list


import math

# MY divisorFunction was incorrect. it does not account for perfect squares like 5
# def divisorFind(N):
#
#    #divisorList=list()
#    sumOfDiv = 0
#    # we only need to check up to the sqrt of N
#    for i in range(1, math.ceil(math.sqrt(N))):
#        if N % i == 0:
#            #divisorList.append(i)
#            #divisorList.append(N//i)
#            sumOfDiv += i + N//i
#    # sum of all the divisor except of the N it self
#    sumOfDiv -= N
#    #divisorList.sort()
#    return sumOfDiv


def divisorFind(num):
    if num == 1:
        return 1
    n = math.ceil(math.sqrt(num))
    total = 1
    divisor = 2
    while (divisor < n):
        if (num % divisor == 0):
            total += divisor
            total += num // divisor
        divisor += 1
    if n ** 2 == num:
        total += n
    return total


# hold the list of abundant numbers
listOfAbdundent = list()

# find all the abundant numbers
for i in range(1, 28124):
    if divisorFind(i) > i:
        listOfAbdundent.append(i)


# list from 1 to 28123
listToRemoveFrom = [i for i in range(1, 28124)]

# count = 0

# remove any number that from the list that can be sum of two abundant number.
for j in listOfAbdundent:
    for k in listOfAbdundent:
        if j + k <= 28123:
            listToRemoveFrom[j + k - 1] = 0

print(sum(listToRemoveFrom))


