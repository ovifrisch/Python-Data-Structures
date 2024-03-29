from dll import DLL
from quadratic_probing_hash import QuadraticProbingHash

"""
When to use: when you anticipate the graph having few edges
Space = O(V + E)
get_edge, remove_edge = O(E)
add_vertex, add_edge = O(1)
So if graph is completely dense, the space requirement is O(V^2) becase there are V^2 edges
"""

class Adjacency_List:
	def __init__(self):
		self.adj_list = []

		# map vertices to index in list
		self.hash = QuadraticProbingHash()

	def add_vertex(self, v):
		self.hash[v] = len(self.adj_list)
		self.adj_list.append({'vertex': v, 'neighbors': DLL()})

	def set_edge(self, v1, v2, edge_cost=None):
		if (not self.hash.contains(v1) or not self.hash.contains(v2)):
			raise Exception("v1 and v2 must exist")

		self.adj_list[self.hash[v1]]['neighbors'].insert_front({'vertex':v2, 'cost':edge_cost})

	def remove_edge(self, v1, v2):
		if (not self.hash.contains(v1) or not self.hash.contains(v2)):
			raise Exception("v1 and v2 must exist")
		if (not self.adj_list[self.hash[v1]]['neighbors'].contains(p=lambda x: x['vertex'] == v2)):
			raise Exception("Cannot remove edge between {} and {} because there isn't one".format(v1, v2))
		self.adj_list[self.hash[v1]]['neighbors'].remove_if(p=lambda x: x['vertex'] == v2)

	def remove_vertex(self, v):
		if (not self.hash.contains(v)):
			raise Exception("Vertex {} does not exist".format(v))

		idx = self.hash.pop(v)
		self.adj_list.pop(idx)
		for i in range(idx, len(self.adj_list)):
			self.hash[self.adj_list[i]['vertex']] -= 1

		# remove from all adjacency lists
		for i in range(len(self.adj_list)):
			if (self.adj_list[i]['neighbors'].contains(p=lambda x: x['vertex'] == v)):
				self.adj_list[i]['neighbors'].remove_if(p=lambda x: x['vertex'] == v)


	def get_vertices(self):
		return [x['vertex'] for x in self.adj_list]

	def get_neighbors(self, v):
		if (not self.hash.contains(v)):
			raise Exception("Cannot get neigbors of vertex {} because it does not exist".format(v))
		return [x['vertex'] for x in self.adj_list[self.hash[v]]['neighbors'].to_list()]

	def get_edge(self, v1, v2):
		if (not self.hash.contains(v1) or not self.hash.contains(v2)):
			raise Exception("v1 and v2 must exist")

		if (not self.adj_list[self.hash[v1]]['neighbors'].contains(p=lambda x: x['vertex'] == v2)):
			raise Exception("no edge between v1 and v2")

		for item in self.adj_list[self.hash[v1]]['neighbors']:
			if (item['vertex'] == v2):
				return item['cost']

	"""
	return a list of all the graph's edges in the form [(from, to, weight), ...]
	"""
	def get_edges(self):
		res = []
		for item in self.adj_list:
			for nbr in item['neighbors']:
				res.append((item['vertex'], nbr['vertex'], nbr['cost']))
		return res

	def __repr__(self):
		res = ""
		for i in range(len(self.adj_list)):
			res += str(self.adj_list[i]['vertex'])
			res += ": "
			for item in self.adj_list[i]['neighbors']:
				res += str(item['vertex']) + ", "
			res += "\n"
		return res[:-1]






if __name__ == "__main__":
	g = Adjacency_List()
	vertices = ['a', 'b', 'c', 'd', 'e']
	for v in vertices:
		g.add_vertex(v)

	g.set_edge('a', 'b', 3)
	g.set_edge('a', 'd', 5)
	g.remove_vertex('b')
	g.remove_edge('a', 'd')


	print(g)




