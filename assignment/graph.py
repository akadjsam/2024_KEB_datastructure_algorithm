from collections import  deque
class Graph() :
    def __init__ (self, size) :
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def print_graph(g) :
    print(' ', end = ' ')
    for v in range(g.SIZE) :
        print(store_ary[v][0], end =' ')
    print()
    for row in range(g.SIZE) :
        print(store_ary[row][0], end =' ')
        for col in range(g.SIZE) :
            print(g.graph[row][col], end= '  ')
        print()
    print()


## 전역 변수 선언 부분 ##
G1 = None
store_ary = [['GS', 30], ['CU', 60], ['SV', 10], ['MN', 90], ['EM', 40]]

## 메인 코드 부분 ##
g_size = 5
G1 = Graph(g_size)
G1.graph[0][1] = 1; G1.graph[0][2] = 1;
G1.graph[1][0] = 1; G1.graph[1][2] = 1; G1.graph[1][3] = 1;
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1;
G1.graph[3][1] = 1; G1.graph[3][2] = 1; G1.graph[3][4] = 1;
G1.graph[4][3] = 1;

weight = store_ary[0][1]
print('## G1 무방향 그래프 ##')
print_graph(G1)

q = deque([0])
for i in range(len(store_ary)):
    if store_ary[i][1] > weight:
        weight = store_ary[i][1]

print(weight)
