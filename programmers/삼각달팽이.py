def solution(n):
    answer = []
    for i in range(1, n+1):
        answer.append([0] * i)
    
    here = mode = 0
    i, j = -1, 0
    
    while n > 0:
        line = n        
        for _ in range(line):
            here += 1
            if mode == 0: # 아래
                i += 1
            elif mode == 1: # 옆
                j += 1
            else: # 위
                i -= 1; j-= 1
            answer[i][j] = here
        
        n -= 1
        mode += 1
        mode %= 3
    
    return sum(answer, [])
