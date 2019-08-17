from bavl import BAVL
import leaf_node
import internal_node
import math
from inode_data import INodeData
import random


class BTree:
	def __init__(self, leaf_capacity, internal_node_capacity):
		self.size = 0
		self.L = leaf_capacity
		self.M = internal_node_capacity
		self.root = leaf_node.LeafNode(self.L, self.M) # initial btree contains a single leafnode & no parent

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
		self.size -= 1

	def contains(self, data):
		key = self.get_key(data)
		return self.root.contains(key, data)

	def __len__(self):
		return self.size

	"""
	level order travsersal
	"""
	def __repr__(self):
		q = [self.root]
		res = ""
		prev = -float('inf')
		while (q):
			node = q.pop(0)
			if (len(node) == 0):
				res += str([])
			elif (isinstance(node, leaf_node.LeafNode)):
				if (len(node) > 0 and node.vals.get_min() < prev):
					res += "\n"
				prev = node.vals.get_max()
				res += str(node.vals.inorder()) + ",   "
			else:
				the_min = node.vals.get_max().key
				if (the_min < prev):
					res += "\n"
				prev = the_min
				res += str([x.key for x in node.vals.inorder()]) + ",   "
				inorder = node.vals.inorder()
				for inode in inorder:
					q.append(inode.child)
		return res


if __name__ == "__main__":
	t = BTree(leaf_capacity=3, internal_node_capacity=3)
	for i in range(15):
		t.insert(i)

	for i in range(14, -1, -1):
		print("removing {}...".format(i))
		t.remove(i)
		print(t)

	# print(t)
	# t.remove(0)
	# print(t)
	# t.remove(1)
	# print(t)
	# t.remove(2)
	# print(t)
	# t.remove(3)
	# print(t)
	# t.remove(4)
	# print(t)
	# t.remove(5)
	# print(t)
	# t.remove(6)
	# print(t)

	# pool = list(range(1000))
	# nums = []
	# while (pool):
	# 	nums.append(pool.pop(random.randint(0, len(pool) - 1)))
	# for num in nums:
	# 	t.insert(num)

	# for num in nums:
	# 	if (not t.contains(num)):
	# 		print("fuck")

	# print("yay :)")










