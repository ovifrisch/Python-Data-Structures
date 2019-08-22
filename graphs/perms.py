import itertools

def get_permutations(nums):
	res = []
	def helper(curr, nums):
		if (not nums):
			return res.append(curr)

		for i in range(len(nums)):
			helper(curr + [nums[i]], nums[:i] + nums[i+1:])

	helper([], nums)
	return res

x = get_permutations([1, 2, 3])
print(len(x))

print(len(list(itertools.permutations([1, 2, 3]))))
