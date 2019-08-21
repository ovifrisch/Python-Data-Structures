from graph import Graph

# all elements in array are the same
def equal(array):
	for i in range(1, len(array)):
		if (array[i] != array[i-1]):
			return False
	return True

def test(graphs):
	results = []
	vertices = ['a', 'b', 'c', 'd', 'e']
	for g in graphs:
		for v in vertices:
			g.add_vertex(v)
		g.set_edge('a', 'd', 3)
		g.set_edge('a', 'a', 6)
		g.set_edge('a', 'e', -300)
		g.set_edge('c', 'd', 39)
		g.remove_edge('a', 'd')
		g.remove_vertex('c')

		results.append(g.get_edge('a', 'a'))
	assert equal(results)



l = Graph("list")
m = Graph("matrix")

test([l, m])