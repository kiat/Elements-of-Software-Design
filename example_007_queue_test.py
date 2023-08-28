'''Tests functionality of our queue implementation.'''
import unittest
from example_007_queue import Queue


class TestStudent(unittest.TestCase):
    '''TestStudent extends a unittest TestCase.'''

    def setUp(self):
        self.my_queue = Queue()

        # Enqueue 10
        self.my_queue.enqueue(10)
        # Enqueue 18
        self.my_queue.enqueue(18)
        # Enqueue 1024
        self.my_queue.enqueue(1024)


    def test_enqueue(self):
        '''Test that the enqueue implementation is correct.'''
        self.assertEqual(self.my_queue.queue, [10, 18, 1024])

    def test_dequeue(self):
        '''Test that the dequeue implementation is correct.'''
        self.my_queue.dequeue()
        print(self.my_queue)
        self.assertEqual(self.my_queue.queue, [18, 1024])

    def test_size(self):
        '''Test that the size implementation is correct.'''
        self.my_queue.dequeue()
        self.my_queue.dequeue()
        self.assertEqual(self.my_queue.size(), 1)

    def test_is_empty(self):
        '''Test that the is_empty implementation is correct.'''
        self.my_queue.dequeue()
        self.my_queue.dequeue()
        self.my_queue.dequeue()

        self.assertTrue(self.my_queue.is_empty())

    def tearDown(self):
        pass
        # print("For example do something after each test ... ")



if __name__ == '__main__':
    unittest.main()
