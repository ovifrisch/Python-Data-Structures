import random

class SkipList:

	class Node:
		# nexts[0] denotes the bottom level
		def __init__(self, val, nexts=[]):
			self.nexts = nexts
			self.val = val

	def __init__(self, levels):
		self.size = 0
		front = self.Node(-float('inf'))
		self.back = self.Node(float('inf'), nexts=[None] * levels)
		front.nexts = [self.back] * levels
		self.root = front
		self.levels = levels

	def decide(self, level):
		x=1/pow(2, level)
		y = random.random()
		return y <= x


	def insert(self, val):

		new_node = self.Node(val, [None] * self.levels)

		def helper(val, level, start, guaranteed_insert):
			if (level < 0):
				return
			elif (not guaranteed_insert and not self.decide(level)):
				helper(val, level - 1, start, False)
			else:
				curr = start
				while (1):
					if (val < curr.nexts[level].val):
						temp = curr.nexts[level]
						curr.nexts[level] = new_node
						new_node.nexts[level] = temp
						return helper(val, level - 1, curr, True)

					curr = curr.nexts[level]


		helper(val, self.levels - 1, self.root, False)
		self.size += 1


	def remove(self, target):

		def helper(target, level, current):

			if (level < 0):
				self.size -= 1
				return
			# reached the end of the current level
			elif (not current.nexts[level]):
				if (level == 0):
					raise Exception("Value not found")
				return helper(val, level - 1, current)

			elif (current.nexts[level].val == target):
				current.nexts[level] = current.nexts[level].nexts[level]
				return helper(target, level - 1, current)

			elif (current.nexts[level].val < target):
				return helper(target, level, current.nexts[level])

			else:
				return helper(target, level - 1, current)
		
		return helper(target, self.levels - 1, self.root)

	def contains(self, val):
		def helper(current, target, level, back):
			if (current.val == target):
				return True

			if (level == 0):
				if (target < current.val or current.val == back.val):
					return False
				else:
					return helper(current.nexts[level], target, level, back)


			if (target > current.nexts[level].val):
				return helper(current.nexts[level], target, level, self.back)
			else:
				return helper(current, target, level - 1, current.nexts[level])

		return helper(self.root, val, self.levels - 1, self.back)

	def __len__(self):
		return self.size

	def __repr__(self):
		res = "["
		curr = self.root.nexts[0]
		while (curr.nexts[0]):
			res += str(curr.val) + ", "
			curr = curr.nexts[0]

		if (res[-1] == " "):
			res = res[:-2]
		return res + "]"


if __name__ == "__main__":
	sl = SkipList(4)
	sl.insert(2)
	sl.insert(5)
	sl.insert(8)
	print(sl)
	print(len(sl))
	sl.remove(5)
	print(sl)
	print(len(sl))



