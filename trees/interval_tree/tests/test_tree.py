import unittest
import sys
sys.path.append('./../')
from interval_tree import IntervalTree
import numpy

class TestIntervalTree(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestIntervalTree, self).__init__(*args, **kwargs)
        self.tree = IntervalTree()

    def get_int(min, max):
        return (np.array(min), np.array(max))

    def test_is_contained1(self):
        self.tree.add([self.get_int([1], [5])])
        res = self.tree.is_contained(self.get_int([2, 4]))
        self.assertEqual(res, True)

    def test_is_contained2(self):
        self.tree.add([self.get_int([1], [5])])
        res = self.tree.is_contained(self.get_int([2, 8]))
        self.assertEqual(res, False)

    def test_is_contained3(self):
        self.tree.add([self.get_int([1], [5])])
        res = self.tree.is_contained(self.get_int([2, 8]), "partial")
        self.assertEqual(res, True)

    def test_is_contained4(self):
        self.tree.add([self.get_int([1], [5])])
        res = self.tree.is_contained(self.get_int([8, 10]))
        self.assertEqual(res, False)

    def test_is_contained5(self):
        self.tree.add([self.get_int([1, 1], [8, 9])])
        res = self.tree.is_contained(self.get_int([3, 3], [8, 8]))
        self.assertEqual(res, True)

    def test_overlap1(self):
        self.tree.add([self.get_int([1], [10]), self.get_int([5], [15])])
        res = self.tree.is_overlapping()
        self.assertEqual(res, True)

    def test_overlap2(self):
        self.tree.add([self.get_int([1], [10]), self.get_int([12], [15])])
        res = self.tree.is_overlapping()
        self.assertEqual(res, False)

    def test_remove2(self):
        self.tree.add([self.get_int([1], [10]), self.get_int([12], [19])])
        self.tree.remove_interval(self.get_int([12], [19]))
        res = self.tree.is_contained(self.get_int([14, 18]))
        self.assertEqual(res, False)













if __name__ == "__main__":
    unittest.main()