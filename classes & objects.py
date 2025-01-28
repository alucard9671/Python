class Car():#blueprint
    def __init__(self, brand, model, year):
        self.brand = brand # Instance variable {Unique to its class}
        self.model = model
        self.year = year
        
    rear_wheel = 2 #[Class variables] are the rules for all variables and sub-classes which do not change. Uses the back 2 tires to move
    front_wheel = 2 #Uses the front 2 tires to move
    all_wheel = 4 # Uses all 4 tires to move

    def display_car(self): #Methods are instructions on how the code should run 
        self.brand = input("enter the car brand: ")#Instance variable unique to each input/"piece". Each car has a different brand
        self.model = input("Enter the car model:")

class Model(Car):#
    def __init__(self, name):
        super.__init__(self, name)
    def model(self):
        name = input("Enter car brand: ")

    def year(self):
        year = int(input("enter what year the car was made: "))


#e.g.
class Beer():
    alchol = "6%" #Class variable

    def __init__(self, flavour, drink):
        self.flavour = flavour
        self.drink = drink #instance variable

    def pouring(self):#Instance method
        print(f"Pour {self.drink} into a glass at a 45 degree angle")

    @classmethod
    def beer_rules(cls): #Class Method
        print(f"all beer has {cls.alchol} alchol")

    @staticmethod
    def beer_fact(): #Static method
        print("Drink more than 3 and you'll get drunk.")

beer1 = Beer("flying fish")
beer1.pouring()
 