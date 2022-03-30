answer_list = []
relations = []
def solution(relation):
    global answer_list, relations
    relations = relation[:]
    col_length = len(relation[0])
    row_length = len(relation)
    
    arr = [set() for _ in range(col_length)]
    for r in range(row_length):
        for c in range(col_length):
            arr[c].add(relation[r][c])
    
    keys = []
    answer = 0
    for c in range(col_length):
        if len(arr[c]) == row_length:
            answer += 1
        else:
            keys.append(c)
            
    keys_length = len(keys)
    print(keys)
    for r in range(2, keys_length+1):
        dfs(0, keys_length, r, 0, keys, [0]*r)
    
    return answer + len(answer_list)


def dfs(depth, n, r, begin_with, keys, result):
    global answer_list
    if depth == r:
        print(result)
        result_set = set(result)
        
        # 최소성 체크
        for answer in answer_list:
            if answer & result_set == answer:
                return
        
        # 유일성 체크
        if is_candikey(result_set):
            answer_list.append(result_set)
        return
    
    for i in range(begin_with, n):
        result[depth] = keys[i]
        dfs(depth+1, n, r, i+1, keys, result)

def is_candikey(candi):
    global relations
    
    col_length = len(candi)
    row_length = len(relations)
    
    arr = set()
    
    for r in range(row_length):
        s = ""
        for c in candi:
            s += relations[r][c] + " "
        arr.add(s)
            
    
    if len(arr) == row_length:
        return True
    else:
        return False
