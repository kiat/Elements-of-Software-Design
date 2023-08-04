"""
A Demonstration Example of Multiple Inheritance in Python.
"""

class Driver:
    """A Class to present Objects of Type Driver."""

    def __init__(self, name, salary):
        """A Driver has a name, and salary."""
        self.name = name
        self.salary = float(salary)

    def __str__(self):
        """A simple string method to convert a driver object to a string."""
        return "I am " + self.name + " with a salary of " + str(self.salary)

    def work_per_day(self, salary_per_hour):
        """
        Calculates the number of hours a driver has
        to work for a given amount of salary per month.
        As an argument salary per hour is given.
        """
        return round(self.salary / (30 * salary_per_hour), 2)


class Student:
    """A Student Class."""

    def __init__(self, name, courses):
        """Students have a name and number of courses taken."""
        self.name = name
        self.courses = courses

    def __str__(self):
        """A String representation of this object."""
        return "I am " + self.name + " with a number of courses " + str(self.courses)

    def work_per_day(self):
        """
        Calculates the hours of study for
        a student given the number of courses.
        """
        return self.courses * 2


class StudentDriver(Driver, Student):
    """
    A Student Driver is a person who is a student
    and has to work as a driver part-time.
    """

    def __init__(self, name, salary, courses):
        """A Student driver is a student and is also a Driver."""
        super().__init__(name, salary)
        Student.__init__(self, name, courses)

    def __str__(self):
        """A string representation."""
        return "I am " + self.name + " with a number of courses " \
        + str(self.courses) + " , and with a salary of " + str(self.salary)

    def work_per_day(self, salary_per_hour=15):
        """Calculates hours of work for a student driver."""
        return super().work_per_day(salary_per_hour) + Student.work_per_day(self)


def main():
    """
    A main function to create objects of the above classes,
    and demonstrate their method calls.
    """

    # The method resolution order (or MRO) tells Python how to search for inherited methods
    # print(StudentDriver.__mro__)

    chris = StudentDriver("Chris", 2000, 4)

    print(chris)
    print("Chris works " + str(round(chris.work_per_day(), 2)) +
          " hours each single day.")


if __name__ == "__main__":
    main()
    