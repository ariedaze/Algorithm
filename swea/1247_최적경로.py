def service(cnt, start, sum):
    global answer

    if cnt == N:
        sum += abs(start[0]-home[0]) + abs(start[1]-home[1])
        answer = min(sum, answer)
        return

    if sum >= answer:
        return

    for i in range(N):
        if start == new[i] or visited[i]: continue
        visited[i] = 1
        service(cnt+1, new[i], sum + abs(start[0]-new[i][0]) + abs(start[1]-new[i][1]))
        visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    new = []
    answer = 10**7

    visited = [0]*N
    company = (arr[0], arr[1])
    home = (arr[2], arr[3])

    for i in range(4, 2*(N+2), 2):
        new.append((arr[i], arr[i+1]))

    service(0, company, 0)
    print(f'#{tc} {answer}')
