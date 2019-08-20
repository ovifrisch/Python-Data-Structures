

class MArySearchTree:

	class Node:
		def __init__(self, items=[{'key':-float('inf'), 'child':None}]):
			self.items = items

	def __init__(self, M):
		if (M < 2):
			raise Exception("M must be greater than 1.")
		self.size = 0
		self.M = M
		self.root = self.Node()

	def insert(self):
		pass

	def remove(self):
		pass

	"""
	find which subtree to search for data in
	"""
	def get_child(self, data, items):
		
		for i in range(len(items) - 1, -1, -1):
			if (data > items[i]['key']):
				return items[i]['child']

	def contains(self, data):
		
		def helper(root):
			nonlocal data
			if (root is None):
				return False
			elif (data in [x['key'] for x in root.items]):
				return True
			else:
				return helper(self.get_child(data, root.items))

		return helper(self.root)

	def __len__(self):
		return self.size

	def __repr__(self):
		return ""
