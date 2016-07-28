def sorted_intersect(self,a,b):
		if a==None or b==None:
			return None
		if a.data > b.data:
			return self.sorted_intersect(a,b.next)
		if a.data < b.data:
			return self.sorted_intersect(a.next,b)
		temp = Node(a.data)
		temp.next = self.sorted_intersect(a.next,b.next)
		return temp
		
# This function takes a and b as two linked list ad returns the head of the new linked list created which contains the intersecting nodes from
# the two linked lists
