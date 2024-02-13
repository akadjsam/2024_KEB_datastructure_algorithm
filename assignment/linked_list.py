class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def print_nodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()

def simple_list(name_email) :
	global head, current, pre
	print_nodes(head)

	node = Node()
	node.data = name_email
	if head == None:
		head = node
		return

	if head.data[1] > name_email[1]:
		node.link = head
		head = node
		return

	current = head
	while current.link != None :
		pre = current
		current = current.link
		if current.data[1] > name_email[1]:
			pre.link = node
			node.link = current
			return
	current.link = node
head, current, pre = None, None, None
data_array = []

if __name__ == "__main__" :
    while True:
        name = input("이름 : ")
        email = input("이메일 : ")
        if name == "" or email == "":
            break
        linked_list = name, email
        linked_list = list(linked_list)
        data_array.append(linked_list)
    for data in data_array:
        simple_list(data)
    print_nodes(head)
