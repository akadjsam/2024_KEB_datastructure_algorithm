from collections import deque

graph =[
    [0,1,1,0,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [0,1,1,0,1,1,1,0],
    [0,0,0,1,0,1,0,0],
    [0,0,0,1,1,0,0,0],

    [0,0,0,1,0,0,0,1],
    [0,0,0,0,0,0,1,0]
]

def dfs(g, v, visited):
    visited[v] = True
    print(chr(ord('A')+v),end=' ')
    for i in range(len(g)):
        if g[v][i] == True and not visited[i]:
            dfs(g,i,visited)

def bfs(g,v,visited):
    queue = deque([v])
    visited[v] = 1
    while queue:
        v = queue.popleft()
        print(chr(ord('A')+v),end=' ')
        for i in range(len(g)):
            if g[v][i] == True and not visited[i]:
                queue.append(i)
                visited[i] = 1

visited1 = [False]*len(graph)
visited2 = [False]*len(graph)

dfs(graph,0,visited1)
print()
bfs(graph,0,visited2)