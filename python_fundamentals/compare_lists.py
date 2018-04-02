#
# Assignment: Compare Lists
# Write a program that compares two lists and prints a message
# depending on if the inputs are identical or not.
#
# Your program should be able to accept
# and compare two lists: list_one and list_two.
# If both lists are identical print "The lists are the same".
# If they are not identical print "The lists are not the same."
# Try the following test cases for
# lists one and two:

def compare_lists(listone,listtwo):
    if (len(listone) != len(listtwo)):
        print "The lists are not the same."
    else:
        isIdentical = True
        i = 0
        while i < len(listone):
            if listone[i] != listtwo[i]:
                isIdentical = False
                break
            i += 1
        if isIdentical:
            print "The lists are the same."
        else:
            print "The lists are not the same."

compare_lists([1,2,5,6,2],[1,2,5,6,2])
compare_lists([1,2,5,6,5],[1,2,5,6,5,3])
compare_lists([1,2,5,6,5,16],[1,2,5,6,5])
compare_lists(['celery','carrots','bread','milk'],['celery','carrots','bread','cream'])
