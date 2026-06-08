class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def show_info(self):
        print(f"Brand name is {self.brand} and and speed is {self.speed} ")
        

class car(Vehicle):
    def __init__(self, brand , speed , fuel_type):
        super().__init__(brand,speed)
        self.fuel_type = fuel_type
    
    def drive(self):
        print("your car is driving")
        
    def show_info(self):
        print(f"your car of brand {self.brand} have a speed of {self.speed} with fuel type {self.fuel_type}")
        

class bike(Vehicle):
    def __init__(self, brand , speed , bike_type):
        super().__init__(brand,speed)
        self.bike_type = bike_type
    
    def ride(self):
        print("your bike is riding ")
        
    def show_info(self):
        print(f"your bike of brand {self.brand} have a speed of {self.speed} with bike type {self.bike_type}")
        
c1 = car("Toyota Corolla",180,"petrol")
b1 = bike("Yamaha YZF-R15",150,"sports")
c1.show_info()
c1.drive()
print("-----------------------------------------------")
b1.show_info()
b1.ride()