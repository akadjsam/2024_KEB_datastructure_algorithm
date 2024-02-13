## 클래스와 함수 선언 부분 ##
import random
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    if current.link == None :
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()

def insert_node(find_data, insert_data) :
    global head, current, pre

    if head.data == find_data :		# 첫 번째 노드 삽입
        node = Node()
        node.data = insert_data
        node.link = head
        last = head		# 마지막 노드를 첫 번째 노드로 우선 지정
        while last.link != head :	# 마지막 노드를 찾으면 반복 종료
            last = last.link	# last를 다음 노드로 변경
        last.link = node		# 마지막 노드의 링크에 새 노드 지정
        head = node
        return

    current = head
    while current.link != head:		# 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node()			 # 마지막 노드 삽입
    node.data = insert_data
    current.link = node
    node.link = head

def delete_node(delete_data):
    global head, current, pre

    if head.data == delete_data:         # 첫 번째 노드 삭제
        current = head
        head = head.link
        last = head
        while last.link is not current:	# 마지막 노드를 찾으면 반복 종료
            last = last.link	# last를 다음 노드로 변경
        last.link = head		# 마지막 노드의 링크에 새 노드 지정
        del(current)
        return

    current = head                          # 첫 번째  외 노드 삭제
    while current.link is not head:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            del(current)

            return
def find_node(find_data) :
    global head, current, pre

    current = head
    if current.data == find_data:
        return current
    while current.link is not head:
        current = current.link
        if current.data == find_data:
            return current
    return Node() # 빈 노드 반환

# def cheking_number():
#     global head, current, pre
#
#     odd_count = 0
#     even_count = 0
#     current = head
#     while current.link is not head:
#         if current.data % 2 == 0:
#             odd_count += 1
#         else:
#             even_count += 1
#     print(odd_count)
#     current = head
#     if odd_count > even_count:
#         while current.link is not head:
#             if current.data % 2 == 0:
#                 current.data = -1 * current.data
#     else:
#         while current.link is not head:
#             if current.data % 2 == 1:
#                 current.data = -1 * current.data
#
#         current = current.link

def cheking_number(datas):
    global head, current

    odd_count = 0
    even_count = 0
    for i in datas:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if even_count > odd_count:
        remainder = 0
    else:
        remainder = 1
    current = head
    while True:
        if current.data % 2 == remainder:
            current.data = current.data * -1
        if current.link == head:
            break
        current = current.link

head, current, pre = None, None, None
data_array = []
[data_array.append(random.randint(1, 100)) for i in range(7)]

## 메인 코드 부분 ##
if __name__ == "__main__" :

    node = Node()
    node.data = data_array[0]	# 첫 번째 노드
    head = node
    node.link = head

    for data in data_array[1:] :	# 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head

    cheking_number(data_array)
    #cheking_number()
    print_nodes(head)