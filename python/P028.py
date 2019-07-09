#Problem 28

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# See diagram in the problem

# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


# to solve this problem I found a good site where you can enter a seq of numbers and it tells you polynomial function
# to generate it if it exists.

# https://oeis.org/
# this spiral is called a Ulam Spiral
# and has the follwing properties
# lwrRt = 4n^2 - 10n + 7         index n from 1
# lwrLft = 4n^2 + 1              index n from 0
# uprLft = 4n^2 - 6n + 3         index n from 1
# uprRt = (2n+1)^2               index n from 0

def findSpiralSum(n):
    sumVal = 0

    for i in range(n+1):
        lwrRt = 4*(i+1)*(i+1) - 10*(i+1) + 7
        lwrLft = (4*i*i) + 1
        uprLft = 4*(i+1)*(i+1) - 6*(i+1) + 3
        uprRt = (2*i+1)**2

        sumVal += lwrRt + lwrLft + uprLft + uprRt


    return sumVal-3

# since we are looking from 1001X1001 grid we need to half it since we are looking at only the diagonals
print(findSpiralSum(500))



