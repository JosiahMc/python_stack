# Find and Replace
# In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the
# first instance of the word "day". Then create a new string where the word "day" is replaced
# with the word "month".

def find_and_replace (str1):
    daystr = "day"
    print str1.find(daystr)
    newstr1 = str1.replace("day","month",1)
    print newstr1

find_and_replace("It's thanksgiving day. It's my birthday,too!")


# Min and Max
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

def min_max(arr):
    max = arr[0]
    min = arr[0]
    for i in range (0,len(arr)):
        if (max < arr[i]):
            max = arr[i]
        if (min > arr[i]):
            min = arr[i]
    print max
    print min

min_max([2,54,-2,7,12,98])


# First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"].
# Now create a new list containing only the first and last values
# in the original list. Your code should work for any list.

def first_and_last (arr):
    print arr[0], arr[len(arr)-1]
first_and_last(["hello",2,54,-2,7,12,98,"world"])


# New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6].
# Sort your list first. Then, split your list in half. Push the list created from the first half to
# position 0 of the list created from the second half. T
# he output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!

def hard_one (arr):
    arr.sort()
    print arr
    newarr_zero = []
    i = 0
    newarr_zero = arr[0:(len(arr)/2)]
    print newarr_zero
    final_arr = []
    final_arr.append(newarr_zero)
    # final_arr = (arr[(len(arr)/2):(len(arr)-1)]
    final_arr.append(arr[(len(arr)/2):(len(arr))])
    print final_arr


hard_one([19,2,54,-2,7,12,98,32,10,-3,6])
