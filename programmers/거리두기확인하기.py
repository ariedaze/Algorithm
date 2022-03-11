def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer

 
udlr = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 상하좌우
manhattan = [(1, 1), (-1, 1), (1, -1), (-1, -1), (2, 0), (-2, 0), (0, 2), (0, -2)] # 거리 2

# 맨해튼 거리 2이하 안됨 |r1 - r2| + |c1 - c2|
# 파티션이면 2여도 오케이
# P(사람) 0(빈테이블) X(파티션)
def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] != "P": continue
            
            for dx, dy in udlr: # 상하좌우가 P라면 0
                x, y = i + dx, j + dy
                if 0<= x < 5 and 0 <= y < 5 and place[x][y] == "P":
                    return 0
                
            for dx, dy in manhattan: # 거리 2인 경우 파티션 체크
                x, y = i + dx, j + dy
                if x < 0 or x >= 5 or y < 0 or y >= 5 or place[x][y] != "P":
                    continue
                    
                if dx and dy: # 대각선인 경우 (1, 1), (-1, 1), (1, -1), (-1, -1)
                    # 1. dx만 증가
                    if place[x][j] != "X": return 0
                    # 2. dy만 증가
                    if place[i][y] != "X": return 0
                    
                elif dx: # dx != 0, 상하2
                    nx = i + int(dx/2)
                    if 0<= nx < 5 and place[nx][y] != "X": # 빈테이블 거르기
                        return 0
                    
                elif dy: # dx != 0, 좌우2
                    ny = j + int(dy/2)
                    if 0<= ny < 5 and place[x][ny] != "X": # 빈테이블 거르기
                        return 0
            
    return 1 # 거리두기 지키면 1 아니면 0
