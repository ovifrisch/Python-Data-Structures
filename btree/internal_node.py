from node import Node



"""
"""
class InternalNode(Node):
	def __init__(self, capacity, vals=[], first_child=None, parent=None):
		Node.__init__(self, capacity, vals, parent)
		self.first_child = first_child # m keys have m + 1 children
		# and each key is associated with a child > than it

	def get_min(self):
		return self.vals.get_min().key


	"""
	Insert an INodeData object into self.vals
	at the right location
	"""
	def insert_inode(self, inode):

		# impossible for node to be first child
		# because we are always keeping the minimum
		# split and inserting the bigger one.
		self.vals.insert(inode)

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
		inode_data = self.vals.get_node(key)
		first_child = False

		if (not inode_data):
			child = self.first_child
			first_child = True
		else:
			child = inode_data.child

		# insert into the child and update child
		child = child.insert(key, data)

		# not overflowing, all good
		if (len(child) <= child.capacity):
			return self

		# child is overflowing
		"""
		1. try adoption
		"""
		p = lambda x: x.child.is_overflow()
		q = lambda x: x.child.can_adopt()
		adoption_path = self.vals.get_optimal_adoption(p, q)
		print(adoption_path)



		return self

	def contains(self, key, data):
		inode = self.vals.get_node(key)
		if (not inode):
			child = self.first_child
		else:
			child = inode.child
		return child.contains(key, data)

	def remove(self, key, data):
		inode = self.vals.get_node(key)
		if (not inode):
			child = self.first_child
		else:
			child = inode.child
		return child.remove(key, data)