# 다음 depth 에서의 시작값(begin_wwith c ztg)
def combination(depth, r, begin_with, arr, result): #조합
    if depth == r:
        print(result)
        return
    
    for i in range(begin_with, len(arr)):
        result[depth] = arr[i]
        combination(depth+1, r, i+1, arr, result)

# 체크리스트
def permutation(depth, r, arr, visited, result): #순열
    if depth == r:
        print(result)
        return
    
    for i in range(len(arr)):
        if visited[i]: continue
        visited[i] = 1
        result[depth] = arr[i]
        permutation(depth+1, r, arr, visited, result)
        visited[i] = 0

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    # 5C2
    combination(0, 2, 0, arr, [0]*2)

    # 5P2
    permutation(0, 2, arr, [0]*len(arr), [0]*2)
