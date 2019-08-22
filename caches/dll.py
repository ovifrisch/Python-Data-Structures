

class Node:
   def __init__(self, data, next=None, prev=None):
      self.data = data
      self.next = next
      self.prev = prev

   def __iadd__(self, num):
      curr = self
      while (num > 0):
         num -= 1
         curr = curr.next
      return curr

class DLL:
   def __init__(self, nodes=None):
      if (nodes):
         self.create_ll(nodes)
      else:
         self.head = None
         self.tail = None
         self.size = 0

   def create_ll(self, nodes):
      self.head = nodes[0]
      x = self.head
      for i in range(len(nodes) - 1):
         x.next = nodes[i+1]
         x.next.prev = x
         x += 1
      self.tail = x
      self.size = len(nodes)

   """
   remove the first node that satisfies the predicate p
   """
   def remove_if(self, p):
      curr = self.head
      while (curr):
         if (p(curr.data)):
            self.remove(curr.data)
            break
         curr += 1

   def remove_node(self, node):
      if (not node.next and not node.prev):
         self.head = self.tail = None
      elif (not node.next):
         node.prev.next = None
         self.tail = node.prev
      elif (not node.prev):
         self.head = node.next
         self.head.prev = None
      else:
         node.prev.next = node.next
         node.next.prev = node.prev

   def remove(self, data):
      if (not self.head):
         raise Exception("Value not found")
      elif (self.head.data == data):
         self.pop_front()
      elif (self.tail.data == data):
         self.pop_back()
      else:
         curr = self.head
         while (curr.next):
            if (curr.next.data == data):
               curr.next = curr.next.next
               curr.next.prev = curr
               return
            curr += 1
         raise Exception("Value not found")

   def insert_front(self, data):
      node = Node(data)
      temp = self.head
      self.head = node
      self.head.next = temp
      if (not self.head.next):
         self.tail = self.head
      else:
         self.head.next.prev = self.head
      self.size += 1
      return node

   def insert_back(self, data):
      node = Node(data)
      if (not self.head):
         self.head = self.tail = node
      else:
         node.prev = self.tail
         self.tail.next = node
         self.tail += 1
      self.size += 1

   def pop_front(self):
      if (not self.head):
         raise Exception("deleting from empty list!")
      else:
         x = self.head.data
         self.head += 1
         if (not self.head):
            self.tail = None
         else:
            self.head.prev = None
         self.size -= 1
         return x


   def reverse(self):
      pass

   def merge(self, other):
      pass

   def remove_loop(self):
      pass

   def sort(self):
      pass

   """

   """
   def rotate(self, k):
      pass

   def tree_to_list(root):
      pass

   def pop_back(self):
      if (not self.head):
         raise Exception("deleting from empty list!")

      x = self.tail.data
      if (not self.tail.prev):
         self.head = self.tail = None
      else:
         self.tail = self.tail.prev
         self.tail.next = None
      self.size -= 1
      return x

   def contains(self, data=None, p=None):
      if (not data and not p or (data and p)):
         raise Exception("invalid arguments")
      curr = self.head
      while (curr):
         if ((p and p(curr.data)) or curr.data == data):
            return True
         curr += 1
      return False

   def __len__(self):
      return self.size

   def __repr__(self):
      res = "["
      curr = self.head
      while (curr):
         res += str(curr.data) + ","
         curr += 1
      
      if (res[-1] == ","):
         res = res[:-1]
      res += "]"
      return res


   def __iter__(self):
      self.start_iter = self.head
      return self

   def __next__(self):
      if (not self.start_iter):
         raise StopIteration
      else:
         data = self.start_iter.data
         self.start_iter += 1
         return data
         


if __name__ == "__main__":
   nodes = []
   for i in range(10):
      nodes.append(Node(i))

   dll = DLL(nodes)
   print(dll)
   
   x = dll.tail
   dll.remove_node(x)
   print(dll)


