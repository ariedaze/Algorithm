N = int(input())
classroom = [[0]*N for _ in range(N)]
favorite = {}
for _ in range(N*N):
    a = list(map(int, input().split()))
    favorite[a[0]] = a[1:]
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
def check_favorite(classroom, friends):
    seats = []
    max_score = 0
    for i in range(N):
        for j in range(N):
            if classroom[i][j]: continue
            score = 0
            for dir in dirs: # i, j에서 4방향 체크
                x, y = i + dir[0], j + dir[1]
                if 0 <= x < N and 0 <= y < N and classroom[x][y] in friends:
                    score += 1
            if score > max_score:
                max_score = score
                seats = [(i, j)]
            elif score == max_score:
                seats.append((i, j))
    return seats

# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
def check_empty(classroom, seats):
    new_seats = []
    max_score = 0
    for i, j in seats:
        score = 0
        for dir in dirs: # i, j에서 4방향 체크
            x, y = i + dir[0], j + dir[1]
            if 0 <= x < N and 0 <= y < N and not classroom[x][y]:
                score += 1
        if score > max_score:
            max_score = score
            new_seats = [(i, j)]
        elif score == max_score:
            new_seats.append((i, j))
    return new_seats

# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
def check_row_col(seats):
    return sorted(seats, key=lambda x: (x[0], x[1]))[0]


# 만족도 0(0) 1(1) 10(2) 100(3) 1000(4)
def get_score(classroom):
    answer = 0
    for i in range(N):
        for j in range(N):
            if favorite.get(classroom[i][j]) is None: continue
            friends = favorite[classroom[i][j]]
            score = 0
            for dir in dirs:
                x, y = i + dir[0], j + dir[1]
                if 0 <= x < N and 0 <= y < N and classroom[x][y] in friends:
                    score += 1
            if score == 1:
                answer += 1
            elif score == 2:
                answer += 10
            elif score == 3:
                answer += 100
            elif score == 4:
                answer += 1000
    return answer
            
for key, value in favorite.items():
    seats = check_favorite(classroom, value)
    # print(key, "=========")
    # print("1seats", seats)
    if len(seats) == 1:
        # print("여기다!", seats[0][0], seats[0][1])
        classroom[seats[0][0]][seats[0][1]] = key
        continue
    new_seats = check_empty(classroom, seats)
    # print("2seats", new_seats)
    if len(new_seats) == 1:
        # print("여기다!", new_seats[0][0], new_seats[0][1])
        classroom[new_seats[0][0]][new_seats[0][1]] = key
        continue

    i, j = check_row_col(new_seats)
    # print("3seat 여기다", i, j)
    classroom[i][j] = key
# print("answer")
# for c in classroom:
#     print(*c)
print(get_score(classroom))
