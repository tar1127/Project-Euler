# Problem 17: 

# if numbers 1 to 5 written out in words : one, two, three, four, five
# then there are 3+3+5+4+4 = 19 letters in total 
# if we write out numbers form 1 to 1000 (inclusive) how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342
# (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
#  The use of "and" when writing out numbers is in compliance with British usage.


toWords = {
            0: "",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety",
            100: "hundred",
            1000: "thousand"
}


# use the above dictionary to get the word format for the number
# Algorithm:
#   if the number is in the dictionary return it
#   if its not in the dictionary, that means its a composite of number from the dictionary
#   i.e: 21 is 20 and 1 --> twentyone
#

def findVal(n):
    return toWords.get(n, None)


def returnLower(val):
    if findVal(val) is not None:
        return findVal(val)
    else:
        comp = str(val)
        valStr = ""
        for j in range(len(comp)):
            valStr += findVal(int(comp[j] + "0" * ((len(comp) - 1) - j)))
        return valStr

def getNumWords(val):
    if val < 100:
        return returnLower(val)
    else:
        comp = str(val)
        comStrUp =  returnLower(int(comp[0]))
        if len(comp) == 3:
            comStrUp += returnLower(int("100"))
        if len(comp) == 4:
            comStrUp += returnLower(int("1000"))
        if comp[1:] != "00" and len(comp) == 3:
            comStrUp += "and"
        comStrUp += returnLower(val % 100)
    return comStrUp


letterCount = 0
for i in range(1,1001,1):
    #print(getNumWords(i))
    letterCount += len(getNumWords(i))

print(letterCount)






