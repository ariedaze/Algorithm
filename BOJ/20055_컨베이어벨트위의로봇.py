from collections import deque

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([0]*N*2)
ans = 1

while True:
    # 1. 벨트가 회전한다 > robot 위치도 같이 회전
    belt.rotate(1)
    robots.rotate(1)
    # 내려가는 위치의 로봇
    robots[N-1] = 0

    # 2. 로봇이 1칸 이동한다 (다음칸에 로봇이 없고 내구도가 1이상)
    for i in range(N-2, -1, -1):
        if robots[i] and robots[i+1] == 0 and belt[i+1] > 0:
            belt[i+1] -= 1
            robots[i+1] = 1
            robots[i] = 0
    # 내려가는 위치의 로봇
    robots[N-1] = 0

    # 3. 올라가는 위치에 로봇이 없다면 로봇을 올린다
    if robots[0] == 0 and belt[0] > 0:
        belt[0] -= 1
        robots[0] = 1

    # 내구도가 0인 칸의 개수가 K개 이상이면 종료한다.
    cnt = 0
    for i in range(2*N):
        if belt[i] == 0:
            cnt += 1
    if cnt >= K:
        break

    # 단계 증가
    ans += 1

print(ans)
