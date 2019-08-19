import random
class BST:

    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def __init__(self, data=[]):
        self.root = None
        self.size = 0
        self.init_tree(data)

    def find_min(self, node):
        while (node.left):
            node = node.left
        return node

    def is_valid(self):

        def inorder(root):
            if (not root):
                return True
            if (not inorder(root.left)):
                return False
            if (self.prev is not None and root.val < self.prev):
                return False

            self.prev = root.val
            return inorder(root.right)

        self.prev = None
        return inorder(self.root)

    def __repr__(self):
        if (not self.root):
            return "[]"

        q = [self.root]

        res = "["

        while (q):
            x = q.pop(0)
            if (not x):
                res += "None, "

            else:
                res += str(x.val) + ", "
                if (x.left or x.right):
                    q.append(x.left)
                    q.append(x.right)

        res = res[:-2] + "]"
        return res

    def __len__(self):
        return self.size


    def init_tree(self, data):
        for i in range(len(data)):
            if (data[i] is not None):
                self.insert(data[i])

    def contains(self, val):
        def helper(node):
            if (not node):
                return False
            elif (node.val == val):
                return True
            elif (val < node.val):
                return helper(node.left)
            else:
                return helper(node.right)

        return self.helper(self.root)


    def insert(self, val):

        def helper(root, val):
            if (not root):
                return self.Node(val)
            elif (val < root.val):
                root.left = helper(root.left, val)
            elif (val > root.val):
                root.right = helper(root.right, val)
            else:
                raise Exception("Value already exists")

            return root

        self.root = helper(self.root, val)
        self.size += 1

    def remove(self, val):


        def helper(node, target):
            # the target was not found
            if (not node):
                raise Exception("Value not found")

            # the target has been found
            if (node.val == target):
                if (not node.left and not node.right):
                    return None
                elif (node.left):
                    return node.left
                elif (node.right):
                    return node.right
                else:
                    # find the inorder successor of the current node
                    node.val = self.find_min(node.right)
                    node.right = helper(node.right, node.val)
                    return node

            elif (target < node.val):
                node.left = helper(node.left, target)
            else:
                node.right = helper(node.right, target)
            return node

        self.root = helper(self.root, val)
        self.size -= 1


if __name__ == "__main__":
    t = BST()
    nums = set()
    for i in range(5):
        nums.add(random.randint(1, 100))
    nums = list(nums)
    print(nums)

    for num in nums:
        t.insert(num)
        print(t.is_valid())

    for num in nums[::-1]:
        t.remove(num)
        print(t)
        print(t.is_valid())
    print(t)
    

