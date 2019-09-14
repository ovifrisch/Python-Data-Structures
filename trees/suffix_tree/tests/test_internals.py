import unittest
import sys
sys.path.append("../.")
from suffix_tree import SuffixTree


class TestInternals(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestInternals, self).__init__(*args, **kwargs)
        self.tree = SuffixTree()

    def test_suffix_gen(self):
        res = self.tree.get_suffixes(["abc", "xyz"])
        self.assertEqual(res, ['$', '@', 'c$', 'z@', 'bc$', 'yz@', 'abc$', 'xyz@'], res)


    def test_get_suffixes_from_tree(self):
        strings = ["ab", "ab", "c"]
        self.tree.add_strings(strings)
        res = self.tree.get_suffixes_from_tree()
        self.assertEqual(set(res), set(["$", "b$", "ab$", "@", "b@", "ab@", "%", "c%"]))


if __name__ == "__main__":
    unittest.main()
