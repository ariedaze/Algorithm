for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        # 무향 그래프
        G[u].append([v, w])
        G[v].append([u, w])

    key = [0xffffff] * (V+1)
    pi = [0] * (V+1)
    key[0] = 0
    visit = [0] * (V+1) # 0: 큐에 있다(비트리 정점) 1: 큐에서 빠졌다(트리 정점)

    cnt = ans = 0
    while cnt < V + 1:
        u, Min = 0, 0xffffff
        for i in range(V+1):
            if visit[i] == 0 and Min > key[i]:
                u, Min = i, key[i]
        visit[u] = 1

        ans += key[u]

        for v, w in G[u]:
            if visit[v] == 0 and key[v] > w:
                key[v] = w
                pi[v] = u
        cnt += 1

    print(f'#{tc} {sum(key)}')
