# Problem 26: A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with
# denominators 2 to 10 are given:
# 1/2 = 0.5
# 1/3 = 0.(3)
# 1/4 = 0.25
# 1/5 = 0.2
# 1/6 = 0.1(6)
# 1/7 = 0.(142857)
# 1/8 = 0.125
# 1/9 = 0.(1)
# 1/10 = 0.1

# where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a
# 6-digit recurring cycle.
# find the value of d < 1000 for which 1/d contains the longest recurring cycles in the its decimal fraction

# example 7
# 1 / 7   => 10 / 7    1 r 3   <==== repeats
# 3 / 7   => 30 / 7    4 r 2
# 2 / 7   => 20 / 7    2 r 6
# 6 / 7   => 60 / 7    8 r 4
# 4 / 7   => 40 / 7    5 r 5
# 5 / 7   => 50 / 7    7 r 1
# 1 / 7   => 10 / 7    1 r 3    <==== repeats


def findCycle(divisor):
    dividend = 1
    remainderList = []
    repeatFound = False
    while dividend % divisor != 0 and not repeatFound:
        remainder = dividend % divisor
        if remainder in remainderList:
            repeatFound = True

        remainderList.append(remainder)
        # print(remainderList)
        remainder *= 10
        dividend = remainder
        # print(remainder)
    if len(remainderList) < 1:
        return 0

    return (len(remainderList) - 1) - remainderList.index(remainderList[-1])


if __name__ == "__main__":

    previousMaxLen = 0
    for i in range(1, 1000):
        currentMaxLen = findCycle(i)
        if currentMaxLen > previousMaxLen:
            iVal = i
            previousMaxLen = currentMaxLen

    print("1/{} : {}".format(iVal, previousMaxLen))