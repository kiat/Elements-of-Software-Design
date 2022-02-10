from people import *
from course import *

dob1 = '2/12/2000'
start_year1 = '1/8/2020'
hiring_year1 = '1/8/2021'

# Create a Student instance
john = Student("UT-ST-001", "John", "Doe", dob1, start_year1)
print(john)


# Create a professor instance
print("########################")
mike = Professor("UT-ST-002", "Mike", "Doe", dob1, hiring_year1, 6000)

print(mike)


cs313_sec_1 = Course(name="Elements of Software Design",  id="CS313", enrollment=10, section=1)

cs313_sec_2 = Course(name="Elements of Software Design",  id="CS313", enrollment=10, section=2)


print(cs313_sec_1)

print(cs313_sec_2)

print(cs313_sec_1 + cs313_sec_2)



# # Create a Complete University with colleges, professors, staff members, students and projects.
#
#
