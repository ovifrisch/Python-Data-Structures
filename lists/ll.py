
"""
Linked List implementation with an
Interface like a Python List
"""
class LinkedList:

	class Node:
		def __init__(self, data, next=None):
			self.data = data
			self.next = next

		def __iadd__(self, i):
			curr = self
			while (i > 0):
				i -= 1
				curr = curr.next
			return curr

	def __init__(self, data=[]):
		self.head = None
		self.init_list(data)


	def init_list(self, data):
		for i in range(len(data) -1, -1, -1):
			self.head = self.Node(data[i], self.head)
		self.size = len(data)

	"""
	append data to the end of the list
	"""
	def append(self, data):
		if (not self.head):
			self.head = self.Node(data)
			self.size += 1
			return

		curr = self.head
		while (curr.next):
			curr += 1
		curr.next = self.Node(data)
		self.size += 1

	"""
	get the index of the first instance of data
	"""
	def index(self, data):
		res = -1
		idx = 0
		curr = self.head
		while (curr):
			if (data == curr.data):
				res = idx
				break
			idx += 1
			curr += 1
		return res


	"""
	insert data at the given position
	"""
	def insert(self, idx, data):
		if (idx > len(self) or idx < -len(self) - 1):
			raise Exception("Index {} out of bounds".format(idx))

		if (idx < 0):
			idx = len(self) + idx + 1

		if (idx == 0):
			self.head = self.Node(data, self.head)
			self.size += 1
			return

		curr = self.head
		while (idx > 1):
			idx -= 1
			curr += 1
		temp = curr.next
		curr.next = self.Node(data, temp)
		self.size += 1


	"""
	remove the first instance of data
	"""
	def remove(self, data):
		if (not self.head):
			raise Exception("{} not in list".format(data))
		if (self.head.data == data):
			self.head = self.head.next
			return

		curr = self.head
		while (curr.next):
			if (curr.next.data == data):
				curr.next += 1
				self.size -= 1
				return
			curr += 1
		raise Exception("{} not in list".format(data))

	"""
	remove and return the element at the given index
	"""
	def pop(self, idx):
		if (idx >= len(self) or idx < -len(self)):
			raise Exception("Index {} out of bounds".format(idx))

		if (idx < 0):
			idx = len(self) + idx

		if (idx == 0):
			val = self.head.data
			self.head = self.head.next
			self.size -= 1
			return val

		curr_idx = 1
		curr = self.head
		while (1):
			if (curr_idx == idx):
				val = curr.next.data
				curr.next += 1
				self.size -= 1
				return val
			curr_idx += 1
			curr += 1



	"""
	remove all the elements of the list
	"""
	def clear(self):
		self.head = None
		self.size = 0

	"""
	the number of instances of data in the list
	"""
	def count(self, data):
		count = 0
		curr = self.head
		while (curr):
			if (curr.data == data):
				count += 1
			curr += 1
		return count

	"""
	sort the list in place (insertion sort for now)
	"""
	def sort(self):
		if (not self.head):
			return None

		def insert(data):
			if (data < self.head.data):
				self.head = self.Node(data, self.head)
				return

			curr = self.head
			while (curr.next.data < data):
				curr += 1
			temp = curr.next
			curr.next = self.Node(data, temp)


		curr = self.head
		while (curr.next):
			if (curr.next.data < curr.data):
				insert(curr.next.data)
				curr.next += 1
			else:
				curr += 1





	def __getitem__(self, idx):
		if (idx >= len(self) or idx < -len(self)):
			raise Exception("Index {} out of bounds".format(idx))

		if (idx < 0):
			idx = len(self) + idx

		curr_idx = 0
		curr = self.head
		while (idx > curr_idx):
			idx -= 1
			curr += 1
		return curr.data


	def __len__(self):
		return self.size

	def __repr__(self):
		res = "["
		curr = self.head
		while (curr):
			res += str(curr.data) + ", "
			curr += 1
		if (len(res) > 1):
			res = res[:-2]
		return res + "]"
		


if __name__ == "__main__":
	x = LinkedList([1, 2, 3, 4])
	print(x)






