
"""
a *max* heap has the property that each node is greater than its children
"""
import math

class DHeap:
	def __init__(self, has_priority, d):
		self.d = d
		self.has_priority = has_priority
		self.array = [None] * 10
		self.size = 0

	def find_min(self):
		if (self.size == 0):
			raise Exception("heap is empty")
		else:
			return self.array[0]


	def change_priority(self, priority):
		self.has_priority = priority
		elements = self.array[:self.size]
		self.size = 0
		for element in elements:
			self.insert(element)


	def resize_array(self):
		self.array = self.array + [None] * self.size

	def parent(self, idx):
		return math.ceil(idx / 2) - 1

	def percolate_up(self, hole, val):
		parent = self.parent(hole)
		# if no parents or heap order satisfied then insert here
		if (parent == -1 or self.has_priority(self.array[parent], val)):
			self.array[hole] = val
		else:
			self.array[hole] = self.array[parent]
			self.percolate_up(parent, val)


	def insert(self, val):
		if (len(self.array) == self.size):
			self.resize_array()

		self.array[self.size] = val
		self.size += 1
		self.percolate_up(self.size - 1, val)

	def child_indices(self, idx):
		children = []
		for i in range(idx*2 + 1, idx*2 + 1 + self.d):
			if (i >= self.size):
				break
			children.append(i)
		return children

	def percolate_down(self, hole, val):
		children = self.child_indices(hole)
		# no children, so you can just insert here
		if (not children):
			self.array[hole] = val
			return

		# at least 1 child

		# if greater than or equal to all children insert here
		can_insert = True
		for child in children:
			if (self.has_priority(self.array[child], val)):
				can_insert = False
				break
		if (can_insert):
			self.array[hole] = val
			return


		# find the maximum child, insert that value here, call percolate with the max child's index and same val
		max_val = self.array[children[0]]
		idx = children[0]
		for child in children:
			if (self.has_priority(self.array[child], max_val)):
				max_val = self.array[child]
				idx = child

		self.array[hole] = self.array[idx]
		self.percolate_down(idx, val)



	def remove_min(self):
		if (self.size == 0):
			raise Exception("heap is empty")

		m = self.array[0]
		val = self.array[self.size - 1]
		self.size -= 1
		self.percolate_down(0, val)
		return m

	def __len__(self):
		return self.size

	def __repr__(self):
		res = "["
		for i in range(self.size):
			res += str(self.array[i]) + ", "

		if (res[-1] == " "):
			res = res[:-2]
		return res + "]"




if __name__ == "__main__":

	def has_priority1(x, y):
		if (x > y):
			return True
		return False

	def has_priority2(x, y):
		if (x < y):
			return True
		return False

	heap = DHeap(has_priority2, 4)
	heap.insert(1)
	heap.insert(2)
	heap.insert(3)
	print(heap)

	heap.change_priority(has_priority1)
	print(heap)



