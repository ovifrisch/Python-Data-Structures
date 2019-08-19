

class Splay:

	class Node:
		def __init__(self, val, left=None, right=None):
			self.val = val
			self.left = left
			self.right = right

	def __init__(self, data=[], tree=None):
		if (tree is not None):
			self.root = tree
			return
		self.size = 0
		self.root = None
		for x in data:
			self.insert(x)

	def rotateWithLeft(self, root):
		new_root = root.left
		root.left = new_root.right
		new_root.right = root
		return new_root

	def rotateWithRight(self, root):
		new_root = root.right
		root.right = new_root.left
		new_root.left = root
		return new_root

	"""
	# zig means left
	# zag means right
	"""
	
	def zig_zag(self, root):
		root.left = self.rotateWithRight(root.left)
		return self.rotateWithLeft(root)

	def zag_zig(self, root):
		root.right = self.rotateWithLeft(root.right)
		return self.rotateWithRight(root)

	def zig_zig(self, root):
		B = root.left.left.right
		C = root.left.right
		D = root.right
		X = root.left.left
		P = root.left
		G = root
		G.left = C
		P.left = B
		P.right = G
		X.right = P
		return X


	def zag_zag(self, root):
		B = root.right.right.left
		C = root.right.left
		D = root.left
		X = root.right.right
		P = root.right
		G = root
		G.right = C
		P.right = B
		P.left = G
		X.left = P
		return X


	def splay(self, access_path):
		if (len(access_path) == 1):
			return access_path[0]

		if (len(access_path) == 2):
			if (access_path[-2][1] == "Left"):
				access_path[-2][0].left = access_path[-1]
				return self.rotateWithLeft(access_path[-2][0])
			else:
				access_path[-2][0].right = access_path[-1]
				return self.rotateWithRight(access_path[-2][0])
		else:
			if (access_path[-3][1] == "Left"):
				if (access_path[-2][1] == "Left"):
					access_path[-2][0].left = access_path[-1]
					access_path[-3] = self.zig_zig(access_path[-3][0])
				else:
					access_path[-2][0].right = access_path[-1]
					access_path[-3] = self.zig_zag(access_path[-3][0])
			else:
				if (access_path[-2][1] == "Right"):
					access_path[-2][0].right = access_path[-1]
					access_path[-3] = self.zag_zag(access_path[-3][0])
				else:
					access_path[-2][0].left = access_path[-1]
					access_path[-3] = self.zag_zig(access_path[-3][0])

		access_path = access_path[:-2]
		return self.splay(access_path)



	def insert(self, val):

		def helper(root, val, access_path):
			if (not root):
				leaf = self.Node(val)
				access_path.append(leaf)
				return leaf
			elif (val == root.val):
				raise Exception("Value already exists")
			elif (val < root.val):
				access_path.append((root, "Left"))
				root.left = helper(root.left, val, access_path)
			else:
				access_path.append((root, "Right"))
				root.right = helper(root.right, val, access_path)

			return root

		access_path = []
		self.root = helper(self.root, val, access_path)
		self.root = self.splay(access_path)
		self.size += 1


	def contains(self, val):

		def helper(root, target, access_path):
			if (not root):
				return False
			if (root.val == target):
				access_path.append(root)
				return True
			elif (target < root.val):
				access_path.append((root, "Left"))
				return helper(root.left, target, access_path)
			else:
				access_path.append((root, "Right"))
				return helper(root.right, target, access_path)

		access_path = []
		does_contain = helper(self.root, val, access_path)
		if (does_contain):
			self.root = self.splay(access_path)
		return does_contain


	def remove(self, val):
		if (not self.contains(val)):
			raise Exception("Value not found")

		# node to be deleted is now at root because of the
		# splaying that occurred in the contains method
		if (not self.root.left and not self.root.right):
			self.root = None

		elif (not self.root.left):
			self.root = self.root.right

		elif (not self.root.right):
			self.root = self.root.left

		else:
			# find and delete largest node in left subtree
			if (not node.left.right):
				node.left.right = self.root.right
				self.root = node.left
			else:
				runner = self.root.left
				while (runner.right):
					runner = runner.right
				largest = runner.right
				runner.right = largest.left
				largest.left = self.root.left
				largest.right = self.root.right
				self.root = largest

		self.size -= 1


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
	t = Splay()
	t.insert(10)
	t.insert(5)
	t.insert(15)
	t.remove(15)
	print(t)
	# print(t)
	# print(t.contains(10))
	# print(t)

