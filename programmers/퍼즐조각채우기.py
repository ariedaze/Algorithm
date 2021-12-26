
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, shape, board, puzzle):
    for mode in range(4):
        nx = x + dx[mode]
        ny = y + dy[mode]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == shape and not visited[nx][ny]:
            visited[nx][ny] = 1
            puzzle.append([nx, ny])
            dfs(nx, ny, shape, board, puzzle)
    return puzzle


def zero_position(puzzle):
    min_x = min(puzzle, key=lambda item: item[0])
    min_y = min(puzzle, key=lambda item: item[1])
    new_puzzle = []
    for p in puzzle:
        new_puzzle.append([p[0]-min_x[0], p[1]-min_y[1]])
    return sorted(new_puzzle)


def rotate(puzzle):
    new_puzzle = []
    max_x = max(puzzle, key=lambda item: item[0])
    for x, y in puzzle:
        new_puzzle.append([y, max_x[0] - x])
    return sorted(new_puzzle)


def solution(game_board, table):
    global visited, n, answer
    answer = 0
    n = len(game_board)
    visited = [[0]*n for _ in range(n)]

    blank = []
    puzzles = []

    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and not visited[i][j]:
                visited[i][j] = 1
                blank.append(zero_position(dfs(i, j, 0, game_board, [[i, j]])))

    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                puzzles.append(zero_position(dfs(i, j, 1, table, [[i, j]])))
    check = [0] * len(blank)

    for puzzle in puzzles:
        for idx, b in enumerate(blank):
            if check[idx]: continue
            if len(puzzle) != len(b): continue
            breaker = False
            new_b = b
            for mode in range(4):
                if puzzle == new_b:
                    answer += len(puzzle)
                    check[idx] = 1
                    breaker = True
                    break
                else:
                    new_b = rotate(new_b)
            if breaker: break
    return answer


solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])