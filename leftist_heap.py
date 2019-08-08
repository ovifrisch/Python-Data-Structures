


class LeftistHeap:
	def __init__(self):
		self.root = None

	def null_path_length(self, node):
		# null_path_length(X), of any node X to be the length of the shortest path from X to a node without two children.
		q = [{"node":node, "npl":0}]

		while (q):
			fq = q.pop(0)
			if (not fq['node'].left or not fq['node'].right):
				return fq['npl']
			q.append({'node':fq.right, 'npl':fq['npl'] + 1})
			q.append({'node':fq.left, 'npl':fq['npl'] + 1})

