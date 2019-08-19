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