from dll import DLL

"""
Implemented using a Linked List
If an element is accessed, it is moved to the front of the list
elements at the end of the list are evicted first
"""

class LRUCache:

	def __init__(self, capacity):
		self.capacity = capacity
		self.hash = {}
		self.dll = DLL()
		self.size = 0

	"""
	Insert an element into the cache
	"""
	def put(self, key, data):
		# key already exists; update it and move it
		if (key in self.hash):
			self.hash[key].data['data'] = data
			self.move_front(self.hash[key])
			return

		# at capacity, pop from back
		if (self.size == self.capacity):
			popped_item = self.dll.pop_back()
			self.hash.pop(popped_item['key'])
			self.size -= 1

		# insert new item to front
		self.hash[key] = self.dll.insert_front({'key':key, 'data':data})
		self.size += 1

	"""
	Access an element in the cache
	"""
	def get(self, key):
		if (not key in self.hash):
			raise Exception("key does not exist")

		# move accesses to the front
		return self.move_front(self.hash[key])

	"""
	Move the node to the front of the list
	"""
	def move_front(self, node):
		key = node.data['key']
		data = node.data['data']
		self.dll.remove_node(node)
		self.hash[key] = self.dll.insert_front({'key':key, 'data':data})
		return data

if __name__ == "__main__":
	lru = LRUCache(2)
	lru.put(1, 'x')
	lru.put(2, 'y')
	lru.get(2)
	lru.get(2)
	lru.put(3, 'a')
	# print(lru.get(1))
	print(lru.get(2))









