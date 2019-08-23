
class CuckooHash:

	def __init__(self, num_tables=2, items_per_cell=1, init_ts=10):
		self.size = 0
		self.num_tables = num_tables
		self.items_per_cell = items_per_cell
		self.init_ts = init_ts
		array = [None] * self.init_ts
		arrays = [array] * self.num_tables
		hash_functions = self.get_hash_functions()
		self.tables = [{'array':x[0], 'hf':x[1]} for x in zip(arrays, hash_functions)]


	def __getitem__(self, key):
		val = self.__find(key)
		if (val is None):
			raise Exception("Key error: {}".format(key))
		return val


	def get_hash_functions(self):
		hfs = []
		# TODO
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
			items = table['array'][table['hf'](key)]
			if (items):
				for i in range(len(items)):
					if (item['key'] == key):
						popped_item = items.pop(i)
						self.size -= 1
						return popped_item['val']


	def table_permutations(self):
		idxs = list(range(num_tables))

		helper(idxs, curr):
			if (not idxs):
				yield curr

			for i in range(len(idxs)):
				helper(curr + [idxs[i]], idxs[:i] + idxs[i+1;])

		yield helper(idxs)


	def __rehash(self):
		pass

	def __setitem__(self, key, val):
		if (self.update(key, val)):
			return

		# try to insert key, val in table i
		def displace(key, val, i):
			table = tables[i]
			idx = table['hf'](key)
			# insert it preemptively
			table['array'][idx].append({'key':key, 'val':val})

			# now if we have exceeded the capacity, remove the first one and return it
			if (len(table['array'][idx]) > self.items_per_cell):
				return table['array'][idx].pop(0)
			return None

		# try each permutation of tables
		for perm in self.table_permutations():
			curr_key = key
			curr_val = val
			curr_idx = 0
			while (1):
				next_item = displace(key, val, perm[curr_idx])
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