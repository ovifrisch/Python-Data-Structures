"""

AVL Tree
________
Self-balancing Binaray Search Tree
__________________________________
Insertion: O(logN)
Deletion: O(logN)
_________________
What it's good for:

Guaranteeing O(logN)
time complexity on Binary Search Tree
operations
_______________________________________
How it works:

For each node in the tree, we enforce that
the height of its two children differ by at
most 1. This AVL property can be violated
on insertion and deltion, so we fix it using
rotations along the search path.

"""


class AVL:

	class Node:
		def __init__(self, val, height, left=None, right=None):
			self.val = val
			self.height = height
			self.left = left
			self.right = right

	def __init__(self, data=[]):
		self.size = 0
		self.root = None
		self.max_diff = 1
		for x in data:
			self.insert(x)

	def insert(self, val):

		def helper(root, val):
			# found spot to insert
			if (not root):
				root = self.Node(val, 0)
				self.size += 1

			# val already in the tree; raise exception
			elif (root.val == val):
				raise Exception("Value already exists")

			# go left
			elif (val < root.val):
				root.left = helper(root.left, val)

			# go right
			else:
				root.right = helper(root.right, val)

			# balance the current node if there is a height violation
			# called for every node on the insertion path
			return self.balance(root)

		# the helper method returns the new root
		self.root = helper(self.root, val)

	def remove(self, val):

		# aux method to find the minimum of a subtree
		def find_min(node):
			while (node.left): # keep going left
				node = node.left
			return node.val # can't go left anymore

		def helper(root, target):
			nonlocal find_min
			if (not root):
				raise Exception("Value not found")

			# go left
			elif (target < root.val):
				root.left = helper(root.left, target)

			# go right
			elif (target > root.val):
				root.right = helper(root.right, target)

			# target is equal to root.val
			else:
				# two children; replace with min of right,
				# recursively delete the replacement
				if (root.left and root.right):
					root.val = find_min(root.right)
					root.right = helper(root.right, root.val)
				else:
					if (root.left):
						return root.left
					else:
						return root.right
			return self.balance(root)

		# helper will return the new root
		self.root = helper(self.root, val)
		self.size -= 1

	def contains(self, val):

		def helper(root, target):
			if (not root):
				return False
			if (target == root.val):
				return True
			if (target < root.val):
				return helper(root.left, target)
			else:
				return helper(root.right, target)

		return helper(self.root, val)

	def balance(self, root):
		if (not root):
			return root

		# left child larger height than right child
		if (self.height(root.left) - self.height(root.right) > self.max_diff):

			# left left
			if (self.height(root.left.left) > self.height(root.left.right)):
				root = self.rotateWithLeft(root)

			# left right
			else:
				root = self.doubleRotateWithLeft(root)

		# right child larger height than left child
		elif (self.height(root.right) - self.height(root.left) > self.max_diff):

			# right right
			if (self.height(root.right.right) > self.height(root.right.left)):
				root = self.rotateWithRight(root)

			# right left
			else:
				root = self.doubleRotateWithRight(root)
				
		root.height = 1 + max(self.height(root.left), self.height(root.right))
		return root

	def rotateWithLeft(self, root):
		new_root = root.left
		root.left = new_root.right
		new_root.right = root
		new_root.right.height = 1 + max(self.height(new_root.right.right), self.height(new_root.right.left))
		root = new_root
		return root

	def rotateWithRight(self, root):
		new_root = root.right
		root.right = new_root.left
		new_root.left = root
		new_root.left.height = 1 + max(self.height(new_root.left.left), self.height(new_root.left.right))
		root = new_root
		return root

	def doubleRotateWithLeft(self, root):
		root.left = self.rotateWithRight(root.left)
		return self.rotateWithLeft(root)

	def doubleRotateWithRight(self, root):
		root.right = self.rotateWithLeft(root.right)
		return self.rotateWithRight(root)

	def height(self, node):
		if (not node):
			return -1
		return node.height

	"""
	return the inorder traversal of the
	tree as a list
	"""
	def inorder(self):
		res = []
		def helper(root):
			if (not root):
				return
			helper(root.left)
			res.append(root.val)
			helper(root.right)
		helper(self.root)
		return res


	"""
	level order traversal
	"""
	def __repr__(self):
		if (not self.root):
			return "[]"

		q = [self.root]
		res = "["

		while (q):
			x = q.pop(0)
			if (not x):
				res += "None, "

			else:
				res += str(x.val) + ", "
				if (x.left or x.right):
					q.append(x.left)
					q.append(x.right)

		res = res[:-2] + "]"
		return res

	def __len__(self):
		return self.size



if __name__ == "__main__":
	avl = AVL()
	for i in range(10):
		avl.insert(i)

	for i in range(10):
		avl.remove(i)




