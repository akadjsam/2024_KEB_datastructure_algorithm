import random
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
        data_array.append(random.randint(1,45))
        set_list = set(data_array)
        if len(set_list) == 6:
            break
        else:
            data_array = list(set_list)

    node = Node()  # 첫 번째 노드
    node.data = data_array[0]
    head = node

    for data in data_array[1:]:  # 두 번째 노드부터
        pre = node
        node = Node()
        node.data = data
        pre.link = node

    print_nodes(head)