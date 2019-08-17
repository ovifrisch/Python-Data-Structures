import internal_node
from node import Node
from inode_data import INodeData

"""
BTree Leaf Node
Internally uses an AVL tree for
efficient find/mutation operations
"""
class LeafNode(Node):
	def __init__(self, capacity, internal_node_capacity, vals=[], parent=None):
		Node.__init__(self, capacity, vals, parent)
		
		# only used to create a new root when leaf is full and has no parent
		self.internal_node_capacity = internal_node_capacity

	def get_key(self, data):
		# for now assume we are just storing integers, so
		# the key can be the data
		return data


	def create_leaf(self, vals):
		return LeafNode(self.capacity, self.internal_node_capacity, vals)
	"""
	insert into the leaf
	can ignore the key if not overflow
	"""
	def insert(self, key, data):
		# check if already here
		if (self.vals.contains(data)):
			raise Exception("Value {} already exists".format(data))

		# insert the value
		self.vals.insert(data)

		"""
		if we have gone over capacity, the parent
		will take care of it. However if there is
		no parent, we must take care of it here.
		"""

		# parent or not overflowing
		if (self.parent or len(self) <= self.capacity):
			return self

		# no parent and overflowing
		inorder_vals = self.vals.inorder()
		split = len(inorder_vals) // 2
		leaf1 = self.create_leaf(inorder_vals[:split])
		leaf2 = self.create_leaf(inorder_vals[split:])
		parent_left = INodeData(-float('inf'), leaf1)
		parent_right = INodeData(self.get_key(leaf2.vals.get_min()), leaf2)
		parent = internal_node.InternalNode(self.internal_node_capacity, self.capacity, [parent_left, parent_right])
		leaf1.parent = parent
		leaf2.parent = parent
		return parent



	def contains(self, key, data):
		return self.vals.contains(data)

	def remove(self, key, data):
		if (not self.vals.contains(data)):
			raise Exception("Value {} does not exist".format(data))
		self.vals.remove(data)
		return self

