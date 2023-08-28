"""A simple example to demonstrate Python unit test framework."""

import unittest
from student import Course, Student


class TestStudent(unittest.TestCase):
    """Unit tests for the functions defined in student.py."""
    def setUp(self):
        self.cs313e = Course("CS313E", 4, 3000)
        self.cs329e = Course("CS329E", 4, 2500)

        self.john = Student("John", "Doe", "01/01/1996", [self.cs313e, self.cs329e])
        self.matt = Student("Matt", "Doe", "01/01/1998", [self.cs313e])

    def test_generate_email001(self):
        """Test generating an email with assertEqual."""
        self.assertEqual(self.john.generate_email("utexas.edu"), "John.Doe@utexas.edu")

    def test_generate_email002(self):
        """Test generating an email with assertTrue."""
        self.assertTrue("@" in list(self.john.generate_email("utexas.edu")))

    def test_generate_email003(self):
        """Test generating an email with assertIn."""
        self.assertIn(".edu", list(self.john.generate_email("utexas.edu")))

    def test_paid_tuition(self):
        """Test generating the paid tuition sum."""
        self.assertEqual(self.john.paid_tuition(), (3000 + 2500))

    def test_cal_discount(self):
        """Tests if the discount calculation is correct with 2 numbers after decimal point."""
        self.assertAlmostEqual(self.john.cal_discount(20), (3000 + 2500) * 0.2, 2)

    def tearDown(self):
        pass
        # print("For example do something after each test ... ")



if __name__ == '__main__':
    unittest.main()
