class Course:
    '''
    This class represents a course
    '''
    def __init__(self, id, title, section, enrollment, capacity, classroom):
        self.id = id
        self.title = title
        self.section = section
        self.enrollment = enrollment
        self.capacity = capacity
        self.classroom = classroom

    def __str__(self):
        return "University ID Number: " + self.id + "\nTitle: " + self.title + " enrollment is:  " + str(self.enrollment)

   #
   # def add(self, n):
   #     self.enrollment = self.enrollment + n





