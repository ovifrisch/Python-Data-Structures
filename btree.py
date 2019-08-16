from dll import DLL
from avl import AVL
import math


"""
Simple wrapper around internal keys
which contains the key and the child
it points to.

Necessary because we need to define
some operators over them used by
the AVL class
"""
class INodeData:
	"""
	need to define >, < and ==
	because AVL tree uses all these
	"""
	def __init__(self, key, child):
		self.key = key
		self.child = child

	def __lt__(self, other):
		return self.key < other.key

	def __eq__(self, other):
		return self.key == other.key

	def __gt__(self, other):
		return self.key > other.key

	def __repr__(self):
		return str(self.key)


"""
Inherits from AVL and implements
an extra method that allows us
to find the next child of the
btree to traverse over
"""
class BAVL(AVL):
	def __init__(self, data=[]):
		AVL.__init__(self, data)

	"""
	find the child to search
	each node is a (key, child) pair
	we want to find the node such that key >= node.key
	and key <= inorder_successor(node).key
	if node does not have an inorder successor, then return the node's child
	if there is no node such that key >= node.key, return None
	"""
	def get_child(self, key):
		self.child = None
		def helper(root):
			if (self.child or not root):
				return

			if (key >= root.val.key):
				if (root.right):
					helper(root.right)
				if (not self.child):
					self.child = root.val.child

			elif (key < root.val.key):
				helper(root.left)


		helper(self.root)
		return self.child



class Node:
	def __init__(self, capacity, parent=None):
		self.capacity = capacity
		self.parent = parent

	"""
	when called fron an internal node, the data is a key value pair
	where the key is the key and the value is a pointer to the child

	when called from a leafnode, the data is whatever data the BTree
	is storing
	"""

"""
"""
class InternalNode(Node):
	def __init__(self, capacity, vals=[], first_child=None, parent=None):
		Node.__init__(self, capacity)
		self.vals = BAVL(vals)
		self.first_child = first_child # m keys have m + 1 children
		# and each key is associated with a child > than it

	def get_child(self, key):
		child = vals.get_child(key)
		if (not child):
			child = self.first_child
		return child

	def insert(self, key, data):
		return self.get_child(key).insert(key, data)

	def contains(self, key, data):
		return self.get_child(key).contains(key, data)

"""
BTree Leaf Node
Internally uses an AVL tree for
efficient find/mutation operations
"""
class LeafNode:
	def __init__(self, capacity, vals=[], parent=None):
		Node.__init__(self, capacity)
		self.vals = AVL(vals)

	"""
	insert into the leaf
	can ignore the key if not overflow
	"""
	def insert(self, key, data):
		# check if already here
		if (self.vals.contains(data)):
			return False

		# no need for splitting
		if (len(self.vals) < self.capacity):
			self.vals.insert(data)
			return True

		# need to split
		## IMPLEMENT!!
		pass

	def contains(self, key, data):
		return self.vals.contains(data)

			


class BTree:
	def __init__(self, leaf_capacity, internal_node_capacity):
		self.size = 0
		self.L = leaf_capacity
		self.M = internal_node_capacity
		self.root = LeafNode(self.L) # initial btree contains a single leafnode & no parent

	"""
	we could be storing complex objects in here
	so map the object to a number than can be used as a key
	"""
	def __get_unique_key(self, data):
		# for now assume we are just storing integers, so
		# the key can be the data
		return data


	def insert(self, data):
		unique_key = self.__get_unique_key(data)
		if (self.root.insert(unique_key, data) is False):
			raise Exception("Value {} already exists".format(data))
		self.size += 1

	def remove(self, data):
		pass

	def contains(self, data):
		unique_key = self.__get_unique_key(data)
		return self.root.contains(unique_key, data)

	def __len__(self):
		return self.size

	def __repr__(self):
		return ""


if __name__ == "__main__":
	t = BTree(5, 5)
	for i in range(5):
		t.insert(i)

	for i in range(6):
		print(t.contains(i))









