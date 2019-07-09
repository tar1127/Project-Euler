
# Problem 24

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible
# permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or
# alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import itertools

count = 0
for i in itertools.permutations(range(10)):
    count += 1
    if count == 1000000:
        ans = i
        break
numStr = ""
for j in i:
    numStr += str(j)
print(numStr)


# the above was the easy way to do it.

