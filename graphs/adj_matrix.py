from quadratic_probing_hash import QuadraticProbingHash


"""
When to use: when you anticipate the graph having many edges
Space = O(V^2)
get_egde, set_edge, remove_edge = O(1)
remove_vertex, add_vertex = O(V^2)

"""

class Adjacency_Matrix:
	def __init__(self):
		self.vertices = []
		self.adjacency_matrix = []

		# hash from each vertex to its index in the adjacency matrix
		self.hash = QuadraticProbingHash()

	def add_vertex(self, v):
		self.hash[v] = len(self.vertices)
		self.vertices.append(v)
		for i in range(len(self.adjacency_matrix)):
			self.adjacency_matrix[i].append(False)
		self.adjacency_matrix.append([False] * len(self.vertices))

	def set_edge(self, v1, v2, edge_cost):
		if (not self.hash.contains(v1) or not self.hash.contains(v2)):
			raise Exception("v1 and v2 must exist")

		self.adjacency_matrix[self.hash[v1]][self.hash[v2]] = edge_cost

	def remove_edge(self, v1, v2):
		if (not self.hash.contains(v1) or not self.hash.contains(v2)):
			raise Exception("v1 and v2 must exist")

		if (not self.adjacency_matrix[self.hash[v1]][self.hash[v2]]):
			raise Exception("Cannot remove edge between {} and {} because there isn't one".format(v1, v2))
		self.adjacency_matrix[self.hash[v1]][self.hash[v2]] = False

	def remove_vertex(self, v):
		if (not self.hash.contains(v)):
			raise Exception("Vertex {} does not exist".format(v))

		idx = self.hash.pop(v)
		self.vertices.pop(idx)
		self.adjacency_matrix.pop(idx)
		for row in self.adjacency_matrix:
			row.pop(idx)

		for i in range(idx, len(self.vertices)):
			self.hash[self.vertices[i]] -= 1

	def get_vertices(self):
		return self.vertices

	def get_neighbors(self, v):
		if (not self.hash.contains(v)):
			raise Exception("Cannot get neigbors of vertex {} because it does not exist".format(v))

		neighbors = []
		for i, val in enumerate(self.adjacency_matrix[self.hash[v]]):
			if (val):
				neighbors.append(self.vertices[i])
		return neighbors

	def get_edge(self, v1, v2):
		if (not self.hash.contains(v1) or not self.hash.contains(v2)):
			raise Exception("v1 and v2 must exist")

		edge = self.adjacency_matrix[self.hash[v1]][self.hash[v2]]
		if (edge):
			return edge
		raise Exception("no edge between v1 and v2")

	"""
	return a list of all the graph's edges in the form [(from, to, weight), ...]
	"""
	def get_edges(self):
		res = []
		for v1 in self.vertices:
			for v2 in self.vertices:
				edge = self.adjacency_matrix[self.hash[v1]][self.hash[v2]]
				if (edge is not False):
					res.append((v1, v2, edge))
		return res

	def __repr__(self):
		res = ""
		offset = ""
		for v in self.vertices:
			if (len(v) > len(offset)):
				offset = " " * len(v)
			res += v + "  "
		res = offset + res
		res += "\n"

		for i in range(len(self.adjacency_matrix)):
			res += self.vertices[i] + offset[len(self.vertices[i]):]
			for j in range(len(self.adjacency_matrix[i])):
				x = [" "] * len(self.vertices[j])
				x[len(x) // 2] = str(self.adjacency_matrix[i][j]) if self.adjacency_matrix[i][j] else "0"
				res += ''.join(x) + "  "
			res += "\n"
		return res



if __name__ == "__main__":
	g = Adjacency_Matrix()
	print(g)


