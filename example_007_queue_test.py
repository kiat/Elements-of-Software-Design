import unittest
from example_007_queue import *


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.my_queue = Queue()

        # enqueue 10
        self.my_queue.enqueue(10)
        # enqueue 18
        self.my_queue.enqueue(18)
        # enqueue 1024
        self.my_queue.enqueue(1024)


    def test_enqueue(self):
        self.assertEqual(self.my_queue.queue, [10, 18, 1024])

    def test_dequeue(self):
        self.my_queue.dequeue()
        print(self.my_queue)
        self.assertEqual(self.my_queue.queue, [18, 1024])

    def test_size(self):
        self.my_queue.dequeue()
        self.my_queue.dequeue()
        self.assertEqual(self.my_queue.size(), 1)

    def test_isEmpty(self):
        self.my_queue.dequeue()
        self.my_queue.dequeue()
        self.my_queue.dequeue()

        self.assertTrue(self.my_queue.isEmpty())

    def tearDown(self):
        pass
        # print("For example do something after each test ... ")



if __name__ == '__main__':
    unittest.main()