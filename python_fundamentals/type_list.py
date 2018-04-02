#
# Assignment: Type List
# Write a program that takes a list and
# prints a message for each element in the list,
# based on that element's data type.
#
# Your program input will always be a list. For each
# item in the list, test its data type. If the
# item is a string, concatenate it onto a new string.
# If it is a number, add it to a running sum. At the
# end of your program print the string, the number
# and an analysis of what the list contains. If it
# contains only one type, print that type, otherwise,
# print 'mixed'.
#
# Here are a couple of test cases. Think of some of
# your own, too. What kind of unexpected input
# could you get?


def type_list (lst):
    strL = ""
    sumL = 0
    for el in lst:
        if type(el) is int or type(el) is float:
            sumL += el
        elif type(el) is str:
            strL += el + " "
    if strL != "" and sumL != 0:
        print "The list you entered is mixed type"
        print "String:", strL
        print "Sum:", sumL, "\n"
    elif sumL != 0:
        print "The list you entered is of integer type"
        print "Sum:", sumL, "\n"
    elif strL != "":
        print "The list you entered is of string type"
        print "String:", strL, "\n"
type_list (['magical unicorns',19,'hello',98.98,'world'])
type_list ([2,3,1,7,4,12])
type_list(['magical','unicorns'])
