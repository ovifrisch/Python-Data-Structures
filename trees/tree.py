class Tree:
    def __init__(self, num_children, data=[]):
        self.num_c = num_children
        if (data):
            self.arr = [None] * max(num_children, len(data))
            self.arr = data + ([None] * max(num_children, len(data)))
            self.size = len(data)
        else:
            self.arr = [None] * (1 + num_children)
            self.size = 0

    def resize(self):
        self.arr = self.arr + [None] * len(self.arr)



    def preorder(self):

        def helper(idx):
            if (idx >= self.size):
                return

            res.append(self.arr[idx])
            # first child's idx
            c1 = self.num_c * idx + 1
            for c in range(c1, c1 + self.num_c):
                helper(c)

        res = []
        helper(0)
        return res

    def postorder(self):
        pass

    def inorder(self):
        # left, node, right
        pass


    def insert(self, val):
        if (self.size == len(self.arr)):
            self.resize()

        self.arr[self.size] = val
        self.size += 1

    def contains(self, val):
        return val in self.arr

    def remove(self, val):
        for i in range(self.size):
            if (self.arr[i] == val):
                self.arr[i] = self.arr[self.size - 1]
                self.arr[self.size - 1] = None
                self.size -= 1
                return
        raise Exception("Element not found")

    def __len__(self):
        return self.size

    def __repr__(self):
        res = "["
        for i in range(self.size):
            res += str(self.arr[i])
            if (i < self.size - 1):
                res += ", "
        res += "]"
        return res

if __name__ == "__main__":
    t = Tree(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    for i in range(100):
        t.insert(i)
    print(t)
    t.remove(1)
    print(t)
    print(len(t.arr))




