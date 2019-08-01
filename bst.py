
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
        
        def helper(node):

            if (val < node.val):
                if (node.left):
                    helper(node.left)
                else:
                    node.left = self.Node(val)
                    self.size += 1
            elif (val > node.val):
                if (node.right):
                    helper(node.right)
                else:
                    node.right = self.Node(val)
                    self.size += 1
            else:
                raise Exception("Value already exists")

        if (not self.root):
            self.root = self.Node(val)
        else:
            helper(self.root)

    def remove(self, val):


        def helper(node):
            # node.val is guaranteed not be equal to val

            # val not found
            if (not node.left and not node.right):
                return

            if (node.left and val == node.left.val):
                if (not node.left.left):
                    node.left = node.left.right
                elif (not node.left.right):
                    node.left = node.left.left
                else:
                    curr = node.left
                    while (curr.right.right):
                        curr = curr.right
                    node.left.val = curr.right.val
                    curr.right = None
                self.size -= 1

            elif (node.right and val == node.right.val):
                if (not node.right.left):
                    node.right = node.right.right
                elif (not node.right.right):
                    node.right = node.right.left
                else:
                    curr = node.left
                    while (curr.right.right):
                        curr = curr.right
                    node.right.val = curr.right.val
                    curr.right = None
                self.size += 1

            # val 
            if (node.left and val < node.left.val):
                return helper(node.left)
            elif (node.right and val > node.right.val):
                return helper(node.right)
            elif (node.left and val > node.left.val):
                return helper(node.left)
            elif (node.right and val < node.right.val):
                return helper(node.right)



        if (not self.root or self.root.val == val):
            dummy = self.Node(-1, self.root, None)
            helper(dummy)
            self.root = dummy.left
        else:
            helper(self.root)




if __name__ == "__main__":
    t = BST([5, 3, 7, 2, None, None, 10])
    

