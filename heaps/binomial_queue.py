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




	def __init__(self, has_priortiy=None, queue=None):
		if (not queue):
			self.queue = [] # sorted list (by height) of binomial trees
		else:
			queue = queue
		self.has_priortiy = has_priortiy

	def insert(self, data):
		one_node_queue = BinomialQueue(queue=[self.BinomialTree(self.Node(data), 0, self.has_priortiy)])
		self.merge(one_node_queue)


	def is_valid_queue(self):
		# make sure the queue is in sorted order
		for i in range(0, len(self.queue) - 1):
			if (self.queue[i].k > self.queue[i+1].k):
				return False
		return True

	def remove_min(self, data):
		pass

	def merge(self, other):
		q3 = [] # the merged queue
		q1 = self.queue
		q2 = other.queue

		def helper(idx1, idx2):
			nonlocal q1, q2, q3

			# potentially merge with q3[-1]
			def merge_tree(tree):
				nonlocal q3
				if (q3 != [] and q3[-1].k == tree.k):
					tree.merge(q3.pop(-1))
				q3.append(tree)


			# mo more trees to merge
			if (idx1 >= len(q1) and idx2 >= len(q2)):
				return

			# trees left in q1
			elif (idx2 >= len(q2)):
				merge_tree(q1[idx1])
				idx1 += 1

			# trees left in q2
			elif (idx1 >= len(q1)):
				merge_tree(q2[idx2])
				idx2 += 1

			# trees left in both
			else:
				# if the trees have the same height, merge them together
				if (q1[idx1].k == q2[idx2].k):
					q1[idx1].merge(q2[idx2])
					q3.append(q1)
				else:
					small_tree, idx1, idx2 = (
						q1[idx1], idx1+1, idx2
						if q1[idx1].k < q2[idx2].k
						else q2[idx2], idx1, idx2+1
					)

					merge_tree(small_tree)

			helper(idx1, idx2)

		helper(0, 0)
		self.queue = q3



	def __len__(self):
		pass

	def __repr__(self):
		pass


if __name__ == "__main__":
	priority = lambda x, y: x < y
	bq = BinomialQueue(priority)
	bq.insert(2)

