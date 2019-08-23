
"""
Data too large to fit in main memory
Analogous to BTree
"""
class ExtendibleHash:

	def __init__(self):
		self.size = 0


	def __setitem__(self, key, val):
		pass

	def __getitem__(self, key):
		pass

	def __repr__(self):
		pass

	def __len__(self):
		return self.size

	def contains(self, key):
		pass

	def pop(self, key):
		pass



if __name__ == "__main__":
	h = ExtendibleHash()