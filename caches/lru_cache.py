from dll import DLL

class LRUCache:

	def __init__(self, capacity):
		self.capacity = capacity
		self.hash = {}
		self.dll = DLL()
		self.size = 0

	def put(self, key, data):
		if (key in self.hash):
			self.hash[key].data['data'] = data
			self.access(self.hash[key])

		if (self.size == self.capacity):
			popped_item = self.dll.pop_front()
			self.hash.pop(popped_item['key'])
			self.size -= 1

		self.hash[key] = self.dll.insert_back({'key':key, 'data':data})
		self.size += 1

	def get(self, key):
		if (not key in self.hash):
			raise Exception("key does not exist")

		# move accesses to the front
		return self.access(self.hash[key])

	def access(self, node):
		key = node.data['key']
		data = node.data['data']
		self.dll.remove_node(node)
		self.hash[key] = self.dll.insert_front({'key':key, 'data':data})
		return data

if __name__ == "__main__":
	lru = LRUCache(2)
	lru.put(1, 'x')
	lru.put(2, 'y')
	lru.put(3, 'z')
	lru.put(4, 'a')
	# print(lru.get(1))
	print(lru.get(3))
	print(lru.get(4))









