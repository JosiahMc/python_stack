# Assignment: Fun with Functions
# Create a series of functions based on the below descriptions.

# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your 
# loop executes have your program print the number of that iteration and 
# specify whether it's an odd or even number.

# Your program output should look like below:

# Number is 1.  This is an odd number.
# Number is 2.  This is an even number.
# Number is 3.  This is an odd number.
# ...
# Number is 2000.  This is an even number.

def even_odd ():
    for num in range (1, 2001):
        if num % 2 == 0:
            print "Number is " + str(num) + ". This is an even number."
        if num % 2 == 1:
            print "Number is " + str(num) + ". This is an odd number"
even_odd ()

# Multiply:
# Create a function called 'multiply' that iterates 
# through each value in a list (e.g. a = [2, 4, 10, 16]) 
# and returns a list where each value has been 
# multiplied by 5.

# The function should multiply each value in the list 
# by the second argument. For example, let's say:

# a = [2,4,10,16]
# Then:

# b = multiply(a, 5)
# print b
# Should print [10, 20, 50, 80 ].

def multiply (num):
    lst = [2,4,10,16]
    for i in range (0,len(lst)):
        lst[i] = lst[i] * num
    print lst   
multiply (5)

# def multiples_hack(lst):
#   new_array = []
#   for elem in lst:
#         arr1 = []
#         for i in range(0, elem):
#             arr1.append(1)
#         new_array.append(arr1)
#     print new_array
# multiples_hack (lst)


# COULDNT FIGURE OUT 3rd Problem