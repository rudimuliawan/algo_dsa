from algorithm.sorting import insertion_sort, selection_sort
import unittest


def is_sorted(data):
    n = len(data)
    for i in range(1, n):
        if data[i] < data[i-1]:
            return False

    return True


class TestSorting(unittest.TestCase):

    def test_insertion_sort(self):
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        insertion_sort(data)
        self.assertTrue(is_sorted(data))

        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        insertion_sort(data)
        self.assertTrue(is_sorted(data))

        data = [3, 7, 2, 4, 6, 5, 1, 10, 9, 8]
        insertion_sort(data)
        self.assertTrue(is_sorted(data))

    def test_selection_sort(self):
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        selection_sort(data)
        self.assertTrue(is_sorted(data))

        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        selection_sort(data)
        self.assertTrue(is_sorted(data))

        data = [3, 7, 2, 4, 6, 5, 1, 10, 9, 8]
        selection_sort(data)
        self.assertTrue(is_sorted(data))
