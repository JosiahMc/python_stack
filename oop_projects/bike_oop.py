

class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def display_info(self):
        print "This bike is: {}, Super fast speed rating: {}, Lifetime Mileage: {}".format(self.price, self.max_speed, self.miles)
        
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 1
        return self
    def __repr__(self):
        return "<Bime OBJ Price: {} Speed: {} Mileage {}>".format(self.price, self.max_speed, self.miles)

bike1 = Bike(2000, "200mph") 
bike2 = Bike(200, "200mph")
bike3 = Bike(29900, "20mph") 
bike4 = Bike(27890, "80mph")

bike1.ride().ride().reverse().ride().ride().ride().reverse()
bike2.ride().ride().ride().ride().reverse().reverse()
bike3.reverse().reverse().reverse()


bike1.display_info()
bike2.display_info()
bike3.display_info()