


def foo():

	def bar():

		for i in range(10):
			yield i

	return bar()


for x in foo():
	print(x)