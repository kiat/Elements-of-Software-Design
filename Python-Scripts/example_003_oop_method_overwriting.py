"""Multiple inheritance - using super(), overloading and overwritting methods"""


class Driver:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return "I am " + self.name + " with salary of " + str(self.salary)

    def work_per_day(self, salary_per_hour):
        return self.salary/(30*salary_per_hour)






class Student:

    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def __str__(self):
        return "I am " + self.name + " with numer of courses " + str(self.courses)

    def work_per_day(self):
        return self.courses * 2



class StudentDriver(Driver, Student):

    def __init__(self, name, salary, courses):
        super().__init__(name, salary)
        self.courses = courses
 
        
    def __str__(self):
        return "I am " + self.name + " with numer of courses " + str(self.courses) + " , and with salary of " + str(self.salary)

    def work_per_day(self):
        return self.salary/(30*15) + self.courses * 2



def main():

    # The method resolution order (or MRO) tells Python how to search for inherited methods
    # print(StudentDriver.__mro__)

    chris = StudentDriver("Chris", 2000, 4)

    print(chris)
    print("Chris works "+str(chris.work_per_day())+" each single day.")


if __name__ == "__main__":
    main()
    