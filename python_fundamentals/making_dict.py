

my_dict = { "Name": "Josiah", "Age": "21", "Country of Birth": "Tanzania", "Favorite Language": "Slang"}

print "My name is", my_dict["Name"]
print "Times around the sun", my_dict["Age"]
print "Place mi madre birthed me", my_dict["Country of Birth"]
print "What I speaketh the mosteth on the reg =", my_dict["Favorite Language"]



def print_my_dict(any_dict):
    for item in any_dict:
        print item
    for k in any_dict.iterkeys():
        print k
    for val in any_dict.itervalues():
        print val
    for key, data in any_dict.iteritems():
        print key, " = ", data
    print any_dict.items()
    print any_dict.keys()
    print any_dict.values()
    



print_my_dict(my_dict)