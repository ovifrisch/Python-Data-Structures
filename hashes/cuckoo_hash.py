import random
import copy

class CuckooHash:

	def __init__(self, num_tables=2, items_per_cell=1, init_ts=1, load_factor=0.5):
		self.size = 0
		self.num_tables = num_tables
		self.items_per_cell = items_per_cell
		self.ts = init_ts
		self.load_factor = load_factor
		self.tables = []
		for i in range(self.num_tables):
			array = [None] * self.ts
			hash_function = self.get_hash_function(self.ts)
			self.tables.append({'array':array, 'hf':hash_function, 'size':0})
		self.table_start = 0
		"""
		array: the underlying array
		hf: the hash function that maps keys in this array
		size: the array's size
		"""


	def __getitem__(self, key):
		val = self.__find(key)
		if (val is None):
			raise Exception("Key error: {}".format(key))
		return val

	def get_hash_function(self, ts):

		def hash(x):
			x = str(x)
			res = 0
			for c in x:
				res += ord(c)
			return res


		rand_bits = random.getrandbits(128)
		f = lambda x: (hash(x) * rand_bits) %  ts
		return f


	def get_hash_functions(self, ts):
		hfs = []
		for _ in range(self.num_tables):
			hfs.append(self.get_hash_function(ts))
		return hfs

	def update(self, key, val):
		for table in self.tables:
			items = table['array'][table['hf'](key)]
			if (items):
				for item in items:
					if (item['key'] == key):
						item['val'] = val
						return True
		return False


	def remove(self, key):
		for table in self.tables:
			array = table['array']
			idx = table['hf'](key)
			items = array[idx]
			if (items):
				for i in range(len(items)):
					if (item['key'] == key):
						popped_item = items.pop(i)
						# check if no more items left
						if (len(items) == 0):
							array[idx] = None
							table['size'] -= 1
						self.size -= 1
						return popped_item['val']


	def table_permutations(self):
		x = list(range(self.num_tables))
		x.pop(self.table_start)
		table_indides = [self.table_start] + x
		res = []

		def helper(idxs, curr):
			if (not idxs):
				res.append(curr)
				return

			for i in range(len(idxs)):
				helper(idxs[:i] + idxs[i+1:], curr + [idxs[i]])

		helper(table_indides, [])
		return res

	"""
	rehash each table by doubling its size, recomputing hash functions,
	and then re-inserting all items
	"""
	def __rehash(self):
		raise Exception("not yet implemented")

	"""
	double the table size for table i, recompute its hash
	function, then rehash all the items
	"""
	def __rehash_table(self, i):
		table_cpy = copy.deepcopy(self.tables[i])
		arr = [None] * len(table_cpy['array']) * 2
		hf = self.get_hash_function(len(arr))
		self.tables[i] = {'array':arr, 'hf':hf, 'size':0}
		old_table_start = self.table_start
		self.table_start = i
		for items in table_cpy['array']:
			if (items):
				for item in items:
					self[item['key']] = item['val']
		self.table_start = old_table_start

	def __setitem__(self, key, val):
		if (self.update(key, val)):
			return

		# try to insert key, val in table i
		def displace(key, val, i):
			table = self.tables[i]
			idx = table['hf'](key)
			# insert it preemptively
			if (not table['array'][idx]):
				table['array'][idx] = []
			table['array'][idx].append({'key':key, 'val':val})

			# now if we have exceeded the capacity, remove the first one and return it
			if (len(table['array'][idx]) > self.items_per_cell):
				x = table['array'][idx].pop(0)
				return x

			# successfully inserted
			if (len(table['array'][idx]) == self.items_per_cell):
				table['size'] += 1
				if (table['size'] / len(table['array']) > self.load_factor):
					self.__rehash_table(i)
			return None

		# try each permutation of tables
		for perm in self.table_permutations():
			curr_key = key
			curr_val = val
			curr_idx = 0
			while (1):
				next_item = displace(curr_key, curr_val, perm[curr_idx])
				if (not next_item): # successfully found a spot
					self.size += 1
					return
				curr_key = next_item['key']
				curr_val = next_item['val']
				curr_idx += 1
				if (curr_idx == len(perm)):
					curr_idx = 0

				# made a cycle
				if (curr_key == key):
					break

		# failed to insert, need to rehash
		self.__rehash()

		# try inserting again, this time in the rehashed table
		self[key] = val


	def pop(self, key):
		if (not self.contains(key)):
			raise Exception("cannot pop {} because it does not exist".format(key))
		return self.remove(key)

	def __find(self, key):
		for table in self.tables:
			items = table['array'][table['hf'](key)]
			if (items):
				for item in items:
					if (item['key'] == key):
						return item['val']
		return None

	def contains(self, key):
		return self.__find() is not None

	def __repr__(self):
		pass

	def __len__(self):
		return self.size



if __name__ == "__main__":
	h = CuckooHash()
	h["ovi"] = 2
	h["dan"] = 3
	h["x"] = 4
	print(h["ovi"])
	print(h["x"])


