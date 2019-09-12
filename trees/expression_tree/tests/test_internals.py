import unittest
import sys
sys.path.append("../.")
from expression_tree import ExpressionTree

"""
.assertEqual(a, b)  a == b
.assertTrue(x)  bool(x) is True
.assertFalse(x) bool(x) is False
.assertIs(a, b) a is b
.assertIsNone(x)    x is None
.assertIn(a, b) a in b
.assertIsInstance(a, b) isinstance(a, b)
"""

class TestInternals(unittest.TestCase):
    """Tests infix evaluation"""

    def __init__(self, *args, **kwargs):
        super(TestInternals, self).__init__(*args, **kwargs)
        self.tree = ExpressionTree()


    # def test_tokenize(self):
    #     expr = "(a+b  )+    (223*bogus)"
    #     res = self.tree.tokenize(expr)
    #     plus = self.tree.num_ops['+']
    #     times = self.tree.num_ops['*']
    #     self.assertEqual(res, ['(', 'a', '+', 'b', ')', '+', '(', 223, '*', 'bogus', ')'])


    # def test_inf2post1(self):
    #     infix = ['2', '+', '3']
    #     res = self.tree.infix2postfix(infix)
    #     self.assertEqual(res, ['2', '3', '+'])

    # def test_inf2post2(self):
    #     infix = "((2+3)*5)*2"
    #     infix = [x for x in infix]
    #     res = self.tree.infix2postfix(infix)
    #     self.assertEqual(res, [x for x in "23+5*2*"])

    # def test_inf2post3(self):
    #     infix = [x for x in "x&y|z"]
    #     res = self.tree.infix2postfix(infix)
    #     self.assertEqual(res, [x for x in "xy&z|"])

    # def test_inf2post4(self):
    #     infix = [x for x in "(2+7-2)*((8+4)/2)"]
    #     res = self.tree.infix2postfix(infix)
    #     self.assertEqual(res, [x for x in "27+2-84+2/*"])


    # def test_inf2pref1(self):
    #     infix = "((2+3)*5)*2"
    #     infix = [x for x in infix]
    #     res = self.tree.infix2prefix(infix)
    #     self.assertEqual(res, [x for x in "**+2352"])


    def test_post2pref(self):
        postfix = [x for x in "23+"]
        res = self.tree.postfix2prefix(postfix)
        self.assertEqual(res, [x for x in "+23"])




if __name__ == "__main__":
    unittest.main()