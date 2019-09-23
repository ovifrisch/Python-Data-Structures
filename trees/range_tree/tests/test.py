import unittest
import numpy as np
import sys
sys.path.append("./../")
from range_tree import RangeTree
import random

class TestRangeTree(unittest.TestCase):

    """
    """

    def __init(self, *args, **kwargs):
        super(TestIntervalTree, self).__init__(*args, **kwargs)
        self.tree = RangeTree()


    def contained_in(self, intervals, range_):
        result = np.ones((1, range_[0].shape[0]))
        for interval in intervals:
            good = True
            for i in range(interval.shape[0]):
                if (not(interval[i] >= range_[0][i] and interval[i] <= range_[1][i])):
                    good = False
                    break
            if good:
                result = np.vstack([result, interval])
        return result[1:]


    def random_test_gen(self, num_intervals, num_dims, min_range, max_range):
        """return a list of num_intervals random intervals and a random range
           such that each interval and the range is between the allowed range.
        """

        intervals = np.zeros((num_intervals, num_dims))
        minimum = np.random.randint(min_range, high=max_range + 1, size=num_dims)
        maximum = np.zeros((num_dims,))
        for i in range(num_dims):
            maximum[i] = random.randint(minimum[i], max_range)

        for i in range(num_intervals):
            interval = np.zeros((1, num_dims))
            for j in range(num_dims):
                interval[0, j] = random.randint(min_range, max_range)
            intervals[i, :] = interval

        return intervals, (minimum, maximum)

    # def test1(self):
    #     data = np.array([[5, 54, 17], [2, 4, 9]])
    #     range_ = (np.array([1, 2, 4]), np.array([10, 53, 100]))
    #     t = RangeTree(3, data)
    #     res = t.get_points(range_)
    #     self.assertTrue(np.array_equal(res, self.contained_in(data, range_)))


    # def test2(self):
    #     dims = 3
    #     data, range_ = self.random_test_gen(1000, dims, 1, 10)
    #     # range_ = (np.array([1, 1, 1]), np.array([8, 8, 8]))
    #     t = RangeTree(dims, data)
    #     res = t.get_points(range_)
    #     print(res.shape)
    #     res = set([tuple(row) for row in res])
    #     truth = set([tuple(row) for row in self.contained_in(data, range_)])
    #     self.assertTrue(np.array_equal(res, truth))


    def test_contains(self):
        data = np.array([[5, 54, 17], [2, 4, 9]])
        t = RangeTree(3, data)
        self.assertTrue(not t.contains(np.array([5, 54, 7])))


if __name__ == "__main__":
    unittest.main()