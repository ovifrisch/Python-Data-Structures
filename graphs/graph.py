from adj_list import Adjacency_List
from adj_matrix import Adjacency_Matrix

class Graph:
	def __init__(self, impl="list"):
		if (impl == "list"):
			self.graph = Adjacency_List()
		elif (impl == "matrix"):
			self.graph = Adjacency_Matrix()
		else:
			raise Exception("Invalid implementation")

	def add_vertex(self, vertex):
		self.graph.add_vertex(vertex)

	def add_edge(self, vertex1, vertex2):
		self.graph.add_edge(vertex1, vertex2)

	def remove_edge(self, vertex1, vertex2):
		self.graph.remove_edge(vertex1, vertex2)

	def remove_vertex(self, vertex):
		self.graph.remove_vertex(vertex)

	def get_vertices(self):
		return self.graph.get_vertices()

	def get_neighbors(self, vertex):
		return self.graph.get_neighbors(vertex)

	def contains_vertex(vertex):
		vertices = self.graph.get_vertices()
		return vertex in vertices

	def contains_cycle(self):
		pass

	def __repr__(self):
		return self.graph.__repr__()

if __name__ == "__main__":
	g = Graph("list")
	g.add_vertex("1")
	print(g)





