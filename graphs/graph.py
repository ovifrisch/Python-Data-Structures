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

	def get_edges(self):
		return self.graph.get_edges()

	def contains_vertex(self, v):
		vertices = self.graph.get_vertices()
		return v in vertices

	def contains_edge(self, v1, v2):
		return v2 in v1.get_neighbors()

	def __len__(self):
		return len(self.get_vertices())


	def contains_cycle(self):
		seen = {} # all nodes that we have visited
		for v in self.get_vertices():
			visited = {} # visited nodes on the current call stack
			if (v in seen):
				continue

			def visit(node):
				nonlocal visited
				if (node in visited):
					return True
				if (node in seen):
					return False

				seen[node] = True
				visited[node] = True
				for nbr in self.get_neighbors(node):
					if(visit(nbr)):
						return True
				visited.pop(node)
				return False

			if(visit(v)):
				return True
		return False


	def shortest_path(self, v1, v2, algo="dijkstra"):
		

		def dikjstra(v1, v2):
			pass

		def bellman_ford(v1, v2):
			pass

		def floyd_warshall(v1, v2):
			pass

	def dfs(self, v):
		if (not self.contains_vertex(v)):
			raise Exception("Cannot perform DFS on vertex that does not exist")

		if (self.connected_components() != 1):
			raise Exception("Cannot perform dfs on a graoh that isn't fully connected")

		visited = {v:'True'}
		res = []

		def visit(node):
			nonlocal visited, res
			for nbr in filter(lambda x: x not in visited, self.get_neighbors(node)):
				visited[nbr] = True
				visit(nbr)
			res.append(node)
		visit(v)
		return res




	def bfs(self, v):

		if (not self.contains_vertex(v)):
			raise Exception("Cannot perform BFS on vertex that does not exist")

		if (self.connected_components() != 1):
			raise Exception("Cannot perform bfs on a graoh that isn't fully connected")

		visited = {v:'True'}

		q = [v]
		res = []
		while (q):
			v = q.pop(0)
			res.append(v)
			for nbr in filter(lambda x: x not in visited, self.get_neighbors(v)):
				q.append(nbr)
				visited[nbr] = True
		return res

	"""
	return a vertex that has no indident edges
	only consider edges that return true on predicate q
	and also returns true on the predict p, if provided as argument
	if none, return None
	"""
	def no_incidents(self, p, q):
		incident_counts = {}
		for v in self.get_vertices():
			incident_counts[v] = 0
		for e in self.get_edges():
			if (q(e[:2])):
				continue
			incident_counts[e[1]] += 1

		for k, v in incident_counts.items():
			if (v == 0 and (not p or not p(k))):
				return k
		return None

	def topological_sort(self):
		if (self.contains_cycle()):
			raise Exception("Cannot perform topological_sort on a cyclic graph")

		num_vertices = len(self)
		removed_edges = {}
		removed_vertices = {}
		res = []

		while (len(removed_vertices) < num_vertices):
			# remove an edge with no incident edges
			p = lambda x: x in removed_vertices
			q = lambda x: x in removed_edges # edge 
			v = self.no_incidents(p, q)
			res.append(v)
			removed_vertices[v] = True
			for nbr in self.get_neighbors(v):
				removed_edges[(v, nbr)] = True
		return res

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
		return 1

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
	g = Graph("list")
	vs = list(range(1, 6))
	es = [(1, 2), (3, 2), (2, 4), (3, 5)]
	for v in vs:
		g.add_vertex(v)
	for e in es:
		g.set_edge(e[0], e[1], 1)

	print(g.topological_sort())

	# g = Graph("list")
	# m = Graph("matrix")

	# vertices = ['a', 'b', 'c', 'd', 'e']
	# for v in vertices:
	# 	g.add_vertex(v)

	# no_cycle_edges = [('a', 'b'), ('a', 'c'), ('b', 'd'), ('c', 'd'), ('d', 'e')]
	# cycle_edges = [('a', 'b'), ('b', 'c'), ('c', 'a'), ('a', 'd'), ('a', 'e')]
	# for e in no_cycle_edges:
	# 	g.set_edge(e[0], e[1], 1)

	# print(g.contains_cycle())




