import numpy as np


class TreeNode:

    def __init__(self, val, dim, left=None, right=None, inner=None):
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
        if data is None:
            self.root = None
        else:
            if not isinstance(data, np.ndarray):
                raise Exception("data must be a numpy array")
            if (len(data.shape) == 1 and self.dims > 1):
                raise Exception("Inconsistent dimensions")
            if (len(data.shape) == 2 and self.dims != data.shape[1]):
                raise Exception("Inconsistent dimensions")

            # add each row to the tree
            np.apply_along_axis(self.add, axis=1, arr=data)

    def add(self, data):
        pass

    def remove(self, data):
        pass



    def get_points1d(self, minimum, maximum):

        subtrees = []
        result = []

        def min_traverse(node):
            if not node:
                return

            if minimum > node.val:
                min_traverse(node.right)
            else:
                subtrees.append(node.right)
                min_traverse(node.left)

        def max_traverse(node):
            if not node:
                return

            if (maximum < node.val):
                max_traverse(node.left)
            else:
                subtrees.append(node.left)
                max_traverse(node.right)

        def traverse(node):
            if not node:
                return

            if (minimum < node.val and maximum > node.val):
                min_traverse(node.left)
                max_traverse(node.right)
            elif (minimum < node.val and maximum < node.val):
                traverse(node.left)
            elif (minimum > node.val and maximum > node.val):
                traverse(node.right)
            elif (minimum == node.val and maximum == node.val):
                result.append(node.val)
                traverse(node.right)
            elif (minimum == node.val):
                result.append(node.val)
                max_traverse(node.right)
            elif (maximum == node.val):
                min_traverse(node.left)


        def bfs(node):
            if not node:
                return

            bfs(node.left)
            result.append(node.val)
            bfs(node.right)


        traverse(self.root)
        for subtree in subtrees:
            dfs(subtree)

        return sorted(result)





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

        result = []

        def helper(node):

            if not node:
                return

            left_bound = range_[0][node.dim]
            right_bound = range_[1][node.dim]
            if (left_bound > node.val):
                helper(node.right)
            elif (right_bound < node.val):
                helper(node.left)




if __name__ == "__main__":
    t = RangeTree(num_dimensions=3, data=np.array([[1, 2, 3], [4, 5, 6]]))








