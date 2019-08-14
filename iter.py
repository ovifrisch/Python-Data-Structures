


class MyList:
	def __init__(self, nums):
		self.nums = nums

	def __next__(self):
		if (self.start >= self.end):
			raise StopIteration
		else:
			self.start += 1
			return self.nums[self.start-1]

	def __iter__(self):
		self.start = 0
		self.end = len(self.nums)
		return self


nums = [1, 2, 3]
my_list = MyList(nums)
for x in my_list:
	print(x)