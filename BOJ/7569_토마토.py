from collections import deque


M, N, H = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N*H)]
empty_cnt = ripe_cnt = answer = 0
Q = deque()

# 좌우상하 and 위 아래의 다른 상자
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        for k in range(H):
            x = i+k*N
            if box[x][j] == 1:
                ripe_cnt += 1
                Q.append((x, j))
            elif box[x][j] == -1:
                empty_cnt += 1

# 토마토 갯수
tomato_num = M*N*H - empty_cnt
# print(tomato_num)

if tomato_num == ripe_cnt:
    print(0)
else:
    while Q:
        i, j = Q.popleft()
        for mode in range(4):
            new_i = i + di[mode]
            new_j = j + dj[mode]
            if 0 <= new_i < N*H and 0 <= new_j < M and box[new_i][new_j] == 0:
                box[new_i][new_j] = box[i][j] + 1
                Q.append((new_i, new_j))
                ripe_cnt += 1
                answer = max(answer, box[new_i][new_j])
        top_i = i - N # 위
        bottom_i = i + N # 아
        if 0 <= top_i < N*H and box[top_i][j] == 0:
            box[top_i][j] = box[i][j] + 1
            Q.append((top_i, j))
            ripe_cnt += 1
            answer = max(answer, box[top_i][j])
        if 0 <= bottom_i < N*H and box[bottom_i][j] == 0:
            box[bottom_i][j] = box[i][j] + 1
            Q.append((bottom_i, j))
            ripe_cnt += 1
            answer = max(answer, box[bottom_i][j])

    if tomato_num == ripe_cnt:
        print(answer)

    else:
        print(-1)

