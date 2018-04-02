# Assignment: Filter by Type
# Write a program that, given some value, tests that value
# for its type. Here's what you should do for each type:
#
# Integer
# If the integer is greater than or equal to 100, print
# "That's a big number!" If the integer is less than 100,
# print "That's a small number"
#
# String
# If the string is greater than or equal to 50 characters
# print "Long sentence." If the string is shorter than 50
# characters print "Short sentence."
#
# List
# If the length of the list is greater than or equal to 10
# print "Big list!" If the list has fewer than 10 values
# print "Short list."
#
# Test your program using these examples:



def filter_by_type(num):
    if num >= 100:
            print "That's a big number!"
    else:
            print "That's a small number"
filter_by_type(45)
filter_by_type(100)
filter_by_type(455)
#etc...

def filter_by_type2 (str):
    if len(str) >= 50:
        print "Long sentence"
    else:
        print "Short sentence"


filter_by_type2("Rubber baby buggy bumpers")
filter_by_type2 ("Experience is simply the name we give our mistakes")
filter_by_type2 ("Tell me and I forget. Teach me and I remember. Involve me and I learn.")

def filter_by_type3(arr):
    if len(arr) >= 10:
        print "Big list"
    else:
        print "Short list"

filter_by_type3([1,7,4,21])
filter_by_type3([3,5,7,34,3,2,113,65,8,89])
filter_by_type3([4,34,22,68,9,13,3,5,7,9,2,12,45,923])
filter_by_type3([])
filter_by_type3(['name','address','phone number','social security number'])
