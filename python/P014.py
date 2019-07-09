# Problem 14: 
# n -> n/2 (n is even)
# n -> 3n+1 (n is odd) 

# using the rule above and starting with 13 the sequence is:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) 
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz(n):
    count = 0  
    while n > 1:
        count += 1
        if n % 2 == 0:
            n /= 2
        else: 
            n = 3*n + 1
        if n == 1:
            count += 1
    return count #"number of collatz: {}".format(count)


if __name__ == "__main__":
    currentLength = 0
    nValue = 0
    for i in range(1, 1000000):
        length = collatz(i)
        if length > currentLength:
            nValue = i
            currentLength = length


    print(currentLength)
    print(nValue)
