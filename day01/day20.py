## 클래스와 함수 선언 부분 ##
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    if current == None :
        return
    print(current.data, end= ' ')
    while current.link is not None:
        current = current.link
        print(current.data, end= ' ')
    print()

def insert_node(find_data, insert_data):
    global head, current, pre

    if head.data == find_data: #첫번째에 노드 삽입
        node = Node()
        node.data = insert_data
        node.link = head
        head = node
        return

    current = head

    while current.link is not None: #중간에 삽입
        pre = current
        current = current.link
        if current.data == find_data :
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node() #마지막 노드
    node.data = insert_data
    current.link = node

def delete_node(delete_data) :
    global memory, head, current, pre

    if head.data == delete_data:         # 첫 번째 노드 삭제
        current = head
        head = head.link
        #print(f'{delete_data}이(가) 삭제되었습니다.')
        del(current)
        return

    current = head                          # 첫 번째  외 노드 삭제
    while current.link is not None:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            #print(f'{delete_data}이(가) 삭제되었습니다.')
            del(current)
            return
    #print(f'{delete_data}은 리스트에 없음')

def find_node(find_data) :
    global memory, head, current, pre

    current = head
    if current.data == find_data:
        return current
    while current.link is not None:
        current = current.link
        if current.data == find_data:
            return current
    return Node() # 빈 노드 반환

head, current, pre = None, None, None
data_array = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__" :

    node = Node()
    node.data = data_array[0]
    head = node

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node

    print_nodes(head)
    insert_node("다현", "화사")
    print_nodes(head)

    insert_node("사나", "솔라")
    print_nodes(head)

    insert_node("1111", "문별")
    print_nodes(head)

    delete_node("다현")
    print_nodes(head)

    delete_node("쯔위")
    print_nodes(head)

    delete_node("지효")
    print_nodes(head)

    delete_node("랜덤")
    print_nodes(head)

    delete_node("화사")
    print_nodes(head)

    f_node = find_node("정연")
    print(f_node.data)

    f_node = find_node("현일")
    print(f_node.data)