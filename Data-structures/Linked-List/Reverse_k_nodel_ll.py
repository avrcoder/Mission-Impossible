class LinkedList(object):
	def __init__(self):
		self.head = None
		self.second = None

	class Node(object):
		def __init__(self,data):
			self.data = data
			self.next = None

	def delete(self,node):
		temp = node.next
		node.next = temp.next
		node.data = temp.data
		temp = None

	def reversek(self,head,k):
		curr = head
		next = None
		prev = None
		c = 0
		while curr!=None and c<k:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
			c+=1
		if next!=None:
			head.next = self.reversek(next,k)
		return prev

	def getcount(self):
		c = 0
		temp = self.head
		while(temp!=None):
			temp = temp.next
			c+=1
		return c

	def printlist(self):
		temp = self.head
		while(temp!=None):
			print temp.data,
			temp = temp.next
		print

	def push(self, new_data):
		new_Node = self.Node(new_data)
		new_Node.next = self.head
		self.head = new_Node
 

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(4)
llist.push(1)
llist.push(5)
llist.push(1)
llist.push(4)
llist.printlist()
llist.head = llist.reversek(llist.head,3)
llist.printlist()
# llist.printlist()
# res = llist.merge(llist)
