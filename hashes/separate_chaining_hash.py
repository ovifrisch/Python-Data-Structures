from dll import DLL
import copy

class SeparateChainingHash:

	def __init__(self):
		self.array = self.__init_arr(2)
		self.size = 0

	def __init_arr(self, N):
		arr = [None] * N
		for i in range(len(arr)):
			arr[i] = DLL()
		return arr

	def __hash(self, key):
		
		def sum_chars(s):
			res = 0
			for c in s:
				res += ord(c)
			return res

		return sum_chars(key) % len(self.array)

	def __getitem__(self, key):
		hashed_key = self.__hash(str(key))
		ll = self.array[hashed_key]
		for item in ll:
			if (item['key'] == key):
				return item['val']

		raise Exception("Key Error: {}".format(key))

	def rehash(self):
		old_array = copy.deepcopy(self.array)
		self.array = self.__init_arr(len(old_array) * 2)
		self.size = 0

		for ll in old_array:
			for item in ll:
				self[item['key']] = item['val']


	def __setitem__(self, key, val):
		hashed_key = self.__hash(str(key))
		ll = self.array[hashed_key]
		self.size += 1

		for item in ll:
			if (item['key'] == key):
				self.size -= 1
				ll.remove_if(lambda x: x['key'] == key)
				break

		ll.insert_front({'key':key, 'val':val})

		if (self.size > len(self.array) // 2):
			self.rehash()

	def pop(self, key):
		if (not self.contains(key)):
			raise Exception("Key Error: {}".format(key))

		hashed_key = self.__hash(str(key))
		ll = self.array[hashed_key]
		val = None
		for item in ll:
			if (item['key' == key]):
				val = item['val']
		ll.remove_if(lambda x: x['key'] == key)
		return val

	def contains(self, key):
		hashed_key = self.__hash(str(key))
		ll = self.array[hashed_key]
		for item in ll:
			if (item['key'] == key):
				return True
		return False

	def __len__(self):
		return self.size

	def __repr__(self):
		res = "{"
		for ll in self.array:
			for item in ll:
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
	h = SeparateChainingHash()
	h[0] = 1
	h[1] = 2
	print(h.contains(1))
	print(h.contains(0))
	print(h)




