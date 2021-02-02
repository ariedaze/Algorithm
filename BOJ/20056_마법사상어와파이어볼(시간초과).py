import copy

def move(N):
    new_map = [[[]for _ in range(N)] for _ in range(N)]
    for idx in range(len(fireballs)):
        r, c, mass, speed, dir = fireballs[idx]
        # 1번과 N번 행, 열이 연결됨
        speed %= N
        # 음수일 수 있기 때문에 N을 더하고 %연산
        nr = (r + (dr[dir] * speed) + N) % N
        nc = (c + (dc[dir] * speed) + N) % N
        new_map[nr][nc].append(idx)
        fireballs[idx][0] = nr
        fireballs[idx][1] = nc
    for i in range(N):
        for j in range(N):
            maps[i][j] = copy.deepcopy(new_map[i][j])


def sum_balls():
    global fireballs
    new_balls = []
    for i in range(N):
        for j in range(N):
            if len(maps[i][j]) == 1:
                new_balls.append(fireballs[maps[i][j][0]])
            # s = 합/5    m = 합/수    모두홀짝=0, 2, 4, 6 아니면 1, 3, 5, 7
            elif len(maps[i][j]) > 1:
                sum_s = sum_m = 0
                odd = even = True
                for k in range(len(maps[i][j])):
                    index = maps[i][j][k]
                    sum_m += fireballs[index][2]
                    sum_s += fireballs[index][3]
                    if (fireballs[index][4] % 2) == 0:
                        odd = False
                    else:
                        even = False
                if sum_m // 5 == 0: continue

                new_m = sum_m // 5
                new_s = sum_s // len(maps[i][j])

                for z in range(4):
                    if odd or even:
                        new_balls.append([i, j, new_m, new_s, z*2])
                    else:
                        new_balls.append([i, j, new_m, new_s, z*2 + 1])
    fireballs = copy.deepcopy(new_balls)

# N : map 크기 | M: 파이어볼 수 | K: 이동 수
N, M, K = map(int, input().split())
maps = [[[]for _ in range(N)] for _ in range(N)]
fireballs = [[] for _ in range(M)]


# direction
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(M):
    # r c(0, 1): 좌표    m(2) : 질량     s(3) : 칸 수    d(4) : 방향
    r, c, m, s, d = map(int, input().split())
    r -= 1
    c -= 1
    fireballs[i] = [r, c, m, s, d]

    # maps에 fireball index 저장
    maps[r][c].append(i)


while K:
    K -= 1
    # ball 이동하기
    move(N)
    # ball 합치기
    sum_balls()

# fireballs.values의 index 2(m)의 합
result = 0
for ball in fireballs:
    result += ball[2]

print(result)