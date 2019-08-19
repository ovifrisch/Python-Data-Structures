import random

class Treap:

	class Node:
		def __init__(self, data, priority, left=None, right=None):
			self.data = data
			self.priority = priority
			self.left = left
			self.right = right

	def __init__(self):
		self.root = None
		self.size = 0
		self.k = 1000

	def rotate_right(self, root):
		new_root = root.right
		temp = new_root.left
		new_root.left = root
		new_root.left.right = temp
		return new_root

	def rotate_left(self, root):
		new_root = root.left
		temp = new_root.right
		new_root.right = root
		new_root.right.left = temp
		return new_root
		
	def insert(self, data):
		
		def helper(data, root):
			if (not root):
				prty = random.randint(0, self.k)
				root = self.Node(data, prty)
			elif (data < root.data):
				root.left = helper(data, root.left)
				if (root.left.priority < root.priority):
					root = self.rotate_left(root)
			else:
				root.right = helper(data, root.right)
				if (root.right.priority < root.priority):
					root = self.rotate_right(root)
			return root


		if (self.contains(data)):
			raise Exception("{} cannot be inserted because it already exists".format(data))
		self.root = helper(data, self.root)
		self.size += 1

	def contains(self, data):

		def helper(data, root):
			if (not root):
				return False
			elif (root.data == data):
				return True
			elif (data < root.data):
				return helper(data, root.left)
			else:
				return helper(data, root.right)

		return helper(data, self.root)

	def valid_bst(self):
		prev = None
		def inorder(root):
			nonlocal prev
			if (not root):
				return True
			if (not inorder(root.left)):
				return False

			if (prev is not None and root.data < prev):
				return False
			prev = root.data
			return inorder(root.right)

		return inorder(self.root)
		
	# every node needs to have priority >= parent
	def valid_heap(self):
		valid = True
		def postorder(root):
			nonlocal valid
			if (root is None):
				return float('inf')
			min_left = postorder(root.left)
			min_right = postorder(root.right)

			if (min(min_left, min_right) < root.priority):
				valid = False

			return root.priority

		postorder(self.root)
		return valid


	def remove(self, data):
		
		def helper(root, data):
			if (not root.left and not root.right):
				return None

			if (root.data != data):
				if (data > root.data):
					root.right = helper(root.right, data)
				else:
					root.left = helper(root.left, data)

			else:

				if (root.right):
					root = self.rotate_right(root)
					root.left = helper(root.left, data)
				else:
					root = self.rotate_left(root)
					root.right = helper(root.right, data)

			return root

		if (not self.contains(data)):
			raise Exception("Cannot remove {} because it does not exist".format(data))

		self.root = helper(self.root, data)
		self.size -= 1

	def __len__(self):
		return self.size

	"""
	inorder
	"""
	def __repr__(self):
		res = "["

		def helper(root):
			nonlocal res
			if (not root):
				return
			helper(root.left)
			res += str(root.data) + ", "
			helper(root.right)

		helper(self.root)
		if (len(res) > 1):
			res = res[:-2]
		return res + "]"




if __name__ == "__main__":
	tr = Treap()
	nums = list(range(-10, 20))
	while (nums):
		tr.insert(nums.pop(random.randint(0, len(nums) - 1)))
	print(tr)

	# nums = list(range(-100, 100))
	# while (nums):
	# 	ri =random.randint(0, len(nums) - 1)
	# 	print(tr.contains(nums[ri]))
	# 	tr.remove(nums.pop(ri))

	# print(len(tr))
	# nums = list(range(-100, 100))
	# while (nums):
	# 	print(tr.contains(nums.pop(random.randint(0, len(nums) - 1))))


	# print(tr.valid_bst())
	# print(tr.valid_heap())



