#print 1-255

#1
def one_to_twofiftysix(start,end):
    for x in range (start, end):
        print x
# one_to_twofiftysix(1,256)
#2
def odd_prints(start,end):
    for x in range (start,end):
        if x % 2 == 1:
            print x
# odd_prints(1,256)
#3
def print_ints_and_sum(start,end):
    sum = 0
    for intiger in range (start, end):
            sum += intiger
            print intiger
            print sum
# print_ints_and_sum(0,256)

#4
def iterate_print(arr):
    for i in range (0,len(arr)):
        print arr[i]
# iterate_print([4,4,4,5,5,5,5])
#5
def find_and_print_max(arr):
    max = arr[0]
    for i in range (0,len(arr)):
        if(max < arr[i]):
            max = arr[i]
    print max
# find_and_print_max([44,444,444,999,393,34949,4949,1,2,3,4,555555,555555555])
#6
