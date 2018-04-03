
# Assignment: Find Characters
# Write a program that takes a list of strings and a string
# containing a
# single character, and prints a new list of all the strings
# containing that character.
#
# Here's an example:

# # input
# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# # output
# new_list = ['hello','world']
# Hint: how many loops will you need to complete this task?

def findcharacter(lists, charact):
    newlist = []
    for idx in lists:
        if idx.find(charact) >= 0:
            newlist.append(idx)

    print newlist
findcharacter(['hello','world','my','name','is','Anna'],"o")
findcharacter(['hello','world','my','name','is','Anna'],"m")
