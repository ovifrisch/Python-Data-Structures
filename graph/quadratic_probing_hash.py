from probing_hash import ProbingHash

class QuadraticProbingHash(ProbingHash):
	def __init__(self):
		ProbingHash.__init__(self, probing_function=(lambda x: pow(x, 2)))


if __name__ == "__main__":
	h = QuadraticProbingHash()
	h[0] = 1
	print(h.contains(0))