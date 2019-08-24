import math
import copy


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
		self.directory = [Leaf()]

	def hash(self, key):
		return key


	def contains(self, key):
		hashed_key = self.hash(key)
		return self.get_leaf(hashed_key).contains(key)

	def get_bit(self, num, pos):
		mask = 1 << pos
		return num & mask != 0

	def clear_bit(self, num, pos):
		mask = ~(1 << pos)
		return num & mask

	def set_bit(self, num, pos, val):
		return self.clear_bit(num, pos) | (val << pos)

	def reverse_bits(self, num, offset):
		"""
		reverse the bits of num starting at offset
		ex: 111111000100, 3 => 111111000001
		"""

		start = 0
		end = offset
		while (start < end):
			temp = self.get_bit(num, start)
			num = self.set_bit(num, start, self.get_bit(num, end))
			num = self.set_bit(num, end, temp)
			start += 1
			end -= 1
		return num

	def get_leaf(self, hashed_key):
		depth = int(math.log(len(self.directory), 2))
		idx = self.reverse_bits(hashed_key, depth - 1) & ((1 << depth) - 1)
		return self.directory[idx]

	def get_bucket(self, hashed_key):
		depth = int(math.log(len(self.directory), 2))
		idx = self.reverse_bits(hashed_key, depth - 1) & ((1 << depth) - 1)
		return idx


	def update_directory(self, right_leaf, left_leaf, hashed_key, bits_required):
		old_directory = copy.deepcopy(self.directory)
		old_bucket = self.get_bucket(hashed_key)

		increase_by = bits_required - (len(self.directory) - 1)
		step_size = int(pow(2, max(0, increase_by)))

		self.directory = [None] * len(self.directory) * step_size
		new_bucket_left = self.get_bucket(left_leaf.items[0]['hash'])
		new_bucket_right = self.get_bucket(right_leaf.items[0]['hash'])
		self.directory[new_bucket_left] = left_leaf
		self.directory[new_bucket_right] = right_leaf

		for i in range(len(self.directory)):
			if (i == new_bucket_left or i == new_bucket_right):
				continue

			# empty leaf
			if (i >= old_bucket * step_size and i < old_bucket * step_size + step_size):
				self.directory[i] = Leaf(self.M)
				continue

			old_idx = math.floor(i / step_size)
			self.directory[i] = old_directory[old_idx]



	def __setitem__(self, key, val):
		hashed_key = self.hash(key)
		leaf = self.get_leaf(key)

		if (leaf.contains(key)):
			leaf[key] = val
			return

		leaf.add(key, val, hashed_key)

		if (len(leaf) <= self.M):
			return

		# the leaf is at its capacity
		bits_required = leaf.bits_required()
		right_leaf, left_leaf = leaf.split()

		self.update_directory(right_leaf, left_leaf, hashed_key, bits_required)


	def __getitem__(self, key):
		hashed_key = self.hash(key)
		leaf = self.get_leaf(hashed_key)
		if (not leaf.contains(key)):
			raise Exception("Key Error")
		return leaf[key]

	def __len__(self):
		return self.size

	def pop(self, key):
		pass


if __name__ == "__main__":
	h = ExtendibleHash()
	h[0] = 1
	h[1] = 1
	h[3] = 1
	h[2] = 1

	for i in range(len(h.directory)):
		print(h.directory[i].items, h.directory[i].depth, h.directory[i].min_agreements)







