# 남 > 스위치 번호가 번호의 배수이면 체인지
# 여 > 번호를 중심으로 대칭인지 확인

switch_num = int(input())
switches = list(map(int, input().split()))
people_num = int(input())
case = [list(map(int, input().split())) for _ in range(people_num)]

def man(switches, n):
    for num in range(n, switch_num+1, n):
        switches[num-1] = 0 if switches[num-1] else 1

def woman(switches, n):
    n -= 1
    prev = next = n
    while 0 <= prev < switch_num and 0 <= next < switch_num:
        if switches[prev] != switches[next]:
            break
        prev -= 1
        next += 1

    for i in range(prev+1, next):
        switches[i] = 0 if switches[i] else 1


for gender, n in case:
    if gender == 1: # 남
        man(switches, n)
    else: # 여
        woman(switches, n)

for i in range(0, switch_num, 20):
    end = i + 20
    if end > switch_num: end = switch_num
    print(*switches[i:end])