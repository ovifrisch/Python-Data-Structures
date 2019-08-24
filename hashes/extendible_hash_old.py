
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

	def increase_directory_size(self, by=1):

		def add_levels(self, root, by):
			if (by == 0):
				return
			root.left = self.Node()
			root.right = self.Node()
			add_levels(root.left, by - 1)
			add_levels(root.right, by - 1)



		def helper(self, root):
			if (root.data_ptr):
				add_levels(root, by)
				return
			helper(root.left)
			helper(root.right)

	"""
	update the trie by adding "by" levels and updating the data pointers
	"""
	def update(self, right_leaf, left_leaf, hashed, by):
		"""
		if you get to a leaf that matches the hash up to that point,

		"""
		pass



class Leaf:
	def __init__(self, M=4, depth=0):
		self.M = M
		self.depth = depth
		self.items = []
		self.min_agreements = float('inf')

	def bits_required(self):
		return self.depth + self.min_agreements + 1

	"""
	starting from depth past LSB, return the number of consecutive bits that
	are the same in hash1 and hash2
	"""
	def num_agreements(self, hash1, hash2):
		shift = count = self.depth

		def agree(bit1, bit2):
			return (bit1 and bit2) or (not bit1 and not bit2)

		while (1):
			if (agree((hash1 >> shift) & 1, ((hash2 >> shift) & 1))):
				count += 1
				shift += 1
			else:
				return count

	def contains(self, key):
		return key in [x['key'] for x in self.items]

	def split(self):

		right_leaf = Leaf(M=self.M, depth=self.depth + self.min_agreements + 1)
		left_leaf = Leaf(M=self.M, depth=self.depth + self.min_agreements + 1)

		shift = self.depth + self.min_agreements
		for item in self.items:
			hsh = item['hash']
			if ((hsh >> shift) & 1 == 1):
				right_leaf.add(item['key'], item['val'], hsh)
			else:
				left_leaf.add(item['key'], item['val'], hsh)

		return right_leaf, left_leaf

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

	def add(self, key, val, hashed):
		self.items.append({'key':key, 'val':val, 'hash':hashed})

		if (len(self) == 1):
			return
		else:
			self.min_agreements = min(self.min_agreements, self.num_agreements(hashed, self.items[0]['hash']))


"""
Data too large to fit in main memory
Look up only takes 2 disk accesses
"""
class ExtendibleHash:

	def __init__(self, M=1):
		self.size = 0
		self.M = M # the maximum number of elements for a leaf
		self.directory = Trie(M)
		self.depth = 0

	def __setitem__(self, key, val):
		hashed = self.hash(key)
		leaf = self.get_leaf(key)

		if (leaf.contains(key)):
			leaf[key] = val
			return

		leaf.add(key, val, hashed)

		if (len(leaf) <= self.M):
			return

		# the leaf is at its capacity
		bits_required = leaf.bits_required()
		right_leaf, left_leaf = leaf.split()
		self.directory.update(right_leaf, left_leaf, hashed, bits_required - self.depth)
		self.depth = max(self.depth, bits_required)



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
	h[3] = 1
	h[11] = 12










