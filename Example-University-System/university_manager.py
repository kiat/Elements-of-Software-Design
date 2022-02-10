from people import *
from course import *


class Course:

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.units = kwargs['units']
        self.college_id = kwargs['college_id']
        self.tuition = kwargs['tuition']



class College:

    def __init__(self, **kwargs):
        '''
        **kwargs is the keyworded arguments
        '''
        self.name = kwargs['name']
        self.college_id = kwargs['college_id']
        self.students = {}
        self.professors = {}
        self.staff_members = {}
        self.courses = {}

    def add_student(self, student):
        self.students.append(student)

    def add_professor(self, prof):
        self.professors.append(prof)

    def add_staff_members(self, staff):
        self.staff_members.append(staff)

    def add_courses(self, course):
        self.courses.append(course)

    def cal_expenses(self):
        '''As an Example all of the costs are salaries'''
        return sum(prof.salary for prof in self.professors) + sum(staff.salary for staff in self.staff_members)

    def cal_revenue(self):
        return sum(course.tuition for course in self.courses) + sum(staff.salary for staff in self.staff_members)


class University:
    def __init__(self, colleges):
        self.colleges = colleges

    def cal_expenses(self):
        return sum(c.cal_expenses() for c in self.colleges)

    def cal_revenue(self):
        return sum(c.cal_revenue() for c in self.colleges)
