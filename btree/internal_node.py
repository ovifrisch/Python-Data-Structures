from node import Node
from inode_data import INodeData
import leaf_node

"""
"""
class InternalNode(Node):
	def __init__(self, capacity, leaf_node_capacity, vals=[], parent=None):
		Node.__init__(self, capacity, vals, parent)
		self.leaf_node_capacity = leaf_node_capacity

	def create_leaf(self, vals, parent=None):
		return leaf_node.LeafNode(self.leaf_node_capacity, self.capacity, vals, parent)

	def create_internal(self, vals, parent=None):
		return InternalNode(self.capacity, self.leaf_node_capacity, vals, parent)


	def get_min_leaf(self, inode):
		child = inode.child
		if (isinstance(child, InternalNode)):
			return self.get_min_leaf(child.vals.get_min())
		return child.vals.get_min()


	"""
	path : List(INodeData)
		- the path to adopt the child at path[0]


	for each INode in path, access the child.
	then remove the maximum val/inode from this child.
	if it's an inode, set its key to -inf. 

	remove the minimum val/inode from the child of the next inode
	if it's an int, put it back
	if it's an inode, find the minimum value and set the key to this
	then put it back
	"""
	def adopt_right(self, path):
		for i in range(len(path) - 1):
			child = path[i].child
			max_ = child.vals.remove_max()
			if (isinstance(max_, INodeData)):
				max_.key = -float('inf')
				path[i+1].key = self.get_min_leaf(max_)
			else:
				path[i+1].key = max_


			next_child = path[i+1].child
			min_ = next_child.vals.remove_min()
			if (isinstance(min_, INodeData)):
				min_.key = self.get_min_leaf(min_)
			next_child.vals.insert(min_)
			next_child.vals.insert(max_)


	"""
	path : List(INodeData)
		- the path to adopt the child at path[-1]

	for each inode in path access the child
	then remove the minimum inode/val from this child
	if its an inode, set its key to be the minimum value in the child

	remove again from the current node.
	if its an inode, set its key to -inf
	put it back

	insert the first removed inode in the previous node
	"""
	def adopt_left(self, path):
		for i in range(len(path) - 1, 0, -1):
			child = path[i].child
			min_ = child.vals.remove_min()
			if (isinstance(min_, INodeData)):
				min_.key = self.get_min_leaf(min_)


			min2 = child.vals.remove_min()
			if (isinstance(min2, INodeData)):
				path[i].key = self.get_min_leaf(min2)
				min2.key = -float('inf')
			else:
				path[i].key = min2
			child.vals.insert(min2)

			prev_child = path[i-1].child
			prev_child.vals.insert(min_)

	"""
	The child associcated with "key" has an extra child. We
	attempt to find a child of this node that has room for it.
	"""
	def adopt(self, key):
		p = lambda x: x.child.is_overflow()
		q = lambda x: x.child.can_adopt()

		# adoption paths, returns inodes
		path = self.vals.get_optimal_adoption(p, q)
		# can't adopt
		if (len(path) <= 1):
			return False

		if (key == path[0].key):
			self.adopt_right(path)
		else:
			self.adopt_left(path)

		return True

	"""

	"""
	def split(self, node):
		inorder_vals = node.vals.inorder()
		split = len(inorder_vals) // 2
		if (isinstance(inorder_vals[0], int)):
			small = self.create_leaf(inorder_vals[:split], self)
			big = self.create_leaf(inorder_vals[split:], self)
		else:
			small = self.create_internal(inorder_vals[:split], self)
			big = self.create_internal(inorder_vals[split:], self)
		return small, big

	"""
	Internal Node Insert
	--------------------

	We call the insert method on the appropriate child,
	updating the child via the return value. Once we get
	to a leaf node, the leaf node blindly inserts the data.
	This may cause an overflow which we handle here by first
	trying to put the child up for adotion, and then if that
	fails, we split the child, add the extra child to our
	children (even if it overflows) because the parent will
	deal with it. If we reach the root and there is an overflow
	in the child, create a new root, split the existing root,
	and set the two split roots as children of the new root.
	"""
	def insert(self, key, data):
		# insert into the child and update child
		inode = self.vals.get_node(key)
		child = inode.child
		child = child.insert(key, data)

		# not overflowing, all good
		if (len(child) <= child.capacity):
			return self

		# child is overflowing
		"""
		1. try adoption
		"""

		# success

		if(self.adopt(inode.key)):
			return self

		# failure; need to split
		small, big = self.split(child)
		inode.child = small
		# get the minimum and set its key to -inf
		the_min = big.vals.remove_min()
		if (isinstance(the_min, INodeData)):
			the_min.key = -float('inf')
		big.vals.insert(the_min)

		big_key = big.vals.get_min()
		if (isinstance(big_key, INodeData)):
			big_key = self.get_min_leaf(big_key)

		big_inode = INodeData(big_key, big)
		self.vals.insert(big_inode)

		if (self.parent or not self.is_overflow()):
			return self

		# need to create new parent
		small, big = self.split(self)
		big_key = self.get_min_leaf(big.vals.get_min()) # always going to be an internal node
		min_inode = big.vals.remove_min()
		min_inode.key = -float('inf')
		big.vals.insert(min_inode)
		parent_left = INodeData(-float('inf'), small)
		parent_right = INodeData(big_key, big)
		parent = self.create_internal(vals=[parent_left, parent_right])
		small.parent = parent
		big.parent = parent
		return parent

	def contains(self, key, data):
		return self.vals.get_node(key).child.contains(key, data)

	def remove(self, key, data):
		inode = self.vals.get_node(key)
		child = inode.child
		child = child.remove(key, data)

		"""
		length of the inode's child is greater than zero
		"""
		if (isinstance(child, leaf_node.LeafNode) and len(child) > 0):
			min_leaf = self.get_min_leaf(inode)
			if (min_leaf > inode.key and inode.key != -float('inf')):
				inode.key = min_leaf
			return self

		elif (isinstance(child, InternalNode) and len(child) > 1):
			min_leaf = self.get_min_leaf(inode)
			if (min_leaf > inode.key and inode.key != -float('inf')):
				inode.key = min_leaf
			return self

		else:
			if (isinstance(child, InternalNode)):
				if (inode.key != -float('inf')):
					new_key = self.get_min_leaf(inode)
					inode.key = new_key
				inode.child = inode.child.vals.get_min().child
			else:
				self.vals.remove(inode)
				min_ = self.vals.remove_min()
				min_.key = -float('inf')
				self.vals.insert(min_)


		if (not self.parent):
			if (len(self) > 1):
				return self
			return self.vals.remove_min().child

		return self

		# """
		# length of the inode's child is equal to zero
		# need to delete it
		# """
		# self.vals.remove(inode.key)

		# # now the parent would check if this node has zero children and proceed to
		# # delete it until we reach the root. but if this is the root, and we have gone
		# # to 0, we set the new root 

		# if (not parent):
			



































