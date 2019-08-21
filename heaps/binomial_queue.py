import random
import copy

class BinomialQueue:

	class Node:
		def __init__(self, data):
			self.data = data
			self.children = []

	class BinomialTree:
		def __init__(self, root, k, has_priortiy):
			self.root = root
			self.k = k
			self.has_priortiy = has_priortiy

		def merge(self, other):
			if (self.k != other.k or not self.root or not other.root):
				raise Exception("Error merging binomial trees because of None roots or height differences")

			if (self.has_priortiy(self.root.data, other.root.data)):
				self.root.children.append(other.root)
			else:
				other_cpy = copy.copy(other)
				other_cpy.root.children.append(self.root)
				self.root = other_cpy.root
			self.k += 1

		def get_top(self):
			if (not self.root):
				raise Exception("cannot get top of empty tree")
			return self.root.data




	def __init__(self, has_priortiy=None, lone_tree=None):
		if (not lone_tree):
			self.queue = [] # sorted list (by height) of binomial trees
		else:
			self.queue = [lone_tree]
		self.has_priortiy = has_priortiy
		self.hash = {}

	def set_queue(self, q):
		self.queue = q

	def contains(self, data):
		return data in self.hash

	def insert(self, data):
		if (data in self.hash):
			raise Exception("cannot insert {} because it already exists".format(data))

		self.hash[data] = True
		one_node_queue = BinomialQueue(lone_tree=self.BinomialTree(self.Node(data), 0, self.has_priortiy))
		self.merge(one_node_queue)
		self.size += 1


	def is_valid_queue(self):
		# make sure the queue is in sorted order
		for i in range(0, len(self.queue) - 1):
			if (self.queue[i].k > self.queue[i+1].k):
				return False
		return True

	def remove_min(self, data):
		
		def smallest_idx():
			if (len(self.queue) == 0):
				raise Exception("Cannot get smallest idx from empty queue")
			"""
			get the index in the queue containing the smallest element
			"min" assuming small elements have priority
			"""
			min_val = self.queue[0].get_top()
			min_idx = 0
			for i in range(1, len(self.queue)):
				if (self.has_priortiy(self.queue[i].get_top(), min_val)):
					min_val = self.queue[i].get_top()
					min_idx = i

			return min_idx

		def get_children(tree):
			"""
			get all the children of this tree
			(they should be in sorted order)
			"""
			children = []
			for i in range(len(tree.root.children)):
				children.append(self.BinomialTree(children[i]), i, self.has_priortiy)
			return children

		if (data not in self.hash):
			raise Exception("cannot remove {} because it does not exist".format(data))

		self.hash.pop(data) # remove from hash
		min_idx = smallest_idx()
		popped_tree = self.queue.pop(min_idx) # remove the tree
		to_merge = BinomialQueue(has_priortiy=self.has_priortiy)
		to_merge.set_queue(get_children(popped_tree)) # add popped's node's children
		self.merge(to_merge)
		self.size -= 1

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
					q3.append(q1[idx2])
					idx1 += 1
					idx2 += 1
				else:
					if (q1[idx1].k < q2[idx2].k):
						small_tree = q1[idx1]
						idx1 += 1
					else:
						small_tree = q2[idx2]
						idx2 += 1

					merge_tree(small_tree)

			helper(idx1, idx2)

		helper(0, 0)
		self.queue = q3



	def __len__(self):
		return self.size()

	def __repr__(self):
		pass


if __name__ == "__main__":
	priority = lambda x, y: x < y
	bq = BinomialQueue(priority)


	nums = list(range(0, 1000))
	while (nums):
		num = nums.pop(random.randint(0, len(nums) - 1))
		bq.insert(num)
		print("inserted {}".format(num))

	print(bq.is_valid_queue())







