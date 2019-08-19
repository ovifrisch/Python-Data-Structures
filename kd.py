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
	def __init__(self, points):
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
		median_val = points[median_idx, dim]


		# find the minimum distance to the right that gives a diff num
		right_idx = median_idx
		while (right_idx < sorted_idxs.shape[0] - 1 and points[right_idx+1, dim] == median_val):
			right_idx += 1

		median = points[right_idx, :]
		left = points[:right_idx, :]
		right = points[right_idx + 1:, :]

		next_dim = self.next_dim(dim)

		left_child = self.make_kd(left, next_dim)
		right_child = self.make_kd(right, next_dim)
		print("inserted point {}".format(median))
		return self.Node(median, dim, left_child, right_child)


	def insert(self, point):
		if (self.contains(point)):
			raise Exception("point already exists")

		# dim and root.dim should always be equal
		# including dim for when root is None
		def helper(self, point, root, dim):

			if (not root):
				return self.Node(point, dim)

			elif (point[dim] > root.point[dim]):
				root.right = helper(point, root.right, self.next_dim(dim))
			else:
				root.left = helper(point, root.left, self.next_dim(dim))

		self.root = helper(point, self.root, self.root.dim)
		self.size += 1

	def remove(self, point):
		if (not self.contains(point)):
			raise Exception("Cannot remove nonexistent point")

		# remove the point

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
		return ""



if __name__ == "__main__":

	# 100 points in 5 dimensions
	rows = 20
	cols = 5
	points = np.zeros((rows, cols))

	for i in range(rows):
		for j in range(cols):
			# generate a random number
			points[i][j] = random.randint(-1000, 1000)

	t = KDTree(points)









