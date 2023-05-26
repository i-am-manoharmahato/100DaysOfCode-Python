#!/usr/bin/env python3

def is_leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

if ((is_leap_year(year) == True) and (month == 2)):
    resulting_days = 29
else:
    resulting_days = days_in_month[month-1]

print(f'Number of days: {resulting_days}')