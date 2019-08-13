
# return a (multiline) string that shows the tree like this for example:

class Node:
	def __init__(self, val, nxt=None):
		self.val = val
		self.next = nxt

def print_list(node):
	res = "["
	while (node):
		res += str(node.val) + ", "
		node = node.next
	print(res + "]")



n1 = Node(1, Node(2, None))
print_list(n1)

x = n1.next
x.val = 3
print_list(n1)




def from_list(tree):
	pass


def from_tree(tree):
	pass