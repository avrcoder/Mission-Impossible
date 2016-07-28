class LinkedList(object):
	def __init__(self):
		self.head = None
		self.second = None

	class Node(object):
		def __init__(self,data):
			self.data = data
			self.next = None

	def midnode(self):
		slow = self.head
		fast = self.head
		slow_prev = self.head
		midnode = None
		res = True
		if self.head!=None and self.head.next!=None:
			while fast!=None and fast.next!=None:
				fast = fast.next.next
				slow_prev = slow
				slow = slow.next
		return slow.data
	# 	if fast!=None:
	# 		midnode = slow
	# 		slow = slow.next
	# 	self.second = slow
	# 	slow_prev.next = None
	# 	self.reverse()
	# 	self.printlist(self.head)
	# 	self.printlist(self.second)	
	# 	res = self.compare(self.head,self.second)
	# 	return res

	# def compare(self,node1,node2):
	# 	curr1 = node1
	# 	curr2 = node2
	# 	while curr1!=None and curr2!=None:
	# 		if curr1.data == curr2.data:
	# 			curr1 = curr1.next
	# 			curr2 = curr2.next
	# 		else:
	# 			return False
	# 	if curr1==None and curr2==None:
	# 		return True
	# 	else:
	# 		return False

	# def reverse(self):
	# 	prev = None
	# 	curr = self.second
	# 	next = None
	# 	while curr!=None:
	# 		next = curr.next
	# 		curr.next = prev
	# 		prev = curr
	# 		curr = next
	# 	self.second = prev


	# def getcount(self):
	# 	c = 0
	# 	temp = self.head
	# 	while(temp!=None):
	# 		temp = temp.next
	# 		c+=1
	# 	return c

	def printlist(self,curr):
		temp = curr
		while(temp!=None):
			print temp.data,
			temp = temp.next
		print

	def push(self, new_data):
		new_Node = self.Node(new_data)
		new_Node.next = self.head
		self.head = new_Node
 

llist = LinkedList()
llist.push('a')
llist.push('b')
llist.push('a')
llist.push('c')
llist.push('a')
llist.push('b')
llist.push('a')
print llist.MidNode()
# llist.printlist()
# res = llist.merge(llist)
