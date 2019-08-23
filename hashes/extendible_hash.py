
# from trie import Trie


# class MyTrie(Trie):
# 	def __init__(self):
# 		Trie.__init__(self)

# 	class Node(Trie.Node):
# 		def __init__(self):


class Trie:

	class Node:
		def __init__(self, left=None, right=None, data_ptr=None):
			self.left = left
			self.right = right
			self.data_ptr = data_ptr

		def is_leaf(self):
			return self.data_ptr is not None

	def __init__(self, M):
		self.M = M
		self.root = self.Node(data_ptr=Leaf(self.M))


class Leaf:
	def __init__(self, M=4, depth=0):
		self.M = 4
		self.depth = 0
		self.items = []

	def contains(self, key):
		return key in [x['key'] for x in self.items]

	def __setitem__(self, key, val):
		for item in self.items:
			if (item['key'] == key):
				item['val'] = val

	def __getitem__(self, key):
		for item in self.items:
			if (item['key'] == key):
				return item['val']

	def __len__(self):
		return len(self.items)

	def add(self, key, val):
		self.items.append({'key':key, 'val':val})


"""
Data too large to fit in main memory
Look up only takes 2 disk accesses
"""
class ExtendibleHash:

	def __init__(self, M=4):
		self.size = 0
		self.M = M # the maximum number of elements for a leaf
		self.directory = Trie(M)
		self.depth = 0

	def __setitem__(self, key, val):
		leaf = self.get_leaf(key)

		if (leaf.contains(key)):
			leaf[key] = val
			return

		if (len(leaf) < self.M):
			leaf.add(key, val)
			return

		# the leaf is at its capacity
		pass

	def get_leaf(self, key):
		hashed = self.hash(key)
		depth = 0

		# find the trie leaf
		def helper(root):
			nonlocal key, depth
			if (root.is_leaf()):
				return root.data_ptr

			# go right
			if ((hashed >> depth) & root.bit):
				root = root.right
			else:
				root = root.left
			depth += 1
			return helper(root)

		return helper(self.directory.root)


	def __getitem__(self, key):
		leaf = self.get_leaf(key)
		if (not leaf.contains(key)):
			raise Exception("Key Error")
		return leaf[key]

	def __repr__(self):
		pass

	def __len__(self):
		return self.size


	"""
	just return the key for now. assuming the keys
	are all unique integers
	"""
	def hash(self, key):
		return key

	def contains(self, key):
		return self.get_leaf(key).contains(key)


	def pop(self, key):
		pass



if __name__ == "__main__":
	h = ExtendibleHash()
	h[0] = 1
	print(h[0])











