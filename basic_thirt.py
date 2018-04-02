#Print from 1 to 255
def print_range(x,y):
    for item in range (x,y+1):
        print item
print_range(1,255)

#PrintOdd
def print_odd(x,y):
    for item in range (x,y+1):
        if item % 2 != 0:
            print item
print_odd(1,255)

#Print Ints and Sum
def int_sum(x,y):
    sum = 0
    for item in range(x, y + 1):
        sum = sum + item
        print item, ",", sum

int_sum(0,255)
#Print Value in Given Arr
array1 = ["Aaron", "Josiah","Jude"]
def arr_vals(arr):
    for item in arr:
        print item
arr_vals(array1)
#Print Max
arr1 = [4,5,6,99,4724,99999,888888888]
def max(arr):
    max = arr[0]
    for item in arr:
        if max < arr[item]:
            max = arr[item]
        print max
max(arr1)
#Print Average
arr1 = [4,5,6,9,4,9,8]
def average(arr):
    sum = 0
    for item in arr:
        sum += item
    av = sum/len(arr)
    print av
average(arr1)
#Square
arr1 = [99,4,5,6,9,4,9,8]
def square(arr):
    i = 0
    for item in arr:
        arr[i] = item * item
        i+=1
    print arr
square(arr1)
#7. Array with Odds
ReturnOddsArray1To255()
Create an array with all the odd integers between 1 and 255 (inclusive).
def returnOddArr():
    arr = []
    for i in range(2, 256, 2):
        arr.append(i)
    return arr
print "7. Array with Odds"
print returnOddArr()

# 8. Square the Values
def squareArr(arr):
    for i in range(0, len(arr)):
        arr[i] *= arr[i]
    return arr
print "8. Square the Values"
print squareArr([3, 2, 5, 2])

# 9. Greater than Y
def printGreaterY(arr, y):
    for elem in arr:
        if elem > y:
            print elem
print "9. Greater than Y"
printGreaterY([32, 3, 312, 43], 50)

# 10. Zero Out Negative Numbers
def zeroNagative(arr):
    for i in range(0, len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    return arr
print "10. Zero Out Negative Numbers"
print zeroNagative([2, -2, -3, 9, -9])

# 11. Max, Min, Average
def printmma(arr):
    min = arr[0]
    max = arr[0]
    sum = 0
    for elem in arr:
        if elem > max:
            max = elem
        if elem < min:
            min = elem
        sum += elem
    print max, min, sum / len(arr)
print "11. Max, Min, Average"
printmma([32, 56, 2, 3, 4])

# 12. Shift Array Values
def shiftArrLeft(arr):
    for i in range(0, len(arr) - 1):
        arr[i] = arr[i+1]
    arr[-1] = 0
    return arr
print "12. Shift Array Values"
print shiftArrLeft([2, 3, 5, 6])

# Swap String For Array Negative Values

def zeroNagativeDojo(arr):
    for i in range(0, len(arr)):
        if arr[i] < 0:
            arr[i] = "Dojo"
    return arr
print "13. Swap String For Array Negative Values"
print zeroNagativeDojo([32, -3, 2, -2, 3])