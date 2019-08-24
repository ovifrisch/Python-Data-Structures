import math
import copy
import random


class Leaf:
	def __init__(self, M=4, depth=0):
		self.M = M
		self.depth = depth
		self.items = []
	"""
	get the number of bits required to uniquely split
	this leaf into 2 buckets
	(this will always be at least self.depth, so return the number of bits after that)
	"""
	def get_agreeing_bits(self):
		# assume self.items has 2 or more elements

		def helper(hash1, hash2):
			shift = self.depth
			count = 0

			def agree(bit1, bit2):
				return (bit1 and bit2) or (not bit1 and not bit2)

			while (1):
				if (agree((hash1 >> shift) & 1, ((hash2 >> shift) & 1))):
					count += 1
					shift += 1
				else:
					return count


		agmts = float('inf')
		for i in range(1, len(self.items)):
			agmts = min(agmts, helper(self.items[0]['hash'], self.items[i]['hash']))
		return agmts

	def contains(self, key):
		return key in [x['key'] for x in self.items]

	def split(self):

		num_agreeing_bits = self.get_agreeing_bits()

		right_leaf = Leaf(M=self.M, depth=self.depth + num_agreeing_bits + 1)
		left_leaf = Leaf(M=self.M, depth=self.depth + num_agreeing_bits + 1)

		shift = self.depth + num_agreeing_bits


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

	def remove(self, key):
		for i in range(len(self.items)):
			if (self.items[i]['key'] == key):
				idx = i
		self.items.pop(idx)

	def add(self, key, val, hashed):
		self.items.append({'key':key, 'val':val, 'hash':hashed})


"""
Data too large to fit in main memory
Look up only takes 2 disk accesses
"""
class ExtendibleHash:

	def __init__(self, M=1):
		self.size = 0
		self.M = M # the maximum number of elements for a leaf
		self.directory = [Leaf()]
		self.rand_big_num = random.getrandbits(128) # for hashing

	def hash(self, key):
		key = str(key)
		def sum_chars(s):
			res = 0
			for c in s:
				res += ord(c)
			return res

		return sum_chars(key) * self.rand_big_num

	def depth(self):
		return int(math.log(len(self.directory), 2))

	def contains(self, key):
		hashed_key = self.hash(key)
		return self.directory[self.leaf_idx(hashed_key)].contains(key)

	def get_bit(self, num, pos):
		mask = 1 << pos
		return num & mask != 0

	def clear_bit(self, num, pos):
		mask = ~(1 << pos)
		return num & mask

	def set_bit(self, num, pos, val):
		return self.clear_bit(num, pos) | (val << pos)

		
	def reverse_bits(self, num, offset):
		start = 0
		end = offset
		while (start < end):
			temp = self.get_bit(num, start)
			num = self.set_bit(num, start, self.get_bit(num, end))
			num = self.set_bit(num, end, temp)
			start += 1
			end -= 1
		return num


	def leaf_idx(self, hashed_key):
		depth = self.depth()
		reversed_hash = self.reverse_bits(hashed_key, depth - 1)
		return reversed_hash & ((1 << depth) - 1)

	"""
	Update the directory as a result of a leaf going over capacity.
	There are a few cases, but I handle them generically by
	creating a new copy of the directory of the appropriate size
	with each leaf initially NULL. Then I iterate over the new
	directory and figure out which indices of the new directory
	corespond to indices in the old directory. Of course the indices of
	the new leaves are skipped over, as well as the indices that map
	to the index in the old directory that we are currently splitting.
	"""
	def update_directory(self, right_leaf, left_leaf, hashed_key):
		old_directory = copy.deepcopy(self.directory) # make a copy
		old_bucket = self.leaf_idx(hashed_key) # the old index of the hashed key

		# the factor with which the directory size must be increased
		factor = max(0, left_leaf.depth - self.depth())

		# the ratio between the new table size and the old
		ratio = int(pow(2, factor))

		# initialize a new directory with empty entries
		self.directory = [None] * len(self.directory) * ratio

		# set the left & right leaves at their respective indices
		left_idx = self.leaf_idx(left_leaf.items[0]['hash'])
		right_idx = self.leaf_idx(right_leaf.items[0]['hash'])
		self.directory[left_idx] = left_leaf
		self.directory[right_idx] = right_leaf

		"""
		now set the rest of the indices
		note: most leaves at the indices at the new array will all map
		to the same leaf at a corresponding index in the old array.
		ex: index i in new array maps to index (i / ratio) in the old
		if i maps to the index of the old leaf that was split, this means
		that unless it's equal to left_idx or right_idx, it will contain
		an empty leaf. 
		"""

		for i in range(len(self.directory)):
			if (i == left_idx or i == right_idx):
				continue

			# empty leaf
			if (i >= old_bucket * ratio and i < old_bucket * ratio + ratio):
				self.directory[i] = Leaf(self.M)
				continue

			old_idx = math.floor(i / ratio)
			self.directory[i] = old_directory[old_idx]



	def __setitem__(self, key, val):
		hashed_key = self.hash(key)
		leaf = self.directory[self.leaf_idx(hashed_key)]

		if (leaf.contains(key)):
			leaf[key] = val
			return

		# preemptively insert the item
		leaf.add(key, val, hashed_key)

		# if leaf not over capacity, we are done
		if (len(leaf) <= self.M):
			self.size += 1
			return

		# else we need to split the leaf
		right_leaf, left_leaf = leaf.split()

		# and update the directory
		self.update_directory(right_leaf, left_leaf, hashed_key)
		self.size += 1


	def __getitem__(self, key):
		hashed_key = self.hash(key)
		leaf = self.directory[self.leaf_idx(hashed_key)]
		if (not leaf.contains(key)):
			raise Exception("Key Error")
		return leaf[key]

	def __len__(self):
		return self.size

	def __repr__(self):
		res = "{"
		for i in range(len(self.directory)):
			leaf = self.directory[i]
			for j in range(len(leaf.items)):
				item = leaf.items[j]
				key = item['key']
				val = item['val']
				if (isinstance(key, int)):
					res += str(key)
				else:
					res += "'" + str(key) + "'"
				res += ": "

				if (isinstance(val, int)):
					res += str(val)
				else:
					res += "'" + str(val) + "'"
				res += ", "

		if (len(res) > 1):
			res = res[:-2]
		res += "}"
		return res


	# lazy delete
	def pop(self, key):
		hashed_key = self.hash(key)
		if (not self.contains(key)):
			raise Exception("Key Error: ".format(key))
		self.directory[self.leaf_idx(hashed_key)].remove(key)
		self.size -= 1


if __name__ == "__main__":
	h = ExtendibleHash(M=1
		)
	h[0] = 1
	h[1] = 1
	h[3] = 1
	h[2] = 1
	h[11] = 1
	# h.pop(11)
	h.pop(0)
	h[0] = 1
	print(len(h))

	for i in range(len(h.directory)):
		print(h.directory[i].items, h.directory[i].depth)

	print(h)







