


class Animal(object):
    def __init__(self, name, health):
        self.name = name 
        self.health = health 
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "Current Health:", self.health


class Dog (Animal):
    def __init__(self):
        super(Dog, self).__init__()
        self.health = 150
        return self 
    def pet(self):
        self.health += 75
        return self

class Dragon (Animal):
     def __init__(self):
         super(Dragon, self).__init__()
         self.health = 170
     def fly(self):
         self.health -= 10


Dog.display_health(Dog)
Dragon.display_health(Dragon)

Dog.pet(Dog).pet(Dog).pet(Dog).Dog.pet(Dog).pet(Dog).pet(Dog).Dog.pet(Dog).pet(Dog).pet(Dog)
Dragon.fly(Animal).fly(Animal).fly(Animal).fly(Animal)
     

# class Attack_Whale (Animal):