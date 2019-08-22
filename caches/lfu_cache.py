from ll import LinkedList
from dll import DLL
"""
tie break using LRU

use a linked list that contains:
	- a frequency
	- a doubly linked list of nodes having that frequency
		- each of these nodes has a value and points back to its outer linked list node

use a hash that maps keys to the doubly linked list nodes
"""
class LFUCache:

	class FreqListNode:
		def __init__(self, freq):
			self.freq = freq
			self.dll = DLL()

	class DataNode:
		def __init__(self, key, data, parent):
			self.data = data
			self.parent = parent
			self.key = key

	def __init__(self, capacity=3):
		self.capacity = capacity
		self.size = 0
		self.freq_list = LinkedList()
		self.hash = {}

	def put(self, key, data):
		if (key in self.hash):
			self.hash[key].data.data = data
			self.hash[key] = self.increase_frequency(self.hash[key])
			return

		if (self.size == self.capacity):
			evicted_data = self.freq_list[0].dll.pop_back()
			self.hash.pop(evicted_data.key)
			self.size -= 1



		if (len(self.freq_list) == 0):
			self.freq_list.append(self.FreqListNode(1))
		node = self.DataNode(key, data, self.freq_list.head)
		self.hash[key] = self.freq_list[0].dll.insert_front(node)
		self.size += 1

	def get(self, key):
		if (key not in self.hash):
			raise Exception("{} does not exist.can't get".format(key))

		dll_node = self.hash[key]
		data = dll_node.data.data
		self.hash[key] = self.increase_frequency(dll_node)
		return data


	def increase_frequency(self, data_node):
		# remove it from its parent
		parent = data_node.data.parent
		parent.data.dll.remove_node(data_node)
		if (not parent.next or parent.next.data.freq != parent.data.freq + 1):
			self.freq_list.insert_after(parent, self.FreqListNode(parent.data.freq + 1))

		# insert it
		new_data_node = self.DataNode(data_node.data.key, data_node.data.data, parent.next)
		parent.next.data.dll.insert_front(new_data_node)
		return parent.next.data.dll.head


if __name__ == "__main__":
	lfu = LFUCache(2)
	lfu.put(2, "y")
	lfu.put(3, "z")
	lfu.put(1, "x")
	lfu.get(1)
	lfu.get(1)
	lfu.get(1)
	lfu.put(4, "a")
	# lfu.put(5, "yy")
	# lfu.put(6, "zz")

	print(lfu.get(1))
	# print(lfu.get(2))
	# print(lfu.get(3))
	print(lfu.get(4))
	# print(lfu.get(4))






