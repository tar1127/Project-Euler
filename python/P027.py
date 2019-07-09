# Problem 27
# Euler discovered the remarkable quadratic formula:
#
# n^2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However,
# when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.
#
# The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79.
# The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n2+an+b, where |a|<1000 and |b|≤1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
# primes for consecutive values of n, starting with n=0.

import itertools

def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


runningMax = 0
aMax = 0
bMax = 0
currentMax = 0

for a in range(-999, 1000):
    for b in range(-999, 1001):
        for i in itertools.count():
            val = i ** 2 + a * i + b
            if isPrime(val):
                currentMax = i
                currentA = a
                currentB = b
            else:
                break
        if currentMax > runningMax:
            runningMax = currentMax;
            aMax = currentA
            bMax = currentB

print(runningMax, aMax, bMax)

print("product:{}".format(aMax * bMax))