from dll import DLL
from quadratic_probing_hash import QuadraticProbingHash

class Adjacency_List:
	def __init__(self):
		self.adj_list = []

		# map vertices to index in list
		self.hash = QuadraticProbingHash()

	def add_edge(self, v1, v2):
		if (not self.hash.contains(v1) or not self.hash.contains(v2)):
			raise Exception("v1 and v2 must exist")

		self.adj_list[self.hash[v1]]['neighbors'].insert_front(v2)

	def add_vertex(self, v):
		self.hash[v] = len(self.adj_list)
		self.adj_list.append({'vertex': v, 'neighbors': DLL()})

	def remove_edge(self, v1, v2):
		if (not self.hash.contains(v1) or not self.hash.contains(v2)):
			raise Exception("v1 and v2 must exist")

		if (not self.adj_list[self.hash[v1]]['neighbors'].contains(v2)):
			raise Exception("Cannot remove edge between {} and {} because there isn't one".format(v1, v2))
		self.adj_list[self.hash[v1]]['neighbors'].remove(v2)

	def remove_vertex(self, v):
		if (not self.hash.contains(v)):
			raise Exception("Vertex {} does not exist".format(v))

		idx = self.hash.pop(v)
		self.adj_list.pop(idx)
		for i in range(idx, len(self.adj_list)):
			self.hash[self.adj_list[i]['vertex']] -= 1

		# remove from all adjacency lists
		for i in range(len(self.adj_list)):
			if (self.adj_list[i]['neighbors'].contains(v)):
				self.adj_list[i]['neighbors'].remove(v)


	def get_vertices(self):
		return [x['vertex'] for x in self.adj_list]

	def get_neighbors(self, v):
		if (not self.hash.contains(v)):
			raise Exception("Cannot get neigbors of vertex {} because it does not exist".format(v))
		return self.adj_list[self.hash[v]]['neighbors'].to_list()

	def __repr__(self):
		res = ""
		for i in range(len(self.adj_list)):
			res += self.adj_list[i]['vertex']
			res += ": "
			for neighbor in self.adj_list[i]['neighbors']:
				res += neighbor + ", "
			res += "\n"
		return res[:-1]






if __name__ == "__main__":
	g = Adjacency_List()
	print(g)




