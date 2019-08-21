
class foo:
	def __init__(self):
		self.items = [{'a':None}]


root = foo()

def bar(root):
	if (not root):
		return foo()

	root.items[0]['a'] = bar(root.items[0]['a'])

bar(root)
print(root.items[0]['a'].items)