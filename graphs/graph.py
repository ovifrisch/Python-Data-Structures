from adj_list import Adjacency_List
from adj_matrix import Adjacency_Matrix
from d_heap import DHeap
import itertools

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

	def predecessor_subgraph(self, v):
		"""
		return the predecessor subgraph formed by doing a bfs
		of the graph starting at vertex v
		"""
		visited = {v:True}

		subgraph = Graph()
		subgraph.add_vertex(v)
		q = [v]

		while (q):
			node = q.pop(0)
			for nbr in filter(lambda x: x not in visited, self.get_neighbors(node)):
				subgraph.add_vertex(nbr)
				subgraph.set_edge(node, nbr, self.get_edge(node, nbr))
				visited[nbr] = True
				q.append(nbr)
		return subgraph


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

	def __floyd_warshall(self):
		pass

	def __relax(self, u, v, w):
		if (u + w < v):
			return u + w
		return v

	def __bellman_ford(self, v):
		"""
		relax all the edges in the graph
		len(graph) times. this ensures that d[v]
		is the shortest path from s to v because
		of the path relaxation property.
		"""

		vertex_dists = {}
		for vtx in self.get_vertices():
			vertex_dists[vtx] = float('inf')
		vertex_dists[v] = 0

		for _ in range(len(self) - 1):
			for e in self.get_edges():
				vertex_dists[e[1]] = self.__relax(vertex_dists[e[0]], vertex_dists[e[1]], e[2])

		for e in self.get_edges():
			if (vertex_dists[e[0]] + e[2] < vertex_dists[e[1]]):
				raise Exception("graph contains a negative weight cycle")
		return vertex_dists



	def __dijkstra(self, v1, v2):
		class Vertex:
			def __init__(self, data, parent=None, dist=float('inf')):
				self.data = data
				self.parent = parent
				self.dist = dist

		pq = DHeap(has_priority=lambda x, y: x.dist < y.dist)
		pq.insert(Vertex(v1, dist=0))
		explored = {}
		while (len(pq) > 0):
			curr = pq.remove_min()
			if (curr.data == v2):
				break
			if (curr.data in explored):
				continue
			explored[curr.data] = True
			for nbr in self.get_neighbors(curr.data):
				if (not nbr in explored):
					pq.insert(Vertex(nbr, curr, curr.dist + self.get_edge(curr.data, nbr)))
		return curr.dist


	def topological_shortest_path(self, v):
		"""
		relax edges in topological order
		"""
		shortest_paths = {}
		for vtx in self.get_vertices():
			shortest_paths[vtx] = float('inf')
		shortest_paths[v] = 0
		vs = self.topological_sort()
		for v in vs:
			for nbr in self.get_neighbors(v):
				shortest_paths[nbr] = self.__relax(shortest_paths[v], shortest_paths[nbr], self.get_edge(v, nbr))
		return shortest_paths



	def shortest_path(self, v1, v2):
		"""
		find the shortest path between v1 and v2
		"""
		if (not self.contains_vertex(v1)):
			raise Exception("v1 must exist")

		if (not self.connected(v1, v2)):
			raise Exception("there is no path between v1 and v2")

		# if the graph is a DAG, use the topological ordering to get an O(V + E) algorithm
		if (not self.contains_cycle()):
			return self.topological_shortest_path(v1)[v2]

		# if the graph contains negative edge weights, do bellman ford
		if (list(filter(lambda x: x[2] < 0, self.get_edges())) != []):
			shortest_paths = self.single_source_shortest_paths(v1)
			return shortest_paths[v2]
		else:
			# otherwise dijkstra
			return self.__dijkstra(v1, v2)

	def single_source_shortest_paths(self, v):
		"""
		find the shortest paths from v to eavh vertex in the graph
		"""
		if (not self.contains_vertex(v)):
			raise Exception("v must exist")
		return self.__bellman_ford(v)

	def shortest_paths(self):
		"""
		find the shortest paths between all pairs of vertices
		"""
		return self.__floyd_warshall()


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


	"""
	can be improved by pre-computing indegrees of each vertex
	and placing them in a queue. For every vertex popped off
	the queue, we lower the indegrees of each of its neighbors.
	If the neighbor's indegree is 0 as a result of this update,
	it is appended to the queue. (a stack could also be used)
	"""
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
		if (not self.contains_vertex(v1)):
			raise Exception("v1 must exist")
		visited = {v1:True}

		def visit(node):
			nonlocal visited, v2
			if (node == v2):
				return True
			for nbr in filter(lambda x: x not in visited, self.get_neighbors(node)):
				visited[nbr] = True
				if (visit(nbr)):
					return True
			return False

		return visit(v1)

	def verify_eulerian_path(self, path):
		"""
		verify that the given path is an eulerian path
		the path is a series of edges
		"""
		if (len(path) != len(self.get_edges()) + 1):
			return False

		if (path[0] != path[-1]):
			return False

		edges = [x[:2] for x in self.get_edges()]
		seen = {}
		for i in range(0, len(path) - 1):
			this_edge = (path[i], path[i+1])
			if (this_edge not in edges):
				return False
			if (this_edge in seen):
				return False
			seen[this_edge] = True
		return True

	def is_bipartite(self):
		pass

	def eulerian_path(self):
		for path in list(itertools.permutations(self.get_vertices())):
			path = list(path) + [path[0]]
			if (self.verify_eulerian_path(path)):
				return path
		return None

	def verify_hamiltonian_path(self, path):
		if (set(path) != set(self.get_vertices())):
			return False

		edges = [x[:2] for x in self.get_edges()]
		for i in range(0, len(path) - 1):
			if ((path[i], path[i+1]) not in edges):
				return False
		return True

	def hamiltonian_path(self):
		for path in list(itertools.permutations(self.get_vertices())):
			if (self.verify_hamiltonian_path(path)):
				return path
		return None

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
		if (not self.contains_vertex(v)):
			raise Exception("v does not exist")

		count = 0
		for vtx in self.get_vertices():
			for nbr in self.get_neighbors(vtx):
				if (nbr == v):
					count += 1
		return count

	def get_min_degree(self):
		degrees = self.get_all_degrees()
		return min([degrees[k] for k in degrees.keys()])


	def get_all_degrees(self):
		degrees = {}
		for v in self.get_vertices():
			degrees[v] = 0

		for v in self.get_vertices():
			for nbr in self.get_neighbors(v):
				degrees[nbr] += 1
		return degrees


	def get_max_degree(self):
		degrees = self.get_all_degrees()
		return max([degrees[k] for k in degrees.keys()])

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
	vs = ['A', 'B', 'C', 'D']
	es = [('A', 'B', 5), ('C', 'D', 3), ('B', 'C', -5), ('D', 'A', 1)]
	for v in vs:
		g.add_vertex(v)
	for e in es:
		g.set_edge(e[0], e[1], e[2])

	# print(g.shortest_path('A', 'C'))
	print(g.get_min_degree())
	print(g.get_max_degree())
	print(g.eulerian_path())

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




