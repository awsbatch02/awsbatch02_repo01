#!usr/bin/python
# To get the first number from the user
print "Please enter first number: "
# Store first input value in a
a = int(input())
# To get second number from the user
print "Please enter second number: "
# Store second input value in b
b = int(input())
# Define a function to add two numbers
def add(var1 , var2):
    c = var1 + var2
    return c
#defining a function to check input number is even or odd
def even(sum):
    e = sum % 2
    if(e == 0):
      print sum," is even number"
    else:
      print sum, "is odd number"
#Defining a function for subtraction
def sub(var1 , var2):
    sub = var1 - var2
    return sub
# Defining a function for multiplication
def mul(var1 , var2):
    mul = var1 * var2
    return mul
# Defining a function for division
def div(var1 , var2):
    div = var1 / var2
    return div
#Calling a addtion function by passing values and store result in Addition variable
addition = add(a , b)
print "Addition of given two numbers is :", addition
#calling even function to check result is even or odd
even(addition)
#Calling subtraction function and store result in subtraction variable
subtraction = sub (a , b)
print "Substraction of given two numbers is :",subtraction
#calling even function to check even or odd
even(subtraction)
#calling muliplication function and store in multiplicatin variable
multiplication = mul(a , b)
print "Multiplication of given two numbers is :",multiplication
#calling even function to check even or odd
even(multiplication)
#Calling div function and store result in division variable
division = div(a , b)
print "Division of given two numbers is: ", division
#calling even function to check even or odd
even(division)


