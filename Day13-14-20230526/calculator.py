#!/usr/bin/env python3

##====================================================================================================##
## This program is to build a basic calculator where it asks the user to choose the 
## operation he/she wants to perform. e.g. Addition (+), Subtraction (-), Multiplication (*)
## Division (/). Then the user is asked for the input 2 number and once the user enters the numbers,
## result is shown on the screen followed by a question if the user wants to continue.
## If user continues, then the previous result is taken as the first number for the
##operationa and only the second number is asked. 
##====================================================================================================##


import os

def add(a, b):
    return float(a)+float(b)

def subtract(a, b):
    return float(a)-float(b)

def multiply(a, b):
    return float(a)*float(b)

def divide(a, b):
    return float(a)/float(b)


def check_operation(opr, nu1, nu2):
    if opr == "+":
        result = add(nu1, nu2)
    elif opr == "-":
        result = subtract(nu1, nu2)
    elif opr == "*":
        result = multiply(nu1, nu2)
    elif opr == "/":
        result = divide(nu1, nu2)
    return result
    

operation = input(f'What operation do you want to do? + - * /  ==>  ')
num_1 = input(f'Enter the first number: ')
num_2 = input(f'Enter the second number: ')
result = check_operation(operation, num_1, num_2)
print(f'{result}')

is_continue = True

while is_continue == True:
    continue_check = input(f'Do you want to continue forward with the current result? y/n ')
    if continue_check == "n":
        os.system("clear")
        is_continue = "False"
        break
    else:
        current_result_val = result
        operation = input(f'What operation do you want to do further? + - * /  ==>  ')
        temp_num = input(f'Enter the second number: ')
        result = check_operation(operation, current_result_val, temp_num)
        print(f'{result}')