def solution(rows, columns, queries):
    answer = []
    board = [[j+1 + (i*columns) for j in range(columns)] for i in range(rows)]
    global min_answer
    for x1, y1, x2, y2 in queries:
        min_answer = board[x1-1][y1-1]
        rotate(x1-1, y1-1, x1-1, y1-1, x2-1, y2-1, 0, board[x1-1][y1-1], board)
        answer.append(min_answer)
    return answer

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상

def rotate(x, y, x1, y1, x2, y2, mode, temp, board):
    global min_answer
    if mode > 3: return
    dx, dy = dirs[mode]
    newx, newy = x + dx, y + dy
    if x1 <= newx <= x2 and y1 <= newy <= y2:
        board[newx][newy], temp = temp, board[newx][newy]
        min_answer = min(min_answer, temp)
        rotate(newx, newy, x1, y1, x2, y2, mode, temp, board)
    else:
        rotate(x, y, x1, y1, x2, y2, mode+1, temp, board)
    
