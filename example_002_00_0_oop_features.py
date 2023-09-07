"""
Multiple Example CLasses to Learn about OOP in Python.
"""


class Car:
    """This class defines a basic car"""

    def __init__(self, cspeed, ngears):
        """
        A Car has a Speed attribute and number of Gears.
        """
        self.speed = cspeed
        self.gears = ngears

    def run(self, speed):
        '''This method runs the car with the given speed.'''
        self.speed = speed
        print("Running with speed ", self.speed)

    def full_brake(self):
        '''If the full brake is applied, this car will stop.'''
        while self.speed > 0:
            self.speed -= 1
            print("Stopping this car", self.speed)


class Truck(Car):
    """
    Truck is a type of Car.
    """

    def full_brake(self):
        '''A truck brakes slowly'''
        while self.speed > 0:
            self.speed -= 0.1
            print("Stopping this truck", self.speed)

    def __repr__(self):
        return "Truck "


class SedanCar(Car):
    """A Sedan Car is a Car. """
    def full_brake(self):
        '''A sedan car can brake fast.'''
        while self.speed > 0:
            self.speed -= 2
            print("Stopping this sedan", self.speed)

    def __repr__(self):
        return "Sedan_Car"


class ToyotaCar:
    """
    Class of all cars made by toyota
    """
    manufacturer_id = 1223234

    def __init__(self, cspeed, ngears):
        """A Toyota has speed and gears. """
        self.speed = cspeed
        self.gears = ngears

    def run(self, speed):
        """It runs with a speed."""
        self.speed = speed
        print("Running with speed ", self.speed)

    def full_brake(self):
        '''If the full brake is applied, this car will stop.'''
        while self.speed > 0:
            self.speed -= 1
            print("Stopping this car", self.speed)


class CarShop():
    """
    A Class to represent Car Shops that can
    repair any type of cars.
    """

    def __init__(self, num_employees):
        self.num_employees = num_employees
        self.cars_in_shop = []

    def repair_car(self, car):
        """
        A method to repair any cars.
        """
        self.cars_in_shop.append(car)
        print("Added your car to the repair list.")

    def __str__(self):

        m_string = "Car shop is repairing a sedan car. Cars in shop are: \n"
        for m_car in self.cars_in_shop:
            m_string = m_string  + str(m_car) + "\n"
        return m_string

# Encapsulation
class Auto():
    """
    A Class to represent Car Objects.
    """

    def __init__(self):
        """
        “Private” instance variables that cannot be accessed
        except from inside an object don’t exist in Python.
        """
        self.__build__ = 0
        # private attribute member

    def set_year(self, year):
        """A Method to check and set the build year."""
        if  1885 < year < 2021:
            self.__build__ = year
        else:
            print("Year must be between 1885 and 2021")
            self.__build__ = 0

    @property
    def year(self):
        """A property year. """
        return self.__build__


def main():
    """This is a main function"""

    # Here we create a sedan car.
    m_car = SedanCar(0, 4)
    m_car.run(10)
    m_car.full_brake()

    # Here we create a truck.
    m_truck = Truck(0, 6)
    m_truck.run(10)
    m_truck.full_brake()

    #######################

    # We can access the class attributes without an object of it.
    print(ToyotaCar.manufacturer_id)


    m_toyota = SedanCar(0, 4)
    m_truck = Truck(0, 4)

    m_car_shop = CarShop(4)

    # Polymorphism
    # Now we bring our cars to the shop.
    m_car_shop.repair_car(m_toyota)
    m_car_shop.repair_car(m_truck)

    m_car = Auto()
    m_car.set_year(2020)
    print(m_car.year)

    # try to set the build year to 1050
    m_car.set_year(1050)
    print(m_car.year)

    #
    m_car.__build__ = 10
    print(m_car.__build__)

    print(dir(m_car))

    print("HelloWorld")


if __name__ == "__main__":
    main()
