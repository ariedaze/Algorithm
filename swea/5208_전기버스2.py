def dfs(cnt, start, end):
    global ans

    if cnt >= ans:
        return

    if end >= N:
        ans = min(cnt, ans)
        return

    can_go = range(start+1, end+1)
    for station in can_go:
        dfs(cnt + 1, station, station + arr[station])


for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    road = [1]
    roads = []
    ans = N
    dfs(0, 1, 1 + arr[1])

    print(f'#{tc} {ans}')
