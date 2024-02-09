from data_structures.collections import Stack, StackIsEmptyException
import unittest


class TestStack(unittest.TestCase):

    def test_stack(self):
        stack = Stack()

        for i in [5, 4, 3, 2, 1]:
            stack.push(i)

        expected_data = [1, 2, 3, 4, 5]
        for index, data in enumerate(stack):
            self.assertEqual(data, expected_data[index])

        expected_data = [1, 2, 3, 4, 5]
        for index, data in enumerate(stack):
            self.assertEqual(stack.get_top(), expected_data[index])
            self.assertEqual(stack.pop(), expected_data[index])

        with self.assertRaises(StackIsEmptyException):
            stack.pop()
