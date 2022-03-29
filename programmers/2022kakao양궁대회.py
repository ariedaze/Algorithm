answer = []
max_diff = 0

def solution(n, info):
    dfs(0, n, apeach=info, ryan=[0]*11)
    if answer:
        return sorted(answer, key = lambda x: x[::-1], reverse=True)[0]
    else:
        return [-1]


def dfs(depth, arrow, apeach, ryan):
    global max_diff, answer
    if depth == 11:
        arrow_temp = ryan[10]
        if arrow:
            ryan[10] = arrow
        score_diff = calculate_score_diff(ryan, apeach)
        if score_diff <= 0:
            if arrow: ryan[10] = arrow_temp
            return
        candi_answer = ryan[:]
        if score_diff > max_diff:
            max_diff = score_diff
            answer = [candi_answer]
        elif score_diff == max_diff:
            answer.append(candi_answer)
            
        ryan[10] = arrow_temp
        return
    # apeach + 1
    if apeach[depth] < arrow:
        temp = ryan[depth]
        ryan[depth] = apeach[depth] + 1
        dfs(depth+1, arrow-apeach[depth]-1, apeach, ryan)
        ryan[depth] = 0
    # 0
    dfs(depth+1, arrow, apeach, ryan)
    
    
def calculate_score_diff(ryan, apeach):
    apeach_score = ryan_score = 0
    
    for i in range(11):
        if not ryan[i] and not apeach[i]: continue # a = b = 0
        if ryan[i] > apeach[i]:
            ryan_score += 10 - i
        else:
            apeach_score += 10 - i
            
    return ryan_score - apeach_score
