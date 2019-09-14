import numpy as np


class TreeNode:

    def __init__(self, val, dim=0, left=None, right=None, inner=None):
        self.val = val
        self.dim = dim
        self.left = left
        self.right = right
        self.inner = inner

class RangeTree:
    """Range Tree Implementation

    Binary decision rule: >= nodes go right
    """

    def __init__(self, num_dimensions=1, data=None):
        """Inits the RangeTree

        Args:
            num_dimensions (optional): the number of dimensions for the data
            data (optional): numpy matrix of data points 

        """
        if (not isinstance(num_dimensions, int) and num_dimensions <= 1):
            raise Exception("num_dimensions must be an Int")
        self.dims = num_dimensions
        self.root = None
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise Exception("data must be a numpy array")
            if (len(data.shape) == 1 and self.dims > 1):
                raise Exception("Inconsistent dimensions")
            if (len(data.shape) == 2 and self.dims != data.shape[1]):
                raise Exception("Inconsistent dimensions")

            # add each row to the tree
            np.apply_along_axis(self.add, axis=1, arr=data)

    def add(self, data):
        """
        [2, 4, 9]
        [5, 54, 17]
        """
        def add_helper(data, dim, tree):
            if dim == self.dims:
                return None

            # empty tree, insert here and recursively insert on empty inner tree
            if tree is None:
                tree = TreeNode(data, dim)
                tree.inner = add_helper(data, dim + 1, None)
                return tree


            def binary_search(node):
                if not node:
                    tree_node = TreeNode(data, dim)
                    tree_node.inner = add_helper(data, dim + 1, None)
                    return tree_node

                # insert into the inner node because we are adding to the outer's subtree
                node.inner = add_helper(data, dim + 1, node.inner)

                if (not node.left and not node.right):
                    if data[dim] <= node.val[dim]:
                        node.left = TreeNode(data, dim)
                        node.right = TreeNode(node.val, dim)
                        node.left.inner = add_helper(data, dim + 1, None)
                        node.right.inner = add_helper(node.val, dim + 1, None)
                        node.val = data
                    else:
                        node.left = TreeNode(node.val, dim)
                        node.right = TreeNode(data, dim)
                        node.left.inner = add_helper(node.val, dim + 1, None)
                        node.right.inner = add_helper(data, dim + 1, None)

                else:
                    if (data[dim] < node.val[dim]):
                        node.left = binary_search(node.left)
                    else:
                        node.right = binary_search(node.right)

                return node

            tree = binary_search(tree)
            return tree

        self.root = add_helper(data, 0, self.root)

    def remove(self, data):
        pass



    def get_points(self, range_):
        """Get all the points that lie in the given range

        Args:
            range: a tuple of ndarrays indicating the query range

        Returns:
            A list of points falling in the given range

        Raises:
            Wrong Dimension: range dimension is wrong
        """

        # validation code

        subtrees = []

        def max_traverse(node):
            maximum = range_[1][node.dim]
            dim_val = node.val[node.dim]
            bottom = node.dim == self.dims - 1

            if not node:
                return

            if (not node.left and not node.right):
                if dim_val <= maximum:
                    if bottom:
                        subtrees.append(node)
                    else:
                        traverse(node.inner)
                return

            if dim_val <= maximum:
                if bottom:
                    subtrees.append(node.left)
                else:
                    if node.left:
                        traverse(node.left.inner)
                max_traverse(node.right)

            else:
                max_traverse(node.left)

        def min_traverse(node):
            minimum = range_[0][node.dim]
            dim_val = node.val[node.dim]
            bottom = node.dim == self.dims - 1

            if not node:
                return

            if (not node.left and not node.right):
                if (dim_val >= minimum):
                    if (bottom):
                        subtrees.append(node)
                    else:
                        traverse(node.inner)
                return

            if dim_val >= minimum:
                if bottom:
                    subtrees.append(node.right)
                else:
                    if node.right:
                        traverse(node.right.inner)
                min_traverse(node.left)
            else:
                min_traverse(node.right)

        def traverse(node):
            if not node:
                return

            minimum = range_[0][node.dim]
            maximum = range_[1][node.dim]
            dim_val = node.val[node.dim]


            if (not node.left and not node.right):
                if (dim_val >= minimum and dim_val <= maximum):
                    if (node.dim == self.dims - 1):
                        subtrees.append(node)
                    else:
                        traverse(node.inner)
                return

            if (minimum < dim_val and maximum < dim_val):
                traverse(node.left)
            elif (minimum > dim_val and maximum > dim_val):
                traverse(node.right)
            elif (minimum < dim_val and maximum > dim_val):
                min_traverse(node.left)
                max_traverse(node.right)
            elif (minimum == dim_val and maximum == dim_val):
                traverse(node.right)
                traverse(node.left)
            elif (minimum == dim_val):
                max_traverse(node.right)
                traverse(node.left)
            elif (maximum == dim_val):
                min_traverse(node.left)
                traverse(node.right)

        traverse(self.root)

        """go over all subtrees and add the leaves"""
        result = np.zeros((1, self.dims))

        def dfs(node):
            nonlocal result
            if not node:
                return

            if (not node.left and not node.right): #leaf
                result = np.vstack([result, node.val.reshape((1, self.dims))])
            dfs(node.left)
            dfs(node.right)

        for tree in subtrees:
            dfs(tree)

        return result[1:]


if __name__ == "__main__":
    data = np.array([[5, 54, 17], [2, 4, 9]])
    range_ = (np.array([1, 2, 4]), np.array([10, 53, 100]))
    t = RangeTree(3, data)
    res = t.get_points(range_)
    print(res)









