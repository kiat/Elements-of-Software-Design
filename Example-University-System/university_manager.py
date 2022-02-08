class University():

    def __init__(self, colleges):
        self.colleges = colleges



class Course:

    def __init__(self, name, units, college, tuition):
        self.__name = name
        self.__units = units
        self.__college = college
        self.__tuition = tuition



class College:

    def __init__(self, name, budget, projects = None, professors, funds, courses):
        self.__name = name
        self.__budget = budget
        self.__professors = professors
        self.__projects = projects
        self.__funds  = funds
        self.__courses = courses

    def cal_expenses(self):


        return 0


    def cal_revenue(self):

        return 0






