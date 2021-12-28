def check_queen(depth, row, visited): # board[row][depth]
    for r in range(depth):
        if row == visited[r]: return True # 같은 행에 퀸 존재
        if abs(row - visited[r]) == depth - r: return True # 대각선에 퀸 존재
    return False

def dfs(depth, n, visited):
    if depth == n:
        return 1
    answer = 0
    for row in range(n):
        if check_queen(depth, row, visited): continue # 퀸이 존재
        visited[depth] = row
        answer += dfs(depth+1, n, visited)
        visited[depth] = 0
    return answer
    
def solution(n):
    visited = [0] * n
    return dfs(0, n, visited)
