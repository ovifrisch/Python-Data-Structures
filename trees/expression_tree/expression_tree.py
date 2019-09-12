"""Expression Tree"""



def get_valid_chars():
    """Returns the set of valid chars in an expression string"""
    lower = set(map(lambda x: chr(x), range(ord('a'), ord('z') + 1)))
    upper = set(map(lambda x: chr(x), range(ord('A'), ord('Z') + 1)))
    nums = set(map(lambda x: chr(x), range(ord('1'), ord('9') + 1)))
    ops = set(['*', '/', '-', '+', '&', '|', '!'])
    misc = set(['(', ')', '.', ' '])
    return lower.union(upper).union(nums).union(ops).union(misc)

class ExpressionTree:
    # pylint: disable=too-many-instance-attributes
    """ Expression tree for binary or boolean expressons"""


    class TreeNode:
        # pylint: disable=too-few-public-methods
        """ A node in the Expression Tree"""

        def __init__(self, left, right):
            self.left = left
            self.right = right


    class OperandNode(TreeNode):
        # pylint: disable=too-few-public-methods
        """An operand node in the Expression Tree"""

        def __init__(self, outer, operand, left=None, right=None):
            # pylint: disable=super-init-not-called
            outer.TreeNode.__init__(self, left, right)
            self.operand = operand

    class OperatorNode(TreeNode):
        # pylint: disable=too-few-public-methods
        """An operator node in the Expression Tree"""

        def __init__(self, outer, operator, left=None, right=None):
            # pylint: disable=super-init-not-called
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
        self.valid_fixes = ["infix", "prefix", "postfix"]
        self.valid_chars = get_valid_chars()
        self.expr_type = None
        self.root = None
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
        self.prec = ['*', '/', '+', '-', '!', '&', '|']


    def __init_tree(self, fix, expr):
        """Validates the expression string and if all is good, constructs the tree

        Args:
            fix: the format of expr
            expr: the expression string

        Raises:
            Invalid Expression: Raised when the expression given its fix is invalid
        """
        self.variables = set()
        self.__validate_fix(fix)
        self.__set_expr_type(expr)
        if sum(map(lambda x: x not in self.valid_chars, expr)) > 0:
            raise Exception("Invalid Expression")
        tokens = self.__tokenize(expr)
        for var in filter(lambda x: isinstance(x, str), tokens):
            self.variables.add(var)
        self.__construct(tokens, fix)

    def __is_op(self, token):
        return token in self.num_ops or token in self.bool_ops


    def __op(self, token):
        if token in self.num_ops:
            return self.num_ops[token]
        return self.bool_ops[token]


    def __tokenize(self, expression):
        """Tokenizes the expression into operands and operators

        Args:
            expr: A valid expression string with possibly whitespace

        Returns:
            A list of tokens
        """


        # pylint: disable=too-many-branches
        res = []
        expr_parts = expression.split() # split on whitespace
        for expr in expr_parts:
            curr_num = None
            curr_var = None
            for char in expr:
                if char in (')', '('):
                    if curr_num is not None:
                        res.append(float(curr_num))
                        curr_num = None

                    if curr_var is not None:
                        res.append(curr_var)
                        curr_var = None

                    res.append(char)
                    continue

                if self.__is_op(char):
                    if curr_num is not None:
                        res.append(float(curr_num))
                        curr_num = None

                    if curr_var is not None:
                        res.append(curr_var)
                        curr_var = None

                    res.append(char)

                elif (char.isdigit() or char == '.'):
                    if curr_num is None:
                        curr_num = char
                    else:
                        curr_num += char

                else:
                    if curr_var is None:
                        curr_var = char
                    else:
                        curr_var += char

            if curr_num is not None:
                res.append(float(curr_num))

            if curr_var is not None:
                res.append(curr_var)
        return res



    def evaluate(self):
        """Evaluates the expression

        Returns: A boolean in case of a Boolean Expression Tree, Float otherwise
        """

        if not self.root:
            raise Exception("Empty Expression")

        def helper(node):
            if not node:
                return None
            if isinstance(node, self.OperandNode):
                if (isinstance(node.operand, str) and node.operand in self.assignments):
                    return self.assignments[node.operand]
                return node.operand
            left = helper(node.left)
            right = helper(node.right)

            if not right:
                if isinstance(left, str):
                    return "(" + node.operator + " " + left + ")"
                return left

            if (isinstance(left, str) or isinstance(right, str)):
                return "(" + str(left) + " " + node.operator + " " + str(right) + ")"
            return self.__op(node.operator)(left, right)

        res = helper(self.root)
        if (isinstance(res, str) and res[0] == '('):
            res = res[1:-1]
        return res


    def __validate_fix(self, fix):
        if fix not in self.valid_fixes:
            raise Exception("Invalid fix")

    def __set_expr_type(self, expr):

        def op_in(ops):
            return map(lambda op: op in expr, ops)

        if (sum(op_in(self.num_ops)) > 0 and sum(op_in(self.bool_ops)) > 0):
            raise Exception("Invalid Expression")

        if sum(op_in(self.num_ops)) > 0:
            self.expr_type = "numeric"
        elif sum(op_in(self.bool_ops)) > 0:
            self.expr_type = "boolean"

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
        for key, val in assignments.items():
            if key not in self.variables:
                raise Exception("Nonexistent variable")

            if (self.expr_type == "numeric" and not isinstance(val, int)):
                raise Exception("Invalid value")

            if (self.expr_type == "boolean" and not isinstance(val, bool)):
                raise Exception("Invalid value")

        self.assignments = assignments


    def __construct(self, tokens, fix="infix"):

        def construct_prefix(tokens):
            """Constructs the expression tree from a prefix expression"""
            # pylint: disable=unused-argument
            def helper():
                nonlocal tokens
                if not tokens:
                    return None

                tok = tokens[0]
                tokens = tokens[1:]

                if self.__is_op(tok):
                    node = self.OperatorNode(self, tok)
                else:
                    node = self.OperandNode(self, tok)
                    return node # operand's cannot have children

                if not tokens:
                    raise Exception("Invalid Expression")

                node.left = helper()

                if not tokens:
                    if node.operator != "!":
                        raise Exception("Invalid Expression")
                    return node

                node.right = helper()

                return node

            return helper()


        if fix == "infix":
            self.root = construct_prefix(self.__infix2prefix(tokens))
        elif fix == "postfix":
            self.root = construct_prefix(self.__postfix2prefix(tokens))
        else: # prefix
            self.root = construct_prefix(tokens)


    def __infix2prefix(self, tokens):
        """Convert an infix expresion to prefix"""

        def flip_paren(char):
            if char == "(":
                return ")"
            if char == ')':
                return "("
            return char

        tokens.reverse()
        tokens = [flip_paren(x) for x in tokens]
        tokens = self.__infix2postfix(tokens)
        tokens.reverse()
        print(tokens)
        return tokens

    def __postfix2prefix(self, tokens):
        """Convert a postfix expression to prefix"""
        stack = []
        for token in tokens:
            if not self.__is_op(token):
                stack.append([token])
            else:
                new_top = [token] + stack[-2] + stack[-1]
                stack = stack[:-2]
                stack.append(new_top)
        return stack[0]


    def __infix2postfix(self, tokens):
        """Convert an infix expression to postfix"""
        stack = []
        res = []
        for token in tokens:
            if token == '(':
                stack.append('(')
            elif (not self.__is_op(token) and token != ')'):
                res.append(token)
            else:
                if self.__is_op(token):
                    if (not stack or stack[-1] == '('):
                        stack.append(token)
                    elif self.prec.index(token) < self.prec.index(stack[-1]):
                        stack.append(token)
                    else:
                        while (stack and stack[-1] != '(' and
                               self.prec.index(stack[-1]) < self.prec.index(token)):
                            res.append(stack.pop(-1))
                        stack.append(token)
                elif token == ")":
                    while stack[-1] != "(":
                        res.append(stack.pop(-1))
                    stack.pop(-1)
        while stack:
            top = stack.pop(-1)
            if top != '(':
                res.append(top)
        return res


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
            if not node:
                return ""

            if isinstance(node, self.OperandNode):
                return str(node.operand)

            left = inorder(node.left)
            right = inorder(node.right)

            return "(" + left + str(node.operator) + right + ")"

        def postorder(node):
            if not node:
                return ""

            if isinstance(node, self.OperandNode):
                return str(node.operand)

            left = postorder(node.left)
            right = postorder(node.right)
            return left + " " + right + " " + node.operator

        def preorder(node):
            if not node:
                return ""

            if isinstance(node, self.OperandNode):
                return str(node.operand)

            left = preorder(node.left)
            right = preorder(node.right)
            return node.operator + ' ' + left + ' ' + right

        if fix == "infix":
            return inorder(self.root)

        if fix == "postfix":
            return postorder(self.root)

        if fix == "prefix":
            return preorder(self.root)
