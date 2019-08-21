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

	def add_vertex(self, v):
		self.graph.add_vertex(v)

	def set_edge(self, v1, v2, edge_cost):
		self.graph.set_edge(v1, v2, edge_cost)

	def remove_edge(self, v1, v2):
		self.graph.remove_edge(v1, v2)

	def remove_vertex(self, v):
		self.graph.remove_vertex(v)

	def get_vertices(self):
		return self.graph.get_vertices()

	def get_neighbors(self, v):
		return self.graph.get_neighbors(v)

	def get_edge(self, v1, v2):
		return self.graph.get_edge(v1, v2)

	def contains_vertex(self, v):
		vertices = self.graph.get_vertices()
		return vertex in vertices

	def contains_cycle(self):
		pass

	def shortest_path(self, v1, v2, algo="dijkstra"):
		

		def dikjstra(v1, v2):
			pass

		def bellman_ford(v1, v2):
			pass

		def floyd_warshall(v1, v2):
			pass

	def dfs(self, v):
		pass

	def bfs(self, v):
		pass

	def topological_sort(self):
		if (self.contains_cycle()):
			raise Exception("Cannot perform topological_sort on a cyclic graph")
		pass

	def minimum_spanning_tree(self, algo="prim"):
		
		def prim():
			pass

		def kruskal():
			pass

	def connected(self, v1, v2):
		# is v1 connected to v2 by a series of edges?
		pass

	def eulerian_path(self):
		# return an eulerian path if it exists, otherwise None
		# visit each edge exactly once
		pass

	def hamiltonian_path(self):
		# visit each vertex exactly once
		pass

	def all_paths(self, v1, v2):
		# get all unique paths from v1 to v2
		pass

	def maximum_flow(self):
		pass

	def connected_components(self):
		pass

	def strongly_connected_components(self):
		pass

	def get_bridges(self):
		# a bridge is an edge in a graph such that if it is removed, the
		# number of connected components decreases by one
		pass

	def articulation_points(self):
		pass

	def get_degree(self, v):
		pass

	def get_min_degree(self):
		pass

	def get_max_degree(self):
		pass

	def critical_path_analysis(self):
		pass

	def all_pairs_shortest_path(self):
		pass

	def traveling_salesman(self, start, vertices):
		pass 

	def __repr__(self):
		return self.graph.__repr__()

if __name__ == "__main__":
	l = Graph("list")
	m = Graph("matrix")

	vertices = ['a', 'b', 'c', 'd', 'e']
	for v in vertices:
		l.add_vertex(v)
		m.add_vertex(v)

	l.set_edge('a', 'e', 3)
	m.set_edge('a', 'e', 3)
	print(l)
	print(m)




