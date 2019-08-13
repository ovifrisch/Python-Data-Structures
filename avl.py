

class AVL:

	class Node:
		def __init__(self, val, height, left=None, right=None):
			self.val = val
			self.height = height
			self.left = left
			self.right = right

	# height of empty tree is defined to be -1
	def __init__(self, data=[]):
		self.size = 0
		self.root = None
		self.max_diff = 1
		for x in data:
			self.insert(x)


	def is_balanced(self):

		def helper(root):
			if (not root):
				return True
			if (abs(self.height(root.left) - self.height(root.right)) > 1):
				return False

			return helper(root.left) and helper(root.right)
		return helper(self.root)

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


	def insert(self, val):

		def helper(root, val):
			if (not root):
				root = self.Node(val, 0)
				self.size += 1
			elif (root.val == val):
				raise Exception("Value already exists")
			elif (val < root.val):
				root.left = helper(root.left, val)
			else:
				root.right = helper(root.right, val)

			return self.balance(root)

		self.root = helper(self.root, val)

	def find_min(self, node):
		while (node.left):
			node = node.left
		return node.val

	def remove(self, val):

		def helper(root, target):
			if (not root):
				raise Exception("Value not found")

			elif (target < root.val):
				root.left = helper(root.left, target)
			elif (target > root.val):
				root.right = helper(root.right, target)
			else:
				if (root.left and root.right):
					root.val = self.find_min(root.right)
					root.right = helper(root.right, root.val)
				else:
					if (root.left):
						return = root.left
					else:
						return root.right
			return self.balance(root)

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
		if (not avl.is_balanced()):
			print("not good")

	for i in range(9, -1, -1):
		avl.remove(i)
		if (not avl.is_balanced()):
			print("not good")
	print(len(avl))






