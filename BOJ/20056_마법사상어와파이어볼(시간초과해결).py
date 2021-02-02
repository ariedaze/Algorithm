def move_and_sum():
    # 1. 이동하기
    new_fireballs = {}
    for r, c in fireballs.keys():
        for ball in fireballs[(r, c)]:
            m, s, d = ball
            s %= N
            new_r = (r + (s * dr[d]) + N) % N
            new_c = (c + (s * dc[d]) + N) % N

            if (new_r, new_c) in new_fireballs.keys():
                new_fireballs[(new_r, new_c)].append(ball)
            else:
                new_fireballs[new_r, new_c] = [ball]

    # 2. 합치기
    for key in new_fireballs.keys():
        if len(new_fireballs[key]) > 1:
            new_m = new_s = 0
            odd = even = True
            for ball in new_fireballs[key]:
                m, s, d = ball
                new_m += m
                new_s += s
                if d % 2 == 0:
                    odd = False
                else:
                    even = False

            new_m //= 5
            new_s //= len(new_fireballs[key])
            new_fireballs[key] = []
            if new_m == 0: continue
            if odd or even:
                dirs = [0, 2, 4, 6]
            else:
                dirs = [1, 3, 5, 7]
            for d in dirs:
                new_fireballs[key].append((new_m, new_s, d))

    return new_fireballs


N, M, K = map(int, input().split())

fireballs = {}

# direction
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for idx in range(M):
    r, c, m, s, d = map(int, input().split())
    r -= 1; c -= 1;
    fireballs[(r, c)] = [(m, s, d)]

while K:
    K -= 1
    fireballs = move_and_sum()

result = 0
for key in fireballs.keys():
    for ball in fireballs[key]:
        result += ball[0]

print(result)