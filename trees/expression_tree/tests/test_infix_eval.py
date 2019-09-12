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


class TestInfixEval(unittest.TestCase):
    """Tests infix evaluation"""

    def __init__(self, *args, **kwargs):
        super(TestInfixEval, self).__init__(*args, **kwargs)
        self.tree = ExpressionTree()


    def get_res(self, expr, assignments={}):
        self.tree.set_expr(expr, fix="infix")
        self.tree.assign_vars(assignments)
        return self.tree.evaluate()

    def test_empty(self):
        self.tree.set_expr(expr_str="", fix="infix")
        with self.assertRaises(Exception) as context:
            self.tree.evaluate()
        self.assertTrue('Empty Expression' in str(context.exception))


    # def test1(self):
    #     expr = "a + b"
    #     res = self.get_res(expr)
    #     self.assertEqual(res, expr)

    # def test2(self):
    #     expr = "a + b"
    #     assigns = {'a': 3, 'b':19}
    #     result = self.get_res(expr, assigns)
    #     self.assertEqual(result, 22)

    # def test3(self):
    #     expr = "+"
    #     with self.assertRaises(Exception) as context:
    #         self.tree.set_expr(expr)
    #     self.assertTrue('Invalid Expression' in str(context.exception))

    # def test4(self):
    #     expr = "((water + eggs) * bacon) / sausage"
    #     res = self.get_res(expr)
    #     self.assertEqual(res, expr)

    # def test5(self):
    #     expr = "((water + eggs) * bacon) / sausage"
    #     assigns = {
    #         'water': 7,
    #         'eggs': 3,
    #         'bacon': 3,
    #         'sausage': 2
    #     }
    #     res = self.get_res(expr)
    #     self.assertEqual(res, 15)


    # def test6(self):
    #     expr = "(3 -* 7) + 2"
    #     with self.assertRaises(Exception) as context:
    #         self.tree.set_expr(expr)
    #     self.assertTrue('Invalid Expression' in str(context.exception))

    # def test7(self):
    #     expr = "((A & B) | C) & !D"
    #     assigns = {
    #         'A': True,
    #         'B': False,
    #         'C': True,
    #         'D': False
    #     }
    #     res = self.get_res(expr, assigns)
    #     self.assertEqual(res, True)


    def test8(self):
        expr = "2 + 3 & True"
        with self.assertRaises(Exception) as context:
            self.tree.set_expr(expr)
        self.assertTrue('Cannot combine boolean and numeric operators' in str(context.exception))




if __name__ == "__main__":
    unittest.main()