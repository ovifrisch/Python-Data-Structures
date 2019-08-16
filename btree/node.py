from bavl import BAVL


class Node:
	def __init__(self, capacity, vals=[], parent=None):
		self.capacity = capacity
		self.parent = parent
		self.vals = BAVL(vals)

	def __len__(self):
		return len(self.vals)

	def is_overflow(self):
		return len(self.vals) > self.capacity

	def can_adopt(self):
		return len(self.vals) < self.capacity