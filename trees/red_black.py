import random

class RedBlackTree:

	class Node:
		def __init__(self, data, is_red, left=None, right=None):
			self.data = data
			self.is_red = is_red
			self.left = left
			self.right = right

	def __init__(self):
		self.size = 0
		self.root = None

	def rotate_left(self, root):
		new_root = root.left
		temp = new_root.right
		new_root.right = root
		new_root.right.left = temp
		return new_root

	def rotate_right(self, root):
		new_root = root.right
		temp = new_root.left
		new_root.left = root
		new_root.left.right = temp
		return new_root


	def left_left(self, root):

		if (root.right and root.right.is_red):
			root.left.left.is_red = False
		else:
			root.is_red = True
			root.left.is_red = False
		return self.rotate_left(root)

	def left_right(self, root):
		if (root.right and root.right.is_red):
			root.left.is_red = False
		else:
			root.left.right.is_red = False
			root.is_red = True
		root.left = self.rotate_right(root.left)
		return self.rotate_left(root)

	def right_left(self, root):
		if (root.left and root.left.is_red):
			root.right.is_red = False
		else:
			root.right.left.is_red = False
			root.is_red = True

		root.right = self.rotate_left(root.right)
		return self.rotate_right(root)



	def right_right(self, root):
		if (root.left and root.left.is_red):
			root.right.right.is_red = False
		else:
			root.is_red = True
			root.right.is_red = False
		return self.rotate_right(root)

	"""
	bottom-up insertion
	find the place to insert, then insert a red node ()
	"""
	def insert(self, data):
		must_rotate = None # set to either "left" or "right"

		def helper(root):
			nonlocal data, must_rotate
			if (not root):
				return self.Node(data, True)


			if (data < root.data):
				root.left = helper(root.left)
				if (must_rotate is not None):
					# perform rotation left, must_rotate
					if (must_rotate == "left"):
						root = self.left_left(root)
					else:
						root = self.left_right(root)
					must_rotate = None
				# violation
				elif (root.is_red and root.left.is_red):
					# handle violation in the parent. signal parent.
					must_rotate = "left"
			else:
				root.right = helper(root.right)
				if (must_rotate is not None):
					# perform rotation left, must_rotate
					if (must_rotate == "left"):
						root = self.right_left(root)
					else:
						root = self.right_right(root)
					must_rotate = None
				# violation
				elif (root.is_red and root.right.is_red):
					# handle violation in the parent. signal parent.
					must_rotate = "right"

			return root


		if (self.contains(data)):
			raise Exception("Cannot insert {} because it already exists".format(data))
		self.root = helper(self.root)
		self.root.is_red = False
		self.size += 1

	def remove(self, data):

		def helper(root):
			nonlocal data
			pass


		if (not self.contains(data)):
			raise Exception("Cannot remove {} because it does not exist".format(data))
		self.root = helper(self.root)
		self.size -= 1


	"""
	is this a valid red black tree
	"""
	def is_valid(self):
		# cond1: each red node must not have a red node as a child
		# cond2: each path from a node to its leaves must have the same number of black nodes


		# do a preorder traversal
		def cond1(root):
			if (not root):
				return True
			if (root.is_red and (root.left and root.left.is_red or root.right and root.right.is_red)):
				return False
			return cond1(root.left) and cond1(root.right)

		def cond2(root):
			violation = False
			def helper(root):
				if (not root):
					return 0

				left_count = helper(root.left)
				right_count = helper(root.right)

				if (left_count != right_count):
					violation = True

				return left_count + (not root.is_red)

			helper(self.root)
			return not violation

		return cond1(self.root) and cond2(self.root)

	def contains(self, data):
		
		def helper(root):
			nonlocal data
			if (not root):
				return False
			elif (data == root.data):
				return True
			elif (data < root.data):
				return helper(root.left)
			return helper(root.right)

		return helper(self.root)

	def __len__(self):
		return self.size

	def __repr__(self):
		return ""



if __name__ == "__main__":
	t = RedBlackTree()
	nums = list(range(-1000, 1000))
	while (nums):
		t.insert(nums.pop(random.randint(0, len(nums) - 1)))


	print(t.is_valid())

