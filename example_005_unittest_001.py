"""A simple example to demonstrate Python unit test framework."""

# Main documentation is here
# https://docs.python.org/3/library/unittest.html

import unittest
from student import Course, Student


class TestStudent(unittest.TestCase):
    """Unit tests for the functions defined in student.py."""
    def test_generate_email001(self):
        """Test generating an email with assertEqual."""
        cs313e = Course("CS313E", 4, 3000)
        cs329e = Course("CS329E", 4, 2500)
        course_list1 = [cs313e, cs329e]

        john = Student("John", "Doe", "01/01/1996", course_list1)

        self.assertEqual(john.generate_email(
            "utexas.edu"), "John.Doe@utexas.edu")

    def test_generate_email002(self):
        """Test generating an email with assertTrue."""
        cs313e = Course("CS313E", 4, 3000)
        cs329e = Course("CS329E", 4, 2500)
        course_list1 = [cs313e, cs329e]

        john = Student("John", "Doe", "01/01/1996", course_list1)

        self.assertTrue("@" in list(john.generate_email("utexas.edu")))

    def test_generate_email003(self):
        """Test generating an email with assertIn."""
        cs313e = Course("CS313E", 4, 3000)
        cs329e = Course("CS329E", 4, 2500)
        course_list1 = [cs313e, cs329e]

        john = Student("John", "Doe", "01/01/1996", course_list1)

        self.assertIn("@", list(john.generate_email("utexas.edu")))


if __name__ == '__main__':
    unittest.main()
