
class Queue:

	class Node:
		def __init__(self, val, prev=None, next=None):
			self.val = val
			self.prev = prev
			self.next = next

		def __isub__(self, i):
			curr = self
			while (i > 0):
				i -= 1
				curr = curr.prev
			return curr

	def __init__(self):
		self.size = 0
		self.tail = None
		self.head = None

	def enqueue(self, val):
		self.tail = self.Node(val, self.tail, None)
		if (not self.tail.prev):
			self.head = self.tail
		else:
			self.tail.prev.next = self.tail
		self.size += 1

	def dequeue(self):
		if (len(self) <= 0):
			raise Exception("Cannot dequeue from empty queue.")

		val = self.head.val
		if (not self.head.next):
			self.head = self.tail = None
		else:
			self.head = self.head.next
			self.head.prev = None
		self.size -= 1
		return val

	def __repr__(self):
		res = "["
		curr = self.tail
		while (curr):
			res += str(curr.val) + ", "
			curr -= 1
		if (len(res) > 1):
			res = res[:-2]

		return res + "]"


	def __len__(self):
		return self.size



if __name__ == "__main__":
	q = Queue()
	for i in range(10):
		q.enqueue(i)
	print(q)

	for i in range(10):
		q.dequeue()
		print(q)

