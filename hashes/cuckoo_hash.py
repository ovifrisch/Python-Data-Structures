

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

	def __setitem__(self, key, val):
		pass

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