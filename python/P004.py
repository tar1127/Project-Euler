# Problem 4 : largest palendrome Product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91x99
# Find the largest palindrome made from the product of two 3-digit numbers.

import time 

# this function is faster then the previous one.


def isPalendrome(n):
    # if the reversed value is equal to n then its a palindrome
    if str(n)[::-1] == str(n):
        return True
    return False


if __name__ == "__main__":
    start = time.time()
    A = [i for i in range(100, 999, 1)]

    previousPalendrome = 0
    iValue = 0
    jValue = 0
    for i in A:
        for j in A:
            if isPalendrome(i * j):
                if i * j > previousPalendrome:
                    previousPalendrome = i * j
                    iValue = i
                    jValue = j
    elapsed = time.time() - start
    print("{0} X {1} = {2}".format(iValue, jValue, previousPalendrome))
    print("it took {} sec to find the answer".format(elapsed))