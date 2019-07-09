
# You are given the following information, but you may prefer to do some

# research for yourself.

#

# 1 Jan 1900 was a Monday.

# Thirty days has September,

# April, June and November.

# All the rest have thirty-one,

# Saving February alone,

# Which has twenty-eight, rain or shine.

# And on leap years, twenty-nine.

# A leap year occurs on any year evenly divisible by 4, but not on a

# century unless it is divisible by 400.



# How many Sundays fell on the first of the month during the twentieth

# century (1 Jan 1901 to 31 Dec 2000)?


month_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# dec 31 1900 is a ?

# 0 = monday

# 6 = sunday

# if i use number % 7

def day_of_week(num_days):
    day = num_days % 7

    if day == 0:
        return "tuesday"

    if day == 1:
        return "wednesday"

    if day == 2:
        return "thursday"

    if day == 3:
        return "firday"

    if day == 4:
        return "saturday"

    if day == 5:
        return "sunday"

    if day == 6:
        return "monday"

from datetime import date, timedelta

start = date(1900, 1, 1)

end = date(2000, 12, 31)

#print(start.year + 1)

#print(end.day)

#print(date.weekday(start))

current = date(1901, 1, 1)

num_sun_frst = 0

while current < end:

    if date.weekday(current) == 6 and current.day == 1:
        num_sun_frst += 1

    current += timedelta(days=1)

print(num_sun_frst)