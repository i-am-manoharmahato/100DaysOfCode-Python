#!/usr/bin/env python3

def is_leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False
    
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

print (is_leap_year(2012))