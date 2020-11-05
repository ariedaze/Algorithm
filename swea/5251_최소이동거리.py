from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        # 유향그래프
        G[u].append([v, w])

    D = [0xffffff] * (N + 1)
    D[0] = 0
    # 1: 선택된 정점(최단경로를 찾은 정점), 0: 선택안된 정점(최단경로 확정 안됨)
    visit = [0] * (N + 1)
    cnt = 0


    # Q = deque()
    # Q.append(0)

    # if D[v] > D[u] +(u,v):
    #     D[v] = D[u] + (u,v)

    # while True:
    #     flag = True
    #     for u in range(N+1):
    #         for v,w in G[u]:
    #             if D[v] > D[u]+w:
    #                 D[v] = D[u]+2
    #                 flag = False
    #     if flag: break

    # while Q:
    #     u = Q.popleft()
    #     for v, w in G[u]:
    #         if D[v] > D[u]+w:
    #             D[v] = D[u]+w
    #             Q.append(v)

    def dfs(u):
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                dfs(v)

    dfs(0)

    while cnt < N + 1:
        # visit[] == 0, D[] 값이 최소인 정점
        u, Min = 0, 0xfffffff
        for i in range(N + 1):
            if visit[i] == 0 and Min > D[i]:
                u, Min = i, D[i]
        visit[u] = 1

        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
        cnt += 1

    print(f'#{tc} {D[N]}')
