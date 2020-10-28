import sys


sys.stdin = open('input/암호코드스캔.txt', 'r')

code = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}

hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000',
    '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    secrets = [input() for _ in range(N)]
    ans = 0
    breaker = False

    # 2진수로 바꾸기
    for i in range(N):
        new_line = ''
        for j in range(M):
            binary = hex_to_bin.get(secrets[i][j])
            new_line += binary
        secrets[i] = new_line

    # 암호 코드의 비율
    secret = [0] * 8
    for i in range(N):
        if secrets[i] == '0'*M*4: continue
        idx = M*4-1
        cnt = 7
        while idx >= 0:
            if (i == 0 or secrets[i-1][idx] == '0') and secrets[i][idx] == '1':
                c1 = c2 = c3 = 0
                while secrets[i][idx] == '1': c3 += 1; idx -= 1
                while secrets[i][idx] == '0': c2 += 1; idx -= 1
                while secrets[i][idx] == '1': c1 += 1; idx -= 1
                mini = min(c1, c2, c3)
                c1 //= mini
                c2 //= mini
                c3 //= mini
                secret[cnt] = code.get((c1, c2, c3))
                cnt -= 1
                if cnt == -1:
                    verification = sum(secret) + 2*(secret[0]+secret[2]+secret[4]+secret[6])
                    if verification % 10 == 0:
                        ans += sum(secret)
                    secret = [0] * 8
                    cnt = 7
            else:
                idx -= 1

    print(f'#{tc} {ans}')
