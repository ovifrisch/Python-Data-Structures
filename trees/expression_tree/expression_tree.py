import re

"""Expression Tree"""

class ExpressionTree:
    """ Expression tree for binary or boolean expressons"""


    class TreeNode:
        """ A node in the Expression Tree"""

        def __init__(self, left, right):
            self.left = left
            self.right = right


    class OperandNode(TreeNode):
        """An operand node in the Expression Tree"""

        def __init__(self, outer, operand, left=None, right=None):
            outer.TreeNode.__init__(self, left, right)
            self.operand = operand

    class OperatorNode(TreeNode):
        """An operator node in the Expression Tree"""

        def __init__(self, outer, operator, left=None, right=None):
            outer.TreeNode.__init__(self, left, right)
            self.operator = operator

    def __init__(self, expr="", fix="infix"):
        """Inits ExpressionTree.

        Args:
            expr (optional): A string representing the expression
            fix: (optional)
                Specifies the format of expr: 'infix' | 'prefix' | 'postfix'
        Raises:
            Invalid fix: The fix paramter was provided but was not one of the allowed values.
            Invalid expr: The expr parameter is invalid
        """
        self.num_ops = {
                "*": lambda x, y: x*y,
                "/": lambda x, y: x/y,
                "+": lambda x, y: x+y,
                "-": lambda x, y: x-y
            }

        self.bool_ops = {
            "&": lambda x, y: x and y,
            "|": lambda x, y: x or y,
            "!": lambda x: not x
        }
        self.assignments = {}
        self.__init_tree(fix, expr)


    def __init_tree(self, fix, expr):
        self.__validate_fix(fix)
        self.__set_expr_type(expr)
        tokens = self.__tokenize(expr)
        self.variables = set()
        for var in filter(lambda x: isinstance(x, str), tokens):
            self.variables.add(var)
        self.__construct(tokens, fix)

    def __is_op(self, token):
        return token in self.num_ops or token in self.bool_ops


    def __op(self, token):
        if token in self.num_ops:
            return self.num_ops[token]
        return self.bool_ops[token]


    def __tokenize(self, expr):
        """Tokenizes the expression into operands and operators

        Args:
            expr: A valid expression string with possibly whitespace

        Returns:
            A list of tokens
        """
        res = []
        expr_parts = expr.split() # split on whitespace
        for expr in expr_parts:
            curr_num = None
            curr_var = None
            for i in range(len(expr)):

                if (expr[i] == '(' or expr[i] == ')'):
                    if (curr_num is not None):
                        res.append(int(curr_num))
                        curr_num = None

                    if (curr_var is not None):
                        res.append(curr_var)
                        curr_var = None

                    res.append(expr[i])
                    continue

                if (self.__is_op(expr[i])):
                    if (curr_num is not None):
                        res.append(int(curr_num))
                        curr_num = None

                    if (curr_var is not None):
                        res.append(curr_var)
                        curr_var = None

                    res.append(expr[i])

                elif (expr[i].isdigit()):
                    if (curr_num is None):
                        curr_num = expr[i]
                    else:
                        curr_num += expr[i]

                else:
                    if (curr_var is None):
                        curr_var = expr[i]
                    else:
                        curr_var += expr[i]

            if (curr_num is not None):
                res.append(int(curr_num))

            if (curr_var is not None):
                res.append(curr_var)
        return res



    def evaluate(self):
        """Evaluates the expression

        Returns: A boolean in case of a Boolean Expression Tree, Float otherwise
        """

        if (not self.root):
            raise Exception("Empty Expression")

        def helper(node):
            if (isinstance(node, self.OperandNode)):
                if (isinstance(node.operand, str) and node.operand in self.assignments):
                    return self.assignments[node.operand]
                return node.operand
            else:
                left = helper(node.left)
                right = helper(node.right)

                if (isinstance(left, str) or isinstance(right, str)):
                    return str(left) + node.operator + str(right)
                else:
                    return self.__op(node.operator)(left, right)

        return helper(self.root)


    def __validate_fix(self, fix):
        if (fix != "infix" and fix != "postfix" and fix != "prefix"):
            raise Exception("Invalid fix")

    def __set_expr_type(self, expr):

        def xx(ops):
            return map(lambda op: op in expr, ops)

        if (sum(xx(self.num_ops)) > 0 and sum(xx(self.bool_ops)) > 0):
            raise Exception("Cannot combine boolean and numeric operators")

        if (sum(xx(self.num_ops)) > 0):
            self.expr_type = "numeric"
        elif (sum(xx(self.bool_ops)) > 0):
            self.expr_type = "boolean"
        else:
            self.expr_type = None

    def set_expr(self, expr, fix="infix"):
        """Sets the expression to expr"""
        self.__init_tree(fix, expr)

    def assign_vars(self, assignments):
        """Assigns values to the operands

        Args:
            assignments: A dict mapping variable names to their values.

        Raises:
            Nonexistent variable: One of the keys in assignments is not a variable.
            Invalid value: One of the values is invalid
        """
        for k, v in assignments.items():
            if (k not in self.variables):
                raise Exception("Nonexistent variable")

            if (self.expr_type == "numeric" and not isinstance(v, int)):
                raise Exception("Invalid value")

            if (self.expr_type == "boolean" and not isinstance(v, bool)):
                raise Exception("Invalid value")

        self.assignments = assignments


    def __construct(self, tokens, fix="infix"):

        def construct_prefix(tokens):
            """Constructs the expression tree from a prefix expression"""

            def helper():
                nonlocal tokens
                if (not tokens):
                    return None

                tok = tokens[0]
                tokens = tokens[1:]

                if (self.__is_op(tok)):
                    node = self.OperatorNode(self, tok)
                else:
                    node = self.OperandNode(self, tok)
                    return node # operand's cannot have children

                node.left = helper()

                if (not tokens):
                    return node

                node.right = helper()

                return node

            return helper()


        if fix == "infix":
            self.root = construct_postfix(self.__infix2prefix(tokens))
        elif fix == "postfix":
            self.root = construct_postfix(self.__postfix2prefix(tokens))
        else: # postfix
            self.root = construct_postfix(tokens)


    def __infix2prefix(tokens):
        """Convert an infix expresion to prefix"""
        pass

    def __postfix2prefix(tokens):
        """Convert a postfix expression to prefix"""
        pass


    def to_str(self, fix="infix"):
        """Converts the tree to a string

        Args:
            fix: (optional, default: 'infix')
                Specifies the format of the returned string: 'infix' | 'prefix' | 'postfix'

        Returns:
            A string representing the expression tree
        Raises:
            Invalid fix: The fix paramter was provided but was not one of the allowed values.
        """

        def inorder(node):
            if (not node):
                return ""

            if (isinstance(node, self.OperandNode)):
                return str(node.operand)

            left = inorder(node.left)
            right = inorder(node.right)

            return "(" + left + str(node.operator) + right + ")"

        def postorder(node):
            if (not node):
                return ""

            if (isinstance(node, self.OperandNode)):
                return str(node.operand)

            left = postorder(node.left)
            right = postorder(node.right)
            return left + " " + right + " " + node.operator

        def preorder(node):
            if (not node):
                return ""

            if (isinstance(node, self.OperandNode)):
                return str(node.operand)

            left = preorder(node.left)
            right = preorder(node.right)
            return node.operator + ' ' + left + ' ' + right

        if (fix == "infix"):
            return inorder(self.root)

        elif (fix == "postfix"):
            return postorder(self.root)

        elif (fix == "prefix"):
            return preorder(self.root)



if __name__ == "__main__":
    e = ExpressionTree("**2 3 4", "prefix")
    # e.assign_vars({
    #     'a':7,
    #     'b':3,
    #     'c':98
    # })
    print(e.to_str("prefix"))


