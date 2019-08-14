from probing_hash import ProbingHash

class LinearProbingHash(ProbingHash):
	def __init__(self):
		ProbingHash.__init__(self, probing_function=(lambda x: x))



if __name__ == "__main__":
	h = LinearProbingHash()
	h[0] = 1
	print(h.contains(1))