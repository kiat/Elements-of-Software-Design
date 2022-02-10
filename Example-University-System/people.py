class Person:
    '''
    This class represents a person
    '''

    def __init__(self, id, firstname, lastname, dob):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob

    def __str__(self):
        return "University ID Number: " + self.id + "\nName: " + self.firstname + " " + self.lastname

    def __repr__(self):
        return self.firstname + " " + self.lastname

    def get_salary(self):
        return 0


class Student(Person):
    '''
    This class represents a Student
    '''

    def __init__(self, id, firstname, lastname, dob, start_year):
        self.start_year = start_year
        self.courses = []

        # invoking the __init__ of the parent class
        # Person.__init__(self, firstname, lastname, dob)
        # or better call super()
        super().__init__(id, firstname, lastname, dob)

    def add_course(self, course_id):
        self.courses.append(course_id)

    def get_courses():
        return self.courses

    def __str__(self):
        return super().__str__() + ". This student has the following courses on records: " + str(list(self.courses))

    # A student has no salary.
    def get_salary(self):
        return 0
    


class Professor(Person):
    '''
    This class represents a Professor in the university system.
    '''

    def __init__(self, id, firstname, lastname, dob, hiring_year, salary):
        self.hiring_year = hiring_year
        self.salary = salary

        self.courses = set()
        self.research_projects = set()

        super().__init__(id, firstname, lastname, dob)

    def __str__(self):
        return super().__str__() + ". This Professor is the instructor of record of following courses : " + str(
            list(self.courses))

    def add_course(self, course_id):
        self.courses.add(course_id)

    def add_courses(self, courses):
        for course in courses:
            self.courses.add(course)

    def get_courses():
        return self.courses

    def get_salary(self):
        return self.salary


class Staff(Person):
    '''
    This class represents a staff member.
    '''

    def __init__(self, id, firstname, lastname, dob, hiring_year, salary):
        self.hiring_year = hiring_year
        self.salary = salary
        super().__init__(id, firstname, lastname, dob)

    def __str__(self):
        return super().__str__() + ". This Staff memeber has a salary of " + str(self.salary)

    def get_salary(self):
        return self.salary





class Teaching_Assistant(Staff, Student):
    '''
    A Teaching Assistant is a student and is a staff member.

    '''

    def __init__(self, id, firstname, lastname, dob, start_year,  hiring_year, salary):

        Student.__init__(self, id, firstname, lastname, dob, start_year)
        self.hiring_year = hiring_year
        self.salary = salary

        # Staff().__init__(self, id, firstname, lastname, dob, hiring_year, salary)


    def __str__(self):
        return Student.__str__(self) + Staff.__str__(self)




