import sys

N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
quest = [map(int, sys.stdin.readline().split()) for _ in range(M)]

sum_arr = [[0] * (N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        sum_arr[i+1][j+1] = (sum_arr[i][j+1] + sum_arr[i+1][j] - sum_arr[i][j]) + arr[i][j]

for k in range(M):
    x1, y1, x2, y2 = quest[k]
    print(sum_arr[x2][y2] - sum_arr[x2][y1-1] - sum_arr[x1-1][y2] + sum_arr[x1-1][y1-1])
