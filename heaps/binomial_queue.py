import random

class BinomialQueue:

	class Node:
		def __init__(self, data, children=None):
			self.data = data
			if (not children):
				children = []
			else:
				children = children

	class BinomialTree:
		def __init__(self, root, k, has_priortiy):
			self.root = root
			self.k = k

		def merge(self, other):
			if (self.k != other.k or not self.root or not other.root):
				raise Exception("Error merging binomial trees because of None roots or height differences")

			if (self.has_priortiy(self.root.data, other.root.data)):
				self.root.children.append(other.root)
			else:
				other_cpy = copy.copy(other)
				other_cpy.root.children.append(self.root)
				self.root = other_cpy
			self.k += 1




	def __init__(self, has_priortiy):
		self.queue = [] # sorted list (by height) of binomial trees
		self.has_priortiy = has_priortiy

	def insert(self, data):
		pass

	def remove_min(self, data):
		pass

	def merge(self, other):
		q3 = [] # the merged queue
		q1 = self.queue
		q2 = other.queue

		def helper(idx1, idx2):

			# mo more trees to merge
			if (idx1 >= len(q1) and idx2 >= len(q2)):
				return

			# trees left in q1
			elif (idx2 >= len(q2)):
				if (q3 == [] or q3[-1].k != q1[idx1].k):
					# just add this one over
					q3.append(q1[idx1])
				else:
					# merge with last tree of q3
					q1[idx1].merge(q3.pop(-1))
					q3.append(q1[idx1])
				idx1 += 1

			# trees left in q2
			elif (idx1 >= len(q1)):
				if (q3 == [] or q3[-1].k != q2[idx2].k):
					# just add this one over
					q3.append(q2[idx2])
				else:
					# merge with last tree of q3
					q2[idx2].merge(q3.pop(-1))
					q3.append(q2[idx2])
				idx2 += 1

			# trees left in both
			else:
				# if the trees have the same height, merge them together
				if (q1[idx1].k == q2[idx2].k):
					q1[idx1].merge(q2[idx2])
					q3.append(q1)
				else:
					if (q1[idx1].k < q2[idx2].k):
						small_tree = q1[idx1]
						idx1 += 1
					else:
						small_tree = q2[idx2]
						idx2 += 1

					if (q3 == [] or q3[-1].k != small_tree.k):
						q3.append(small_tree)
					else:
						small_tree.merge(q3.pop(-1))
						q3.append(small_tree)
						
			helper(idx1, idx2)

		helper(0, 0)
		self.queue = q3



	def __len__(self):
		pass

	def __repr__(self):
		pass


if __name__ == "__main__":
	bq = BinomialQueue()