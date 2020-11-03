def dfs(part_sum, cnt):
    global ans

    if part_sum >= ans:
        return

    if cnt == N:
        ans = min(ans, part_sum)
        return

    for product in range(N):
        if done[product]: continue
        done[product] = 1
        dfs(part_sum + arr[product][cnt], cnt + 1)
        done[product] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    done = [0] * N
    ans = 99 * 15 * 15

    dfs(0, 0)

    print(f'#{tc} {ans}')
