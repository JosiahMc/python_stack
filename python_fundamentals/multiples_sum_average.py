# Assignment: Multiples, Sum, Average
# This assignment has several parts. All of your code
# should be in one file that is well commented to indicate what each block
# of code is doing and which problem you are solving. Don't forget to test your code as you go!



# Multiples
# Part I - Write code that prints all the odd numbers from
# 1 to 1000. Use the for loop and don't use a list to do this exercise.

def multiples(start,stop):
    for i in range (start,stop):
        if i % 2 == 1:
            print i
# multiples(1,1001)


# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

def multiples_five(start,stop):
    for i in range (start,stop):
        if i % 5 == 0:
            print i
# multiples_five(5,1000000)


# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
def sum_list (arr):
    sum = 0
    for i in range (0,len(arr)):
        sum += arr[i]
    print sum

sum_list([1, 2, 5, 10, 255, 3])

# Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
