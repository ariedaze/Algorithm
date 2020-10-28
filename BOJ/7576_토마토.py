from collections import deque
M, N = map(int, input().split()) # M은 가로, N은 세로
box = [list(map(int, input().split())) for _ in range(N)] # 없으면 -1 익은 것 1
empty_cnt = ripe_cnt = answer = 0
Q = deque()
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

# 토마토 확인
for i in range(N):
    for j in range(M):
        if box[i][j] == -1:
            empty_cnt += 1
        if box[i][j] == 1:
            ripe_cnt += 1
            Q.append((i, j))

days = [[0]*M for _ in range(N)]

# 토마토 갯수
tomato_num = M*N - empty_cnt


if tomato_num == ripe_cnt:
    print(0)
else:
    while Q:
        i, j = Q.popleft()
        for mode in range(4):
            new_i = i + di[mode]
            new_j = j + dj[mode]
            if 0 <= new_i < N and 0 <= new_j < M and box[new_i][new_j] == 0:
                box[new_i][new_j] = 1
                Q.append((new_i, new_j))
                ripe_cnt += 1
                days[new_i][new_j] = days[i][j] + 1
                answer = max(answer, days[new_i][new_j])

    if tomato_num == ripe_cnt:
        print(answer)

    else:
        print(-1)



