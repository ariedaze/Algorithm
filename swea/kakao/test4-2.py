
max_diff = -1

def solution(n, info):
    answer = [0] * 11
    ryan = [0] * 11

    def combination(depth, begin_with, k):
        global max_diff
        if k <= 0 or depth == 9:
            # 점수계산
            ryan_score = apeach_score = 0
            for r in range(10):
                if ryan[r]:
                    ryan_score += 10 - r
                elif info[r]:
                    apeach_score += 10 - r

            # answer 변경
            diff = ryan_score - apeach_score
            if diff > max_diff:
                max_diff = diff
                for i in range(11):
                    answer[i] = ryan[i]
                cnt = sum(answer)
                if cnt < n:
                    answer[10] = n - cnt

            elif diff != 0 and diff == max_diff:
                cnt = sum(ryan)
                if cnt < n:
                    ryan[10] = n - cnt
                for l in range(10,-1,-1):
                    if ryan[l] > answer[l]:
                        for i in range(11):
                            answer[i] = ryan[i]
                        ryan[10] = 0
                        return
                ryan[10] = 0
            return

        for i in range(begin_with, 10):
            # i번째 점수를 ryan이 얻는 경우
            new_k = k - info[i] - 1
            if new_k >= 0:
                ryan[i] = info[i] + 1
                combination(depth+1, begin_with+1, new_k)
            else:
                ryan_score = apeach_score = 0
                for r in range(10):
                    if ryan[r]:
                        ryan_score += 10 - r
                    elif info[r]:
                        apeach_score += 10 - r

                # answer 변경
                diff = ryan_score - apeach_score
                if diff > max_diff:
                    max_diff = diff
                    for i in range(11):
                        answer[i] = ryan[i]
                    cnt = sum(answer)
                    if cnt < n:
                        answer[10] = n - cnt

                elif diff != 0 and diff == max_diff:
                    cnt = sum(ryan)
                    if cnt < n:
                        ryan[10] = n - cnt
                    for l in range(10, -1, -1):
                        if ryan[l] > answer[l]:
                            for i in range(11):
                                answer[i] = ryan[i]
                            # ryan[10] = 0
                            # return
                    ryan[10] = 0
                    ryan[i] = 0
                    return
            ryan[i] = 0

    combination(0, 0, n)

    if max_diff <= 0:
        return [-1]

    return answer




# solution(5, [2,1,1,1,0,0,0,0,0,0,0])
# solution(9, [0,0,1,2,0,1,1,1,1,1,1])
