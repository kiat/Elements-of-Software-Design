class Course:
    '''
    This class represents a course
    '''
    def __init__(self, **kwargs):

        self.id = kwargs['id']
        self.name = kwargs['name']

        if 'units' in kwargs:
            self.units = kwargs['units']
        else:
            self.units = None

        if 'tuition' in kwargs:
            self.tuition = kwargs['tuition']
        else:
            self.tuition = None

        if 'section' in kwargs:
            self.section = kwargs['section']
        else:
            self.section = None

        if 'enrollment' in kwargs:
            self.enrollment = kwargs['enrollment']
        else:
            self.enrollment = None

        if 'capacity' in kwargs:
            self.capacity = kwargs['capacity']
        else:
            self.capacity = None


    def __str__(self):
        return "University ID Number: " + self.id + "\nTitle: " + self.title + " enrollment is:  " + str(self.enrollment)

    def add(self, n):
       self.enrollment = self.enrollment + int(n)



    def __str__(self):
        '''
        We print the course name, section number and enrollment
        '''
        return self.id + " , " + self.name + " , " + str(self.section) + " , " + str(self.enrollment)



    def __add__(self, other_course):
        '''
        This dunder method enables + operator on two courses.
        '''
        if isinstance(other_course, Course):
            self.enrollment = self.enrollment + other_course.enrollment
            self.section = int(self.section) + int(other_course.section)

            return self
        raise Exception(f"{other_course} is not of class Course")

# Dunder Methods in Python
#
# __sub__
# for subtraction(-)
#
# __mul__
# for multiplication(*)
#
# __truediv__
# for division( /)
#
# __eq__
# for equality(== )
#
# __lt__
# for less than( <)
#
# __gt__
# for greater than( >)
#
# __le__
# for less than or equal to (≤)
#
# __ge__
# for greater than or equal to (≥)

# Documentation here, Python Data model
# https://docs.python.org/3/reference/datamodel.html








