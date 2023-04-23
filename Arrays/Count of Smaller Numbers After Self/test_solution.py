import unittest  # importing the unittest module for unit testing
from solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()  # creating an instance of the Solution class for testing

    def test_empty_input(self):
        # testing with empty input
        nums = []
        expected_counts = []
        self.assertEqual(self.solution.countSmaller(nums), expected_counts)

    def test_single_input(self):
        # testing with a single input
        nums = [5]
        expected_counts = [0]
        self.assertEqual(self.solution.countSmaller(nums), expected_counts)

    def test_multiple_input(self):
        # testing with multiple inputs
        nums = [5, 2, 6, 1]
        expected_counts = [1, 0, 1, 0]
        self.assertEqual(self.solution.countSmaller(nums), expected_counts)

    def test_duplicate_input(self):
        # testing with duplicate inputs
        nums = [1, 2, 2, 3]
        expected_counts = [0, 0, 0, 2]
        self.assertEqual(self.solution.countSmaller(nums), expected_counts)


if __name__ == '__main__':
    unittest.main()  # running the test suite using unittest module
