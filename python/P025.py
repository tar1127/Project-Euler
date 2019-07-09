
# Problem 25
# The Fibonacci sequence is defined by the recurrence relation:
# F(n) = F(n-1) + F(n-2) where F(1) = 1 and F(2)=1.
# Hence the first 12 terms will be:
# F(1)= 1
# F(2)= 1
# F(3)= 2
# F(4)= 3
# F(5)= 5
# F(6)= 6
# F(7)= 13
# F(8)= 21
# F(9)= 34
# F(10)= 55
# F(11)= 89
# F(12)= 144
# the 12th term is the first term contain three digit.
# what is the index of the first term in the Fibonacci sequence to contain 1000 digit.


# returns the next Fibonacci number
def fib():
    x, y = 0, 1
    while True:
        yield y
        x, y = y, x + y

def findFib(nDig):
    index = 0
    for i in fib():
        index += 1
        if len(str(i)) == nDig:
            return index

if __name__=="__main__":
    print(findFib(1000))

