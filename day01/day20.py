graph =[
    [0,1,1,0,0,0],
    [1,0,0,1,0,0],
    [1,0,0,1,0,0],
    [0,1,1,0,1,1],
    [0,0,0,1,0,1],
    [0,0,0,1,1,0]
]
name_array=['문별','솔라','휘인','쯔위','선미','화사']

def dfs(g, v, visited):
    visited[v] = True
    print(name_array[v],end=' ')
    for i in range(len(g)):
        if g[v][i] == True and not visited[i]:
            dfs(g,i,visited)

visited = [False]*len(graph)

dfs(graph,0,visited)
'''
G1 = Graph(5)
G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1
G1.graph[2][4] = 1; G1.graph[4][2] = 1
'''