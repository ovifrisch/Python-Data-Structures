

class Node:
   def __init__(self, val, next=None, prev=None):
      self.val = val
      self.next = next
      self.prev = prev

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
         x = x.next
      self.tail = x
      self.size = len(nodes)

   def insert_front(self, node):
      temp = self.head
      self.head = node
      self.head.next = temp
      if (not self.head.next):
         self.tail = self.head
      self.size += 1

   def insert_back(self, node):
      if (not self.head):
         self.head = self.tail = node
      else:
         node.prev = self.tail
         self.tail.next = node
         self.tail = self.tail.next
      self.size += 1

   def pop_front(self):
      if (not self.head):
         raise Exception("deleting from empty list!")
      else:
         x = self.head.val
         self.head = self.head.next
         if (not self.head):
            self.tail = None
         self.size -= 1
         return x

   def pop_back(self):
      if (not self.head):
         raise Exception("deleting from empty list!")
      else:
         x = self.tail.val
         self.tail = self.tail.prev
         self.tail.next = None
         if (not self.tail):
            self.head = None
         self.size -= 1
         return x

   def contains(self, data):
      curr = self.head
      while (curr):
         if (curr.val == data):
            return True
         curr = curr.next
      return False

   def __len__(self):
      return self.size

   def __repr__(self):
      res = "["
      curr = self.head
      while (curr):
         res += str(curr.val) + ","
         curr = curr.next
      
      if (res[-1] == ","):
         res = res[:-1]
      res += "]"
      return res
         


if __name__ == "__main__":
   nodes = []
   for i in range(10):
      nodes.append(Node(i))
   ll = DLL(nodes)
   print(ll)