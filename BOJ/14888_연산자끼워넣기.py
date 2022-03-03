from collections import deque

N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split()) # + - x /

max_ = -1e9
min_ = 1e9

def dfs(depth, dfs_sum, add, sub, mul, div):
    global min_, max_

    if depth == N:
        min_ = min(min_, dfs_sum)
        max_ = max(max_, dfs_sum)
        return
    
    if add:
        dfs(depth+1, dfs_sum + numbers[depth], add-1, sub, mul, div)
    if sub:
        dfs(depth+1, dfs_sum - numbers[depth], add, sub-1, mul, div)
    if mul:
        dfs(depth+1, dfs_sum * numbers[depth], add, sub, mul-1, div)
    if div:
        dfs(depth+1, int(dfs_sum / numbers[depth]), add, sub, mul, div-1)


dfs(1, numbers[0], add, sub, mul, div)

print(max_)
print(min_)
