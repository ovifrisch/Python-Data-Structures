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


    def test_tokenize(self):
        expr = "(a+b  )+    (223*bogus)"
        res = self.tree.tokenize(expr)
        plus = self.tree.num_ops['+']
        times = self.tree.num_ops['*']
        self.assertEqual(res, ['(', 'a', '+', 'b', ')', '+', '(', 223, '*', 'bogus', ')'])

if __name__ == "__main__":
    unittest.main()