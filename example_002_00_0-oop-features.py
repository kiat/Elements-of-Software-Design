class Car:
    '''This class defines a basic car'''

    def __init__(self, cspeed, ngears):
        self.speed = cspeed
        self.gears = ngears

    def run(self, speed):
        '''This method runs the car with the given speed.'''
        self.speed = speed
        print("Running with speed ", self.speed)

    def full_brake(self):
        '''If the full brake is applied, this car will stop.'''
        while (self.speed > 0):
            self.speed -= 1
            print("Stoping this car", self.speed)


class Truck(Car):
    pass

    def full_brake(self):
        '''A truck brakes slowly'''
        while (self.speed > 0):
            self.speed -= 0.1
            print("Stoping this truck", self.speed)

    def __repr__(self):
        return "Truck "


class Sedan_Car(Car):
    pass

    def full_brake(self):
        '''A sedan car can brake fast.'''
        while (self.speed > 0):
            self.speed -= 2
            print("Stoping this sedan", self.speed)

    def __repr__(self):
        return "Sedan_Car"


# Here we create a sedan car.
m_car = Sedan_Car(0, 4)
m_car.run(10)
m_car.full_brake()

# Here we create a truck.
m_truck = Truck(0, 6)
m_truck.run(10)
m_truck.full_brake()


class Toyota_Car:
    # Class of all cars made by toyota
    manufacturer_id = 1223234

    def __init__(self, cspeed, ngears):
        self.gears = ngears

    def run(self, speed):
        self.speed = speed
        print("Running with speed ", self.speed)

    def full_brake(self):
        '''If the full brake is applied, this car will stop.'''
        while (self.speed > 0):
            self.speed -= 1
            print("Stoping this car", self.speed)


# We can access the class attributes without an object of it.
print(Toyota_Car.manufacturer_id)


class Car_Shop():

    def __init__(self, num_employees):
        self.num_employees = num_employees
        self.cars_in_shop = []

    def repair_car(self, car):
        self.cars_in_shop.append(car)
        print("####")
        print("Car shop is reparing a sedan car. Cars in shop are: ")

        for car in self.cars_in_shop:
            print(car)


m_toyota = Sedan_Car(0, 4);
m_truck = Truck(0, 4);

m_car_shop = Car_Shop(4);


# Polymorphism
# Now we bring our cars to the shop.
m_car_shop.repair_car(m_toyota)
m_car_shop.repair_car(m_truck)


# Encapsulation

class Car():
    def __init__(self):
        self.__build__ = 0  # private attribute member
        # “Private” instance variables that cannot be accessed except from inside an object don’t exist in Python.

    def set_year(self, year):

        if (year > 1885 and year < 2021):
            self.__build__ = year
        else:
            print("Year must be between 1885 and 2021")
            self.__build__ = 0

    @property
    def year(self):
        return self.__build__


m_car = Car()
m_car.set_year(2020)
print(m_car.year)

# try to set the build year to 1050
m_car.set_year(1050)
print(m_car.year)

#
m_car.__build__ = 10
print(m_car.__build__)

print(dir(m_car))
