# Problem 21:

# save the text file (right click and 'Save Link/Target As...'),

# a 46K text file containing over five-thousand first names,

# begin by sorting it into alphabetical order.

# Then working out the alphabetical value for each name,

# multiply this value by its alphabetical position in the

# list to obtain a name score.


# For example, when the list is sorted into alphabetical order,

# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th

# name in the list. So, COLIN would obtain a score of 938  53 = 49714.

# What is the total of all the name scores in the file?

# open the file and in read



list_of_names = []

with open("../supportFiles/p022_names.txt", 'r') as infile:
    list_of_names = infile.read().replace("\"", "").split(",")

list_of_names = sorted(list_of_names)

count = 0

total_value = 0

for name in list_of_names:
    name_sum = sum([ord(i) - 64 for i in list(name)])

    total_value += name_sum * (list_of_names.index(name) + 1)

print(total_value)
print(list_of_names.index("COLIN"))



#    for line in infile:

#        line = line.replace("\"","")

#        name = line.split(",")

#        list_of_names.append(name)