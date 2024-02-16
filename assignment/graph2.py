## 클래스 및 함수 선언 부분 ##
class Graph() :
	def __init__ (self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

def print_graph(g) :
    print(' ', end = ' ')
    for v in range(g.SIZE) :
        print(name_ary[v], end =' ')
    print()
    for row in range(g.SIZE) :
        print(name_ary[row], end =' ')
        for col in range(g.SIZE) :
            print("%2d" % g.graph[row][col], end = ' ')
        print()
    print()

def find_vertex(g, find_vtx) :
    stack = []
    visited_ary = []	# 방문한 노드

    current = 0	# 시작 정점
    stack.append(current)
    visited_ary.append(current)

    while (len(stack) != 0) :
        next = None
        for vertex in range(gSize) :
            if g.graph[current][vertex] != 0 :
                if vertex in visited_ary:	# 방문한 적이 있는 정점이면 탈락
                    pass
                else :			# 방문한 적이 없으면 다음 정점으로 지정
                    next = vertex
                    break

        if next != None :				# 다음에 방문할 정점이 있는 경우
            current = next
            stack.append(current)
            visited_ary.append(current)
        else :					# 다음에 방문할 정점이 없는 경우
            current = stack.pop()

    if find_vtx in visited_ary :
        return True
    else :
        return False


## 전역 변수 선언 부분 ##
G1 = None
name_ary = ['SL', 'NY', 'LD', 'BJ', 'BK', 'PS']

## 메인 코드 부분 ##
gSize = 6
G1 = Graph(gSize)
G1.graph = [[0,80,0,10,0,0],
            [80,0,0,40,70,0],
            [0,0,0,0,30,60],
            [10,40,0,0,50,0],
            [0,70,30,50,0,20],
            [0,0,60,0,20,0]]

print('케이블 건설을 위한 전체 연결도 ##')
print_graph(G1)

# 가중치 간선 목록
edge_ary = []
for i in range(gSize) :
    for k in range(gSize) :
        if G1.graph[i][k] != 0 :
            edge_ary.append([G1.graph[i][k], i, k])

from operator import itemgetter
edge_ary = sorted(edge_ary, key = itemgetter(0), reverse = False)

new_ary = []
for i in range(0, len(edge_ary), 2):
    new_ary.append(edge_ary[i])

index = 0
while (len(new_ary) > gSize - 1) :	# 간선의 개수가 '정점 개수-1'일 때까지 반복
    start = new_ary[index][1]
    end = new_ary[index][2]
    save_cost = new_ary[index][0]

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    start_yn = find_vertex(G1, start)
    end_yn = find_vertex(G1, end)

    if start_yn and end_yn :
        del (new_ary[index])
    else :
        G1.graph[start][end] = save_cost
        G1.graph[end][start] = save_cost
        index += 1

print('효율적인 도로 연결도 ##')
print_graph(G1)
