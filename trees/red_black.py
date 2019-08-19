

class RedBlackTree:

	class Node:
		def __init__(self, data, color, left=None, right=None):
			self.data = data
			self.color = color # red or black
			self.left = left
			self.right = right

	def __init__(self):
		self.size = 0

	def insert(self, data):
		pass

	def remove(self, data):
		pass

	def contains(self, data):
		pass

	def __len__(self):
		return self.size

	def __repr__(self):
		return ""



if __name__ == "__main__":
	t = RedBlackTree()

