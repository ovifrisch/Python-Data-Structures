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

def test():
    raise ValueError

class TestPrefixEval(unittest.TestCase):
    """Tests infix evaluation"""

    def __init__(self, *args, **kwargs):
        super(TestPrefixEval, self).__init__(*args, **kwargs)
        self.tree = ExpressionTree()


    def get_res(self, expr, assignments={}):
        self.tree.set_expr(expr, fix="prefix")
        self.tree.assign_vars(assignments)
        return self.tree.evaluate()

    def test_empty(self):
        self.tree.set_expr(expr="", fix="infix")
        with self.assertRaises(Exception) as context:
            self.tree.evaluate()
        self.assertTrue('Empty Expression' in str(context.exception))


    def test1(self):
        expr = "+ 1 12"
        res = self.get_res(expr)
        self.assertEqual(res, 13)


    def test2(self):
        expr = "**2 3 4"
        res = self.get_res(expr)
        self.assertEqual(res, 24)

    def test3(self):
        expr = "/+3 9 3"
        res = self.get_res(expr)
        self.assertEqual(res, 4)




if __name__ == "__main__":
    unittest.main()