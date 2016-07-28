class LinkedList(object):
	def __init__(self):
		self.head = None
		self.second = None

	class Node(object):
		def __init__(self,data):
			self.data = data
			self.next = None

	def removeDup(self):
		if self.head==None:
			return
		temp = self.head
		next_next = None
		while temp.next!=None:
			if temp.data == temp.next.data:
				next_next = temp.next.next
				temp.next = None
				temp.next = next_next
			else:
				temp = temp.next


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
llist.push(1)
llist.push(3)
llist.push(4)
llist.push(4)
llist.push(4)
llist.push(7)
llist.printlist()
llist.removeDup()
llist.printlist()
# llist.printlist()
# res = llist.merge(llist)
