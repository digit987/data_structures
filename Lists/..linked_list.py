class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

def print_linked_list():
	global head
	current = head
	while current is not None:
		print(current.data)
		current = current.next

def reverse_linked_list():
	global head
	prev = temp = None
	current = head
	while current is not None:
		if current.next is None:
			head = current
		temp = current.next
		current.next = prev
		prev = current
		current = temp

print("Printing original list")
print_linked_list()

print("Printing reversed list")
reverse_linked_list()
print_linked_list()
