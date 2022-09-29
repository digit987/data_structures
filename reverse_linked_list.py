class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
class Operations:
	def __init__(self):
		self.head = None
		
	def create_node(self, data):
		current = self.head
		if self.head is None:
			current = Node(data)
			self.head = current
		else:
			while current.next is not None:
				current = current.next
			current.next = Node(data)
			
	def print_linked_list(self):
		current = self.head
		while current is not None:
			print(current.data)
			current = current.next

	def reverse_linked_list(self):
		prev = temp = None
		current = self.head
		while current is not None:
			if current.next is None:
				self.head = current
			temp = current.next
			current.next = prev
			prev = current
			current = temp

op = Operations()
while True:
	print("1. Enter data")
	print("2. Print list")
	print("3. Print reverse list")
	print("4. Exit")
	choice = int(input("Enter your choice"))
	if choice == 1:
		data = input("Enter node value: ")
		op.create_node(data)
	if choice == 2:
		op.print_linked_list()
	if choice == 3:
		print("Printing reversed list")
		op.reverse_linked_list()
		op.print_linked_list()
	if choice == 4:
		exit()
