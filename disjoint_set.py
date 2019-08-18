import copy


class DisjointSet:

	class Node:
		def __init__(self, data, parent, size, rank):
			self.data = data
			self.parent = parent
			self.size = size
			self.rank = rank

	def __init__(self):
		self.array = []
		self.hash = {}
		self.num_sets = 0

	def num_sets(self):
		return self.num_sets

	def add(self, data):
		for node in self.array:
			if (node.data == data):
				raise Exception("This element already exists")

		# hash the index of the data
		self.hash[data] = len(self.array)
		self.array.append(self.Node(data, -1, 1, 0))
		self.num_sets += 1


	def union(self, data1, data2, by=None):
		if (data1 not in self.hash or data2 not in self.hash):
			raise Exception("Both of these elements must exist")

		p1 = self.find(data1)
		p2 = self.find(data2)
		if (p1 == p2):
			raise Exception("These elements cannot be unioned because they belong to the same set")
		s1 = self.array[p1].size
		s2 = self.array[p2].size
		r1 = self.array[p2].rank
		r2 = self.array[p2].rank
		new_rank = r1 + 1 if r1==r2 else max(r1, r2)
		new_size = s1 + s2

		def helper(new_parent, child, new_size, new_rank):
			self.array[child].parent = new_parent
			self.array[new_parent].size = new_size
			self.array[new_parent].rank = new_rank

		if (not by):
			self.array[p2].parent = p1
			self.array[p1].size = new_size
			self.array[p1].rank = new_rank

		elif (by == "rank"):
			if (r1 <= r2):
				helper(p2, p1, new_size, new_rank)
			else:
				helper(p1, p2, new_size, new_rank)
		elif (by == "size"):
			if (s1 <= s2):
				helper(p2, p1, new_size, new_rank)
			else:
				helper(p1, p2, new_size, new_rank)
		else:
			raise Exception("Invalid by argument: {}".format(by))

		self.num_sets -= 1


	"""
	returns the index of the root in the array
	"""
	def find(self, data):
		if (data not in self.hash):
			raise Exception("This element does not exist")

		idx = self.hash[data]
		while (self.array[idx].parent != -1):
			idx = self.array[idx].parent
		return idx


	def compress(self, arr=None):
		if (arr is None):
			arr = self.array

		def helper(x):
			nonlocal arr
			if (arr[x.parent].parent == -1):
				return x.parent
			return helper(arr[x.parent])

		for x in arr:
			if (x.parent == -1):
				continue
			x.parent = helper(x)

		return arr

	"""
	print all the elements of the set that are in the
	same group together
	"""
	def __repr__(self):
		cpsd = self.compress(copy.deepcopy(self.array))
		parents = {}
		for i in range(len(cpsd)):
			if (cpsd[i].parent == -1):
				parents[i] = [cpsd[i].data]

		for i in range(len(cpsd)):
			if (cpsd[i].parent != -1):
				parents[cpsd[i].parent].append(cpsd[i].data)

		res = ""
		for _, val in parents.items():
			res += str(val)
			res += "\n"
		return res




if __name__ == "__main__":
	d = DisjointSet()
	l = "Los Altos"
	mo = "Mountain View"
	p = "Palo Alto"
	i = "Irvine"
	s = "San Diego"
	la = "Los Angeles"
	n = "New York"
	b = "Brooklyn"
	m = "Manhattan"

	cities = [l,mo,p,i,s,la,n,b,m]
	for x in cities:
		d.add(x)

	d.union(l, mo, by="rank")
	d.union(p, l, by="rank")
	d.union(b, m, by="rank")
	d.union(b, l, by="rank")
	print(d)
	

