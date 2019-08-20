
"""
Heap that allows for efficient merging
"""

class LeftistHeap:

	class Node:
		def __init__(self, data, npl=-1, left=None, right=None):
			self.data = data
			self.npl = npl
			self.left = left
			self.right = right

	def __init__(self, has_priority):
		self.root = None
		self.size = 0
		self.has_priority = has_priority

	def null_path_length(self, node):
		# null_path_length(X), of any node X to be the length of the shortest path from X to a node without two children.
		if (not node):
			return -1

		q = [{"node":node, "npl":0}]

		while (q):
			fq = q.pop(0)
			if (not fq['node'].left or not fq['node'].right):
				return fq['npl']
			q.append({'node':fq.right, 'npl':fq['npl'] + 1})
			q.append({'node':fq.left, 'npl':fq['npl'] + 1})


	def get_nlp(self, node):
		if (not node):
			return -1
		return node.nlp


	def insert(self, data):
		pass

	def get_min(self):
		if (len(self) == 0):
			raise Exception("Cannot get min of empty heap")
		return self.head.data

	def remove_min(self, data):
		pass


	"""
	recursively merge the heap with the larger root with the right subheap of the heap with the smaller root.
	"""
	def merge_recursive(self, small, big):
		if (not small):
			return big
		if (not big):
			return small
		if (not small.right):
			small.right = big
		elif (small.right.get_min() < big.get_min()):
			small.right = self.merge_recursive(small.right, big)
		else:
			small.right = self.merge_recursive(big, small.right)

		if (self.get_nlp(small.left) < self.nlp(small.right)):
			temp = small.left
			small.left = small.right
			small.right = temp
			small.nlp = 1 + self.get_nlp(small.right)
		return small

	def merge(self, other):
		if (len(self) == 0):
			return other
		elif (len(other) == 0):
			return self
		elif (self.get_min() < other.get_min()):
			small = self
			big = other
		else:
			small = other
			big = self
		return self.merge_recursive(small, big)

	def is_valid(self):
		pass


	def __len__(self):
		return self.size

	def __repr__(self):
		res = ""
		return res

