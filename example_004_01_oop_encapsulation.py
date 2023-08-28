"""An example of encapsulation."""

class Car():
    """A simple Car class to demonstrate encapsulation."""
    def __init__(self, year=1885):
        self.year = year
        # “Private” instance variables that cannot be accessed except from
        # inside an object don’t exist in Python.

    @property
    def year(self):
        """Method to return year value."""
        print("Get year value...")
        return self.__year

    @year.setter
    def year(self, year):
        """Method to set year value."""
        print("Set year value...")
        if 1885 < year < 2022:
            self.__year = year
        else:
            raise ValueError("Year must be between 1885 and 2022")
            # self.__year =  0
            # print("Year must be between 1885 and 2022")

    def __str__(self):
        return str(self.year)


m_car1 = Car(2021)
print(m_car1)
# print(dir(m_car1))

print(m_car1.year)
m_car1.year = 2019
print(m_car1.year)

# 'Car' object has no attribute '__year'
# print(m_car1.__year)
# AttributeError: 'Car' object has no attribute '__year'

print("######  Check if we can create a car with build year 1050 #######")

try:
    m_car2 = Car(1050)
    print(m_car2)
except ValueError as e:
    print("Can not create this car.", e)
