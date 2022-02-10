from people import *
from course import *


def gen_student_form():
    id = input("Enter Student ID: ")
    firstname = input("Enter Student's firstname:")
    lastname = input("Enter Student's lastname:")

    dob = input("Enter Student's date of birth (dd/mm/yyyy):")

    start_year = input("Enter Student's first study year/date (dd/mm/yyyy):")

    return Student(id, firstname, lastname, dob, start_year)