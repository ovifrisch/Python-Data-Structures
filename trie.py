

class Trie:

	class Node:
		def __init__(self, letter="", num_words=0):
			self.is_word = False
			self.children = []
			self.letter = letter
			self.num_words = num_words # the number of words that have this common prefix


	def __init__(self, words=[]):
		self.root = self.Node()
		self.size = 0
		for w in words:
			self.insert(w)

	def insert(self, word):
		node = self.root
		if (self.contains(word)):
			raise Exception("Trie already contains word.")
			return
		for c in word:
			node.num_words += 1
			if (c not in [x.letter for x in node.children]):
				node.children.append(self.Node(c))
			node = node.children[[x.letter for x in node.children].index(c)]
		node.is_word = True
		self.size += 1


	def delete(self, word):
		node = self.root
		if (not self.contains(word)):
			raise Exception("Trie does not contain word")
			return

		for c in word:
			idx = [x.letter for x in node.children].index(c)
			child = node.children[idx]
			if (child.num_words < 2):
				node.children.pop(idx)
				self.size -= 1
				return
			node.num_words -= 1
			node = node.children[idx]
		node.is_word = False
		self.size -= 1


	# returns the node that defines prefix, or None
	def __find_node(self, prefix):
		node = self.root
		for c in prefix:
			if (c not in [x.letter for x in node.children]):
				return None
			node = node.children[[x.letter for x in node.children].index(c)]
		return node

	def contains(self, word):
		x = self.__find_node(word)
		return x is not None and x.is_word

	def is_prefix(self, prefix):
		return self.__find_node(word)

	def __len__(self):
		return self.size

	def __repr__(self):

		 def helper(node, curr, res):
		 	if (node.is_word):
		 		res.append(curr)
		 	for n in node.children:
		 		helper(n, curr + n.letter, res)

		 words = []
		 helper(self.root, "", words)
		 res = "["
		 for w in words:
		 	res += w + ", "

		 if (len(res) > 1):
		 	res = res[:-2]

		 res += "]"
		 return res




if __name__ == "__main__":
	trie = Trie(["was", "wash", "waste", "words", "word", "wording"])
	print(trie)
	trie.delete("wash")
	print(trie)
	trie.insert("hello")
	print(trie)
	trie.delete("wording")
	print(trie)
	print(trie.contains("wording"))
	print(trie.contains("was"))




