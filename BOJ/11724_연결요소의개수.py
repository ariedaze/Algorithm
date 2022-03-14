N, M = map(int, input().split())
visited = [0] * N
graph = [[] * N for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

answer = 0

def dfs(u, visited):
    for v in graph[u]:
        if visited[v]: continue
        visited[v] = 1
        dfs(v, visited)


for i in range(N):
    if visited[i]: continue
    visited[i] = 1
    dfs(i, visited)
    answer += 1


print(answer)
