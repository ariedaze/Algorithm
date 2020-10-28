for tc in range(1, int(input()) + 1):
    N = int(input())
    score = list(map(int, input().split()))

    visit = [0] * (sum(score) + 1)
    Q = [0]

    for value in score:
        for i in range(len(Q)):
            if visit[Q[i] + value]: continue
            visit[Q[i] + value] = 1
            Q.append(Q[i] + value)

    print(f'#{tc} {len(Q)}')
