from avl import AVL

"""
Inherits from AVL and implements
an extra method that allows us
to find the next child of the
btree to traverse over

also implements remove_min and remove_max
needed for splitting/sharing nodes
"""
class BAVL(AVL):
	def __init__(self, data=[]):
		AVL.__init__(self, data)


	"""
	create two lists and return the one
	with minimum length. the first list
	is the inorder of the tree ending just
	before a node meets condition p and starts
	at the last node that meets condition q.

	the second list is the inorder of the tree that
	starts just after a node meets condition p and
	ends at the first node that meets condition q.

	p is guaranteed to be true for exactly one node
	q is not guaranteed for any nodes
	if no node is found before p that satisfies q
	this list will be empty. same goes for the mirror case.

	p is overflow
	q is underflow
	"""
	def get_optimal_adoption(self, p, q):
		pre = []
		post = []
		found_p = found_q = False

		def helper(root):
			nonlocal pre, post, found_p, found_q
			if (not root):
				return

			helper(root.left)
			if (found_q and found_p):
				return
			if (q(root.val)):
				if (not found_p):
					pre = [root.val]
				else:
					post.append(root.val)
					found_q = True
					return

			elif (p(root.val)):
				pre.append(root.val)
				post.append(root.val)
				found_p = True

			else:
				if (found_p):
					post.append(root.val)
				elif (pre != []):
					pre.append(root.val)

			helper(root.right)

		helper(self.root)
		if (not found_q):
			return pre
		return pre if len(pre) > len(post) else post



	"""
	get the inode that has this key
	"""
	def get_node(self, key):
		node = None
		def helper(root):
			nonlocal node
			if (node or not root):
				return
			if (key >= root.val.key):
				if (root.right):
					helper(root.right)
				if (not node):
					node = root.val
			elif (key < root.val.key):
				helper(root.left)
		helper(self.root)
		return node

	def remove_min(self):
		if (not self.root):
			raise Exception("Remove min not defined on empty tree")

		node = self.root
		while (node.left):
			node = node.left
		val = node.val
		self.remove(val)
		return val

	def remove_max(self):
		if (not self.root):
			raise Exception("Remove max not defined on empty tree")

		node = self.root
		while (node.right):
			node = node.right
		val = node.val
		self.remove(val)
		return val

	def get_min(self):
		if (not self.root):
			raise Exception("Get min not defined on empty tree")

		node = self.root
		while (node.left):
			node = node.left
		return node.val

	def get_max(self):
		if (not self.root):
			raise Exception("Get min not defined on empty tree")

		node = self.root
		while (node.right):
			node = node.right
		return node.val



if __name__ == "__main__":
	t = BAVL([1, 2, 3, 4, 5, 6])
	print(t)
	p = lambda x: x == 1
	q = lambda x: x == 2
	vals = t.get_optimal_adoption(p, q)
	print(vals)






