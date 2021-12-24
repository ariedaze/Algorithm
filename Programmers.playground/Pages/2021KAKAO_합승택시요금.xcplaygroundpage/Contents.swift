import Foundation


// Floyd-Warshal 알고리즘
// O(n^3)   >> n이 1000까진 ok
// 플로이드 알고리즘을 사용해서 d[i][j] => i에서 j까지의 최저 요금을 구한다
// 그 후 루프를 돌면서 최솟값을 찾아준다. min(d[s][k] + d[k][a] + d[k][b])

// 플로이드워셜 알고리즘
//

func solution(_ n:Int, _ s:Int, _ a:Int, _ b:Int, _ fares:[[Int]]) -> Int {
    let INF =  200 * 100000
    var nodes = (0..<n).map{ _ in Array(repeating: INF, count: n) }
    
//    for i in 0..<n{
//        nodes[i][i] = 0
//    }
    
    for fare in fares {
        let v = fare[0] - 1
        let w = fare[1] - 1
        let f = fare[2]
        
        nodes[v][w] = f
        nodes[w][v] = f
    }
    
    func floydWarshal() {
        for middle in 0..<n {
            for to in 0..<n {
                if nodes[to][middle] == INF || to == middle {
                    continue
                }
                for from in 0..<n {
                    if from == to {
                        continue
                    }
                    // to>from 와 to>middle>from를 비교
                    nodes[to][from] = min(nodes[to][from], nodes[to][middle] + nodes[middle][from])
                }
            }
        }
    }
    floydWarshal()
    
    var cost = nodes[s-1][a-1] + nodes[s-1][b-1]
    
    for i in 0..<n {
        // s > i 에서  i > a 와 i > b 비교
        let start = nodes[s-1][i]
        let a = a-1 == i ? 0 : nodes[i][a-1]
        let b = b-1 == i ? 0 : nodes[i][b-1]
        cost = min(cost, start+a+b)

    }
    
    return cost
}


solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])

solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])

solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])

