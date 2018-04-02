


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_new_dict(arr1,arr2):
    new_dict = {}
    for i in range (0,len(arr1)):
        key = arr1[i]
        new_dict[key] = arr2[i]

    print(new_dict)
make_new_dict (name,favorite_animal)



