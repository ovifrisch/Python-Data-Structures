import unittest
import sys
sys.path.append("../.")
from suffix_tree import SuffixTree


class TestSuffixTree(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSuffixTree, self).__init__(*args, **kwargs)
        self.tree = SuffixTree()

    def test_get_strings(self):
        strings = ["banana, heater, healer", "barns", "flag", ""]
        self.tree.add_strings(strings)
        res = self.tree.get_strings()
        self.assertEqual(set(strings), set(res))


    def test_add_strings1(self):
        strings = ["banana", "heater", "healer", "barns", "flag", ""]
        self.tree.add_strings(strings)
        strings = ["a", "b", "c", "d", "e"]
        with self.assertRaises(Exception) as context:
            self.tree.add_strings(strings)
        self.assertTrue('Tree at Capacity' in str(context.exception))


    def test_add_strings2(self):
        strings = ["banana", "x", "yx#x", "sss^"]
        with self.assertRaises(Exception) as context:
            self.tree.add_strings(strings)
        self.assertTrue('Illegal Character' in str(context.exception))

    # def test_longest_common_substring1(self):
    #     strings = ["xabaxa", "ghabaxi"]
    #     self.tree.add_strings(strings)
    #     res = self.tree.longest_common_substring()
    #     self.assertEqual(res, "abax")

    # def test_longest_common_substring2(self):
    #     strings = ["bad_input"]
    #     self.tree.add_strings(strings)
    #     with self.assertRaises(Exception) as context:
    #         self.tree.longest_common_substring()
    #     self.assertTrue('Not Enough Strings' in str(context.exception))

    # def test_longest_common_substring3(self):
    #     self.tree.add_strings(["same_string, diff_string"])
    #     self.tree.add_strings(["same_string"])
    #     res = self.tree.longest_common_substring(["same_string", "same_string"])
    #     self.assertEqual("res", "same_string")

    # def test_longest_common_substring4(self):
    #     strings = ["abc", "def", "ghi"]
    #     self.add_strings(strings)
    #     res = self.tree.longest_common_substring()
    #     self.assertEqual(res, "")


    # def test_longest_repeated_substring1(self):
    #     strings = ["abab"]
    #     self.add_strings(strings)
    #     res = self.tree.longest_repeated_substring("abab")
    #     self.assertEqual(res, "ab")

    # def test_longest_repeated_substring2(self):
    #     strings = ["xxabcdabcdlp", "xoxoxoxo"]
    #     self.add_strings(strings)
    #     res = self.tree.longest_repeated_substring()
    #     self.assertEqual(res, ["abcd", "xoxo"])

    # def test_longest_repeated_substring3(self):
    #     strings = ["abcdef", "fedcba"]
    #     self.add_strings(strings)
    #     res = self.tree.longest_repeated_substring()
    #     self.assertEqual(res, ["a", "f"])


    # def test_longest_palindrome1(self):
    #     strings = ["mom", "dad", "sis", "bro"]
    #     self.add_strings(strings)
    #     res = self.tree.longest_palindrome()
    #     self.assertEqual(res, ["mom", "dad", "sis", "b"])

    # def test_longest_palindrome2(self):
    #     strings = ["xyzyaayz"]
    #     self.add_strings(strings)
    #     res = self.tree.longest_palindrome()
    #     self.assertEqual(res, ["zyaayz"])

    # def test_longest_palindrome3(self):
    #     strings = ["", "", "aaabbbccbbbaa"]
    #     self.add_strings(strings)
    #     res = self.tree.longest_palindrome()
    #     self.assertEqual(res, ["", "", "aabbbccbbbaa"])






if __name__ == "__main__":
    unittest.main()