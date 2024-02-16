from collections import deque

# input_data = list(map(int, input().split()))
n,m,k,x=  map(int, input().split())
b = []
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)

distance = [-1] * (n+1)
distance[x] = 0

# bfs
q = deque([x])
while q:
    now = q.popleft()
    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)