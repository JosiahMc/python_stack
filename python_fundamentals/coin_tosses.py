# Assignment: Coin Tosses
# Write a function that simulates tossing a coin 5,000 times. Your function should 
# print how many times the head/tail appears.

# # Sample output should be like the following:

# # Starting the program...
# Attempt #1: Thro1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ...
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
# Ending the program, thank you!
# Hint: Use the python built-in round function to convert that floating point number into an integer

import random

def heads_tails ():
    heads_so_far = 0
    tails_so_far = 0
    attempts_so_far = 0
    print "Starting the program..."
    for i in range (0,5000):
        attempts_so_far = attempts_so_far + 1
        coin_toss = random.randint (1,2)
        if coin_toss % 2 == 0:
            heads_so_far = heads_so_far + 1
            print "Attempt #" + str(attempts_so_far) + " Throwing a coin... It's a head!... Got " + str(heads_so_far) + "head(s) so far and " + str(tails_so_far) + " tails so far"
        elif coin_toss % 2 == 1:
            tails_so_far = tails_so_far + 1
            print "Attempt #" + str(attempts_so_far) + " Throwing a coin... It's a tail!... Got " + str(heads_so_far) + "head(s) so far and " + str(tails_so_far) + " tails so far"

    print "Ending the program, thank you!"
heads_tails()