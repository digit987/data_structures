'''
We print the items of a linked list in reverse i.e. without reversing the actual list.
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


def print_linked_list(current):
	global list
	if current.next is not None:
		print_linked_list(current.next)
	print(current.data)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
current = head
print_linked_list(current)
