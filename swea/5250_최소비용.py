from collections import deque

T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    fuel = [[0xffffff] * N for _ in range(N)]
    fuel[0][0] = 0
    Q = deque()
    Q.append((0, 0))

    while Q:
        x, y = Q.popleft()

        for mode in range(4):
            nx, ny = x + dx[mode], y + dy[mode]
            if 0 <= nx < N and 0 <= ny < N:
                # 이동비용
                cost = 1
                if arr[nx][ny] > arr[x][y]:
                    cost += arr[nx][ny] - arr[x][y]
                # 연료 갱신
                if fuel[nx][ny] > fuel[x][y] + cost:
                    fuel[nx][ny] = fuel[x][y] + cost
                    Q.append((nx, ny))
    print(f'#{tc} {fuel[N-1][N-1]}')
