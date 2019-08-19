import copy
import math

class ProbingHash:

	def __init__(self, probing_function):
		# make sure the table size is always prime
		self.array = [None] * 101
		self.size = 0
		self.probing_function = probing_function

	def next_prime(self, N):
		curr = N + 1
		next_prime = None
		while (not next_prime):
			prime = True
			for i in range(2, math.floor(pow(curr, 0.5)) + 1):
				if (curr % i == 0):
					prime = False
					break
			if (prime):
				next_prime = curr
			curr += 1
		return next_prime

	"""
	x is the str reperesentation of the key
	Return value is the hashed value using sum_chars(x) % table_size
	"""
	def __hash(self, key):
		
		def sum_chars(s):
			res = 0
			for c in s:
				res += ord(c)
			return res

		return sum_chars(key) % len(self.array)

	"""
	probe the array using probing_function until cell with key is found or None found
	if val is None:
		if None, return False. if key, return True
	else
		if None, add key val pair to cell. if key, do nothing.
	"""
	def __probe(self, hashed_key, key, val=None, pop=False):
		curr_idx = hashed_key
		num_probes = 0
		while (1):
			# continue with probing if there's an entry here that doesn't match our key
			# else go inside this block
			if (self.array[curr_idx] is None or self.array[curr_idx]['key'] == key):
				if (val is not None):
					self.array[curr_idx] = {'key':key, 'val':val}
					return
				else:
					if (self.array[curr_idx] is None):
						return False
					else:
						the_val = self.array[curr_idx]['val']
						if (pop):
							self.array[curr_idx] = None
						return the_val
			num_probes += 1
			curr_idx = (hashed_key + self.probing_function(num_probes)) % len(self.array)


	"""
	Get the 
	"""
	def __getitem__(self, key):
		hashed_key = self.__hash(str(key))
		val = self.__probe(hashed_key, key)
		if (val is False):
			raise Exception("Key Error: {}".format(key))
		return val
	"""
	Rehash the hastable
	Set the new size to be the next prime after 2 times the old size
	"""
	def __rehash(self):
		print("rehashing")
		old_array = copy.deepcopy(self.array)
		self.array = [None] * self.next_prime(len(self.array) * 2)
		self.size = 0

		for item in old_array:
			if (item is None):
				continue
			self[item['key']] = item['val']

	"""
	Add key val pair to hash
	"""
	def __setitem__(self, key, val):
		if (self.contains(key) is False):
			self.size += 1
		# check if size will be >= capacity
		if (self.size >= len(self.array) // 2):
			self.__rehash()

		hashed_key = self.__hash(str(key))
		self.__probe(hashed_key, key, val)

	"""
	Remove the key from hash
	"""
	def pop(self, key):
		hashed_key = self.__hash(str(key))
		val = self.__probe(hashed_key, key, pop=True)
		if (val is False):
			raise Exception("Key Error: {}".format(key))
		self.size -= 1
		return val

	"""
	Does the hash contain this key
	"""
	def contains(self, key):
		hashed_key = self.__hash(str(key))
		if (self.__probe(hashed_key, key) is False):
			return False
		return True


	def __len__(self):
		return self.size

	def __repr__(self):
		res = "{"
		for item in self.array:
			if (item is None):
				continue
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



if __name__ == "__main__":
	h = ProbingHash(probing_function=(lambda x: pow(x, 2)))
	h[0] = 1
	h[2] = 2
	h['cat'] = 1
	h[1] = 'cat'
	h['cat'] = 'cat'
	h['dog'] = 'cat'
	print(h)
	print(len(h))









