import unittest
from student import *


class TestStudent(unittest.TestCase):

    def test_generate_email001(self):
        cs313e = Course("CS313E", 4, 3000)
        cs329e = Course("CS329E", 4, 2500)
        course_list1 = [cs313e, cs329e]

        john = Student("John", "Doe", "01/01/1996", course_list1)

        self.assertEqual(john.generate_email("utexas.edu"), "John.Doe@utexas.edu")

    def test_generate_email002(self):
        cs313e = Course("CS313E", 4, 3000)
        cs329e = Course("CS329E", 4, 2500)
        course_list1 = [cs313e, cs329e]

        john = Student("John", "Doe", "01/01/1996", course_list1)

        self.assertTrue("@" in list(john.generate_email("utexas.edu")))

    def test_generate_email003(self):
        cs313e = Course("CS313E", 4, 3000)
        cs329e = Course("CS329E", 4, 2500)
        course_list1 = [cs313e, cs329e]

        john = Student("John", "Doe", "01/01/1996", course_list1)

        self.assertIn("@", list(john.generate_email("utexas.edu")))



if __name__ == '__main__':
    unittest.main()
