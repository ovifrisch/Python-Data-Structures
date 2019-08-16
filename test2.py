


class Foo:
	def __init__(self, x):
		self.x = x


x = {'key':2, 'child':Foo(2)}
y = {'key':1, 'child': Foo(3)}
print(x < y)
