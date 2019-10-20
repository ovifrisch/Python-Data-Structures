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

    def __init__(self, data=None):
        """Inits the RangeTree

        Args:
            num_dimensions (optional): the number of dimensions for the data
            data (optional): numpy matrix of data points 

        """
        self.root = None
        self.size = 0
        if len(data.shape) == 1:
            self.dims = data.shape[0]
        else:
            self.dims = data.shape[1]
        np.apply_along_axis(self.add, axis=1, arr=data)
            

    def add(self, data):
        """
        Adds data to the tree

        Args:
            data: np array (1 row and self.dims cols)
        """
        def add_helper(data, dim, node):
            # base case
            if dim == self.dims:
                return None

            if not node:
                tree_node = TreeNode(data, dim)
                tree_node.inner = add_helper(data, dim + 1, None)
                return tree_node

            # insert into the inner node because we are adding to the outer's subtree
            node.inner = add_helper(data, dim + 1, node.inner)

            # reached the bottom, make sure that parent node contains max value of left subtree
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

            # node has at least 1 child, continue binary search
            else:
                if (data[dim] < node.val[dim]):
                    node.left = add_helper(data, dim, node.left)
                else:
                    node.right = add_helper(data, dim, node.right)

            return node

        self.root = add_helper(data, 0, self.root)
        self.size += 1

    def remove(self, data):
        """
        Removes data from the tree

        Args:
            data: np array (1 row and self.dims cols)

        Returns:
            data if it exists

        Raises:
            Element does not exist, if data does not exist
        """
        if self.contains(data):
            raise Exception("Element does not exist")




    def contains(self, data):
        """
        just do a binary search on the first level
        """

        def helper(node):
            if not node:
                return False

            elif np.array_equal(node.val, data):
                return True

            elif node.val[0] == data[0]:
                return helper(node.left) or helper(node.right)

            elif (data[0] < node.val[0]):
                return helper(node.left)

            return helper(node.right)

        return helper(self.root)



    def get_points(self, query_range):
        """Get all the points that lie in the given range

        Args:
            range: a tuple of ndarrays indicating the query range

        Returns:
            A list of points falling in the given range

        Raises:
            Wrong Dimension: range dimension is wrong
        """

        if (query_range[0].shape[0] != self.dims or query_range[1].shape[0] != self.dims):
            raise Exception("Wrong Dimension")

        subtrees = []

        def max_traverse(node):
            maximum = query_range[1][node.dim]
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
            minimum = query_range[0][node.dim]
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

            minimum = query_range[0][node.dim]
            maximum = query_range[1][node.dim]
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
    t = RangeTree(data=data)
    res = t.get_points(range_)
    print(res)









