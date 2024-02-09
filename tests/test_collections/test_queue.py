from data_structures.collections import Queue, QueueIsEmptyException
import unittest


class TestQueue(unittest.TestCase):

    def test_queue(self):
        queue = Queue()

        for i in [1, 2, 3, 4, 5]:
            queue.enqueue(i)

        expected_data = [1, 2, 3, 4, 5]
        for index, data in enumerate(queue):
            self.assertEqual(data, expected_data[index])

        expected_data = [1, 2, 3, 4, 5]
        for index, data in enumerate(queue):
            self.assertEqual(queue.dequeue(), expected_data[index])

        with self.assertRaises(QueueIsEmptyException):
            queue.dequeue()
