import random
import copy

class MArySearchTree:

	class Node:
		"""
		we are responsible for keeping the keys in sorted order
		"""
		def __init__(self):
			self.items = [{'key': -float('inf'), 'child':None}]


		"""
		find the position to place key using binary search
		"""
		def add_key(self, key):
			left = list(filter(lambda x: x['key'] < key, self.items))
			right = list(filter(lambda x: x['key'] > key, self.items))
			self.items = left + [{'key':key, 'child':None}] + right

	def __init__(self, M):
		if (M < 2):
			raise Exception("M must be greater than 1.")
		self.size = 0
		self.M = M
		self.root = None

	"""
	find which subtree to search for data in
	"""
	def get_child_idx(self, data, items):

		for i in range(len(items) - 1, -1, -1):
			if (data >= items[i]['key']):
				return i

	def insert(self, data):

		def helper(root):
			nonlocal data
			if (not root):
				root = self.Node()

			if (len(root.items) == self.M):
				idx = self.get_child_idx(data, root.items)
				root.items[idx]['child'] = helper(root.items[idx]['child'])
			else:
				root.add_key(data)

			return root

		if (self.contains(data)):
			raise Exception("Cannot insert {} because it already exists".format(data))
		self.root = helper(self.root)
		self.size += 1

	def find_min(self, root):
		if (not root.items[0]['child']):
			return root.items[1]['key']
		return self.find_min(root.items[0]['child'])

	def find_max(self, root):
		if (not root.items[-1]['child']):
			return root.items[-1]['key']
		return self.find_max(root.items[-1]['child'])

	def remove(self, data):
		
		def helper(root, data):
			child_idx = self.get_child_idx(data, root.items) # index of the subtree to traverse next
			if (root.items[child_idx]['key'] == data):
				child = root.items[child_idx]['child']
				if (child):
					root.items[child_idx]['key'] = self.find_min(child)
					root.items[child_idx]['child'] = helper(child, root.items[child_idx]['key'])

				else:
					root.items.pop(child_idx)
					if (len(root.items) == 1):
						root = root.items[0]['child']
			else:
				root.items[child_idx]['child'] = helper(root.items[child_idx]['child'], data)

			return root

		if (not self.contains(data)):
			raise Exception("Cannot remove {} because it does not exist".format(data))
		self.root = helper(self.root, data)
		self.size -= 1


	def contains(self, data):
		
		def helper(root):
			nonlocal data
			if (root is None):
				return False
			elif (data in [x['key'] for x in root.items]):
				return True
			else:
				# return helper(root.get_child(data))
				idx = self.get_child_idx(data, root.items)
				return helper(root.items[idx]['child'])
				# return helper(root[self.get_child_idx(data, root.items)]['child'])

		return helper(self.root)

	def __len__(self):
		return self.size

	def is_valid(self):
		"""
		do an inorder search and return false if current value is less than prev
		"""
		prev = None

		def inorder(root):
			nonlocal prev
			if (not root):
				return True
			if (not inorder(root.items[0]['child'])):
				return False

			for item in root.items[1:]:
				if (prev is not None and item['key'] < prev):
					return False
				prev = item['key']

				if (not inorder(item['child'])):
					return False
			return True

		return inorder(self.root)


	"""
	inorder traversal
	"""
	def __repr__(self):
		res = "["

		def helper(root):
			nonlocal res
			if (not root):
				return

			helper(root.items[0]['child'])
			for item in root.items[1:]:
				res += str(item['key']) + ", "
				helper(item['child'])


		helper(self.root)
		if (len(res) > 1):
			res = res[:-2]
		return res + "]"




def main():
	t = MArySearchTree(M=2)

if __name__ == "__main__":
	t = MArySearchTree(M=2)

	y = 100

	nums = list(range(0, y))
	while (nums):
		num = nums.pop(random.randint(0, len(nums) - 1))
		t.insert(num)
		print("inserted {}".format(num))

	print(t.is_valid())

	for i in range(0, y):
		if (not t.contains(i)):
			print("fuck")


	nums = list(range(0, y))
	while (nums):
		num = nums.pop(random.randint(0, len(nums) - 1))
		t.remove(num)

	for i in range(0, y):
		if (t.contains(i)):
			print("fuck")




