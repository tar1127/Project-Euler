# Problem 1:
# If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of 
# these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.

# expected Answer: 233168


# loop through 0 to maxvalue check each value if multiple of 3 or 5
# save the values in an array and  return the sum
def findsum(maxvalue):
    """
    >>> findsum2(1000)
    233168

    :param maxvalue: loop to maxvalue
    :return: the sum of all values from 0 to maxvalue which are divisible by 3 or 5
    """
    # this array will hold the numbers that are multiple of 3 or 5 
    tempArray=[]
    for i in range(maxvalue):
        if i % 3 == 0 or i % 5 == 0: 
            tempArray.append(i)
    return sum(tempArray)


# does the same thing as the findsum but more compact code
#
def findsum2(maxvalue):
    """
     >>> findsum2(1000)
     233168

    :param maxvalue: loop to maxvalue
    :return: the sum of all values from 0 to maxvalue which are divisible by 3 or 5
    """
    # filter creates a list of elements for which function returns true  : filter(function, list)
    # lambda function is checking if each value in the range is multiple of 3 or 5.
    # then we sum the filtered values to get time final result.
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(maxvalue)))


if __name__ == "__main__":
    # need doctest lib to run the test inside the functions
    import doctest
    doctest.testmod()

    # print the result
    print("the result is {}".format(findsum(1000)))
    print(findsum2(1000))



