
# Problem 3: 
# The prime factors of 13195 are 5, 7, 13 and 29. := 5*7*13*29 = 13195
#
# What is the largest prime factor of the number 600851475143 ?

# Prime number can only be divided by 1 or itself and must be whole number 
# eg: prime factor of 12 :  2, 3


# google result turned up the following algorithm to find prime factorization
# https://people.revoledu.com/kardi/tutorial/BasicMath/Prime/Algorithm-PrimeFactor.html
#
# The websites shows the following method:
# lets say the simplest algorithm to find the prime-factors is to repeatedly dividing then number with prime factors
# until the number becomes 1
# ex:
#   lets say we want to find the prime factors of : 100
#   the smallest prime number that divides 100 evenly is 2
#   now we have 50
#   again we find the the smalled prime number that divides 50 evenly again its 2
#   next 50 can be divided by 2 to get 25
#   now 25 can be divided by 5 and 5 is a prime factor.
#   there for the answer is 5.


def primeFactor(factorNum):

    p = 2
    # if p increments to the factorNum it means this is a prime, and can only be divided by 1 or itself
    # so we check
    while factorNum > p * p:
        if factorNum % p == 0:
            # is the number divisible by p? then do the division
            factorNum /= p
        else:
            # otherwise increment p
            p += 1

    return int(factorNum)

if __name__ == "__main__":
    print(primeFactor(600851475143))