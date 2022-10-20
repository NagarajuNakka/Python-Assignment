class Shark:

    # Constructor method with instance variables name and age
    def __init__(self,colour,Vehicle_name, speed,mileage):
        self.name = Vehicle_name
        self.mileage = mileage
        self.speed=speed
        self.colour=colour

def main():
    # First object, set up instance variables of constructor method
    instance1 = Shark("White","School Volo" ,180,12)
    instance2 = Shark("White", "Sudi Q5", 240, 18)

    # Print out instance variable name
    print("colour:",instance1.colour)
    print("Vehicle Name:",instance1.name)
    print("Speed:",instance1.speed)
    print("Mileage:",instance1.mileage)
    print("colour:", instance2.colour)
    print("Vehicle Name:", instance2.name)
    print("Speed:", instance2.speed)
    print("Mileage:", instance2.mileage)
if __name__ == "__main__":
    main()