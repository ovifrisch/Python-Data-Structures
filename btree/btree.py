from bavl import BAVL
from leaf_node import LeafNode
import math
from inode_data import INodeData


class BTree:
	def __init__(self, leaf_capacity, internal_node_capacity):
		self.size = 0
		self.L = leaf_capacity
		self.M = internal_node_capacity
		self.root = LeafNode(self.L, self.M) # initial btree contains a single leafnode & no parent

	"""
	we could be storing complex objects in here
	so map the object to a number than can be used as a key
	"""
	def get_key(self, data):
		# for now assume we are just storing integers, so
		# the key can be the data
		return data


	def insert(self, data):
		key = self.get_key(data)
		self.root = self.root.insert(key, data)
		self.size += 1

	def remove(self, data):
		key = self.get_key(data)
		self.root = self.root.remove(key, data)
		if (not self.root):
			raise Exception("Value {} does not exist".format(data))
		self.size -= 1

	def contains(self, data):
		key = self.get_key(data)
		return self.root.contains(key, data)

	def __len__(self):
		return self.size

	def __repr__(self):
		return ""


if __name__ == "__main__":
	t = BTree(5, 5)
	for i in range(9):
		t.insert(i)

	for i in range(9):
		print(t.contains(i))









