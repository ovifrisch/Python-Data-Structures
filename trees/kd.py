import numpy as np
import random
"""
K dimensional Tree
"""
class KDTree:

	class Node:
		def __init__(self, point, dim, left=None, right=None):
			self.point = point
			self.dim = dim
			self.left = left
			self.right = right

	"""
	points: a 2D numpy array.
	each row is a point
	"""
	def __init__(self, points=None):
		if (points is None):
			self.size = 0
			self.root = None
			self.num_dims = None
			return

		if (points.shape[1] > 0):
			points = np.unique(points, axis=0)
		self.num_dims = points.shape[1]
		self.root = self.make_kd(points, dim=0)
		self.size = points.shape[0]


	def next_dim(self, dim):
		dim += 1
		if (dim == self.num_dims):
			dim = 0
		return dim

	"""
	Construct a kd tree from the given points

	points less than or equal to median of dimension go left
	greater than goes right
	"""
	def make_kd(self, points, dim):
		if (points.shape[0] == 0 or points.shape[1] == 0):
			return None

		sorted_idxs = np.argsort(points[:, dim])
		median_idx = sorted_idxs.shape[0] // 2
		median_val = points[sorted_idxs[median_idx], dim]


		# find the minimum distance to the right that gives a diff num
		right_idx = median_idx
		while (right_idx < sorted_idxs.shape[0] - 1 and points[sorted_idxs[right_idx+1], dim] == median_val):
			right_idx += 1



		median = points[sorted_idxs[right_idx], :]
		left = points[sorted_idxs[:right_idx], :]
		right = points[sorted_idxs[right_idx + 1:], :]

		next_dim = self.next_dim(dim)

		left_child = self.make_kd(left, next_dim)
		right_child = self.make_kd(right, next_dim)
		return self.Node(median, dim, left_child, right_child)


	def insert(self, point):
		if (self.num_dims is None):
			self.num_dims = point.shape[0]
		if (self.contains(point)):
			raise Exception("point already exists")

		# dim and root.dim should always be equal
		# including dim for when root is None
		def helper(point, root, dim):
			if (not root):
				return self.Node(point, dim)

			elif (point[dim] > root.point[dim]):
				root.right = helper(point, root.right, self.next_dim(dim))
			else:
				root.left = helper(point, root.left, self.next_dim(dim))
			return root

		self.root = helper(point, self.root, 0)
		self.size += 1

	"""
	find the min and max points along dim starting at node
	"""

	def find_min(self, node, dim):
		
		if (not node.left and not node.right):
			return node.point

		if (node.dim == dim):
			if (node.left):
				return self.find_min(node.left, dim)
			return node.point

		if (not node.right):
			return self.find_min(node.left, dim)
		if (not node.left):
			return self.find_min(node.right, dim)

		left = self.find_min(node.left, dim)
		right = self.find_min(node.right, dim)
		if (left[dim] < right[dim]):
			return left
		return right




	def find_max(self, node, dim):
		if (not node.left and not node.right):
			return node.point

		if (node.dim == dim):
			if (node.right):
				return self.find_max(node.right, dim)
			return node.point

		if (not node.right):
			return self.find_max(node.left, dim)
		if (not node.left):
			return self.find_max(node.right, dim)

		left = self.find_max(node.left, dim)
		right = self.find_max(node.right, dim)
		if (left[dim] > right[dim]):
			return left
		return right

	def remove(self, point):
		if (not self.contains(point)):
			raise Exception("Cannot remove nonexistent point")

		def helper(point, root):
			if (np.array_equal(point, root.point)):
				if (root.right):
					replacement = self.find_min(root.right, root.dim)
					root.point = replacement
					root.right = helper(replacement, root.right)
				elif (root.left):
					replacement = self.find_max(root.left, root.dim)
					root.point = replacement
					root.left = helper(replacement, root.left)
				else:
					root = None

			else:
				if (point[root.dim] > root.point[root.dim]):
					root.right = helper(point, root.right)
				else:
					root.left = helper(point, root.left)

			return root


		self.root = helper(point, self.root)

		self.size -= 1

	def contains(self, point):

		def helper(point, root):
			if (not root):
				return False
			if (np.array_equal(point, root.point)):
				return True

			if (point[root.dim] > root.point[root.dim]):
				return helper(point, root.right)
			return helper(point, root.left)

		return helper(point, self.root)

	def __len__(self):
		return self.size

	"""
	inorder travsersal of tree
	"""
	def __repr__(self):
		res = ""

		def helper(root):
			nonlocal res
			if (not root):
				return
			helper(root.left)

			res += str(root.point) + ", "

			helper(root.right)

		helper(self.root)

		return res



if __name__ == "__main__":

	# 100 points in 5 dimensions
	rows = 10000
	cols = 5
	points = np.zeros((rows, cols))

	for i in range(rows):
		for j in range(cols):
			points[i][j] = random.randint(-100, 100)

	t = KDTree(points)


	for i in range(rows):
		if (not t.contains(points[i, :])):
			print("fuck{}".format(i))




	# print(points[0])
	# t.remove(points[0])









