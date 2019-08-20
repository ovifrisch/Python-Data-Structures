

import copy
import random
"""
Heap that allows for efficient merging
Identical to Skew Heap except after we merge two nodes,
we swap them unconditionally, except when the node does
not have a right child. skew heaps are to lefist heaps
as splay trees are to avl trees. they have O(MlogN) amortized
cost/operation.
"""

class SkewHeap:

	class Node:
		def __init__(self, data, left=None, right=None):
			self.data = data
			self.left = left
			self.right = right
			self.size = 1
			if (left):
				self.size += left.size
			if (right):
				self.size += right.size

	def __init__(self, has_priority, root=None):
		self.root = root
		self.has_priority = has_priority

	def contains(self, data):
		def helper(root):
			if (not root):
				False
			elif (root.data == data):
				return True
			return helper(root.left) or helper(root.right)

		return helper(self.root)


	def insert(self, data):
		one_element_heap = SkewHeap(self.has_priority, self.Node(data))
		self.merge(one_element_heap)

	def remove_min(self):
		if (len(self) == 0):
			raise Exception("Cannot remove min from an empty heap")

		data = self.root.data
		if (not self.root.left):
			self.root = self.root.right
		elif (not self.root.right):
			self.root = self.root.left
		elif (self.has_priority(self.root.left.data, self.root.right.data)):
			self.root = self.merge_recursive(self.root.left, self.root.right)
		else:
			self.root = self.merge_recursive(self.root.right, self.root.left)
		return data

	def get_top(self):
		if (len(self) == 0):
			raise Exception("Cannot get min of empty heap")
		return self.root.data

	def get_size(self, node):
		if (not node):
			return 0
		return node.size


	"""
	recursively merge the heap with root less priority (p2)
	with the right subheap of the heap with root of more priority
	"""
	def merge_recursive(self, p1, p2):
		if (not p1):
			return p2
		if (not p2):
			return p1
		if (not p1.right):
			p1.right = p2
		elif (self.has_priority(p1.right.data, p2.data)):
			p1.right = self.merge_recursive(p1.right, p2)
		else:
			p1.right = self.merge_recursive(p2, p1.right)

		p1.size = 1 + self.get_size(p1.left) + self.get_size(p1.right)

		if (p1.right):
			temp = p1.left
			p1.left = p1.right
			p1.right = temp
		return p1

	def merge(self, other_):
		other = copy.deepcopy(other_)
		if (len(self) == 0):
			self.root = other.root
			return
		elif (len(other) == 0):
			return
		elif (self.has_priority(self.get_top(), other.get_top())):
			self.root = self.merge_recursive(self.root, other.root)
		else:
			self.root = self.merge_recursive(other.root, self.root)


	"""
	heap order property is maintained
	"""
	def is_valid(self):
		valid = True

		def heap_order(root):
			nonlocal valid
			if (not root):
				return

			valid_left = not root.left or self.has_priority(root.data, heap_order(root.left))
			valid_right = not root.right or self.has_priority(root.data, heap_order(root.right))

			if (not (valid_left and valid_right)):
				valid = False
				
			return root.data

		heap_order(self.root)
		return valid

	def __len__(self):
		if (not self.root):
			return 0
		return self.root.size

	"""
	inorder traversal
	"""
	def __repr__(self):
		if (not self.root):
			return "[]"

		q = [self.root]

		res = "["

		while (q):
			x = q.pop(0)
			if (not x):
				res += "None, "

			else:
				res += "{}, ".format(str(x.data))
				if (x.left or x.right):
					q.append(x.left)
					q.append(x.right)

		res = res[:-2] + "]"
		return res

"""
"""
if __name__ == "__main__":
	priority = lambda x, y: x < y
	heap1 = SkewHeap(priority)
	heap2 = SkewHeap(priority)

	nums1 = list(range(-100, 100))
	nums2 = list(range(-300, -200)) + list(range(200, 300))

	while (nums1):
		heap1.insert(nums1.pop(random.randint(0, len(nums1) - 1)))

	while (nums2):
		heap2.insert(nums2.pop(random.randint(0, len(nums2) - 1)))

	print(heap1.is_valid())
	print(heap2.is_valid())
	print(len(heap1))
	print(len(heap2))

	heap1.merge(heap2)
	print(heap1.is_valid())
	print(len(heap1))

	print(heap2.is_valid())
	print(len(heap2))

	while (len(heap1) > 0):
		heap1.remove_min()

	print(heap1)








