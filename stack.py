

class Stack:

	class Node:
		def __init__(self, val, next):
			self.val = val
			self.next = next

		def __iadd__(self, i):
			curr = self
			while (i > 0):
				i -= 1
				curr = curr.next
			return curr

	def __init__(self):
		self.size = 0
		self.head = None

	def push(self, val):
		self.head = self.Node(val, self.head)
		self.size += 1

	def pop(self):
		if (len(self) <= 0):
			raise Exception("Cannot pop from empty stack")

		val = self.head.val
		self.head += 1
		self.size -= 1
		return val

	def __len__(self):
		return self.size

	def __repr__(self):
		res = "["
		curr = self.head
		while (curr):
			res += str(curr.val) + ", "
			curr += 1

		if (len(res) > 1):
			res = res[:-2]
		return res + "]"


if __name__ == "__main__":
	stack = Stack()
	for i in range(10):
		stack.push(i)
	print(stack)

	for i in range(10):
		stack.pop()
		print(stack)
