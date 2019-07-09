# Problem 9:
# A Pythagorean triplet is a set of three natural numbers a < b < c
# for example 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# there exists exactly one Pythagorean triplet for which a+b+c = 1000
# find the product abc. 

def findPythogTrip(N):
    sumVal = 0
    m = 1
    n = m+1
    while sumVal <= N:
        a = n ** 2 - m ** 2
        b = 2 * n * m
        c = n ** 2 + m ** 2
        m+=1
        n+=m+1
        sumVal = a+b+c
        if sumVal == 1000:
            print("{}, {}, {} sum : {}".format(a, b, c, sumVal))
            print ("the product is : {}".format(a*b*c))
            break




if __name__== "__main__":
    findPythogTrip(1000)