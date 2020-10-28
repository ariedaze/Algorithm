import sys


sys.stdin = open('input/단순2진암호코드.txt', 'r')

code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    secrets = [input() for _ in range(N)]
    secret = ''
    zero = '0'*M
    verification = []
    ans = 0

    for line in secrets:
        if line != zero:
            for i in range(M-1, -1, -1):
                if line[i] == '1':
                    secret = line[i-55:i+1]
                    break
            break

    for i in range(0, 56, 7):
        verification.append(code.get(secret[i:i+7]))

    for j in range(0, 8, 2):
        ans += verification[j]*3
        ans += verification[j+1]

    if ans % 10 == 0:
        print(f'#{tc} {sum(verification)}')
    else:
        print(f'#{tc} 0')