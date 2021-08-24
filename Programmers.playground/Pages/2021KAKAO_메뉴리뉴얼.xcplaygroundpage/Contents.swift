//: [Previous](@previous)

import Foundation

// course를 반복문을 돌면서 해당 크기에 대한 order(얘도 반복문) 조합을 구한다
// orderDict를 순회하면서 countDict 만들기
//

func solution(_ orders:[String], _ course:[Int]) -> [String] {
    var orderDict: [String : Int] = [:]
    var countDict: [Int:[(String, Int)]] = [:]
    var arrForCombination: [String] = []
    
    func combination(_ depth: Int, _ beginWith: Int, _ size: Int, _ arr: [String]) {
        if depth == size {
            let orderString = arrForCombination.reduce("", +)
            orderDict[orderString] = orderDict[orderString] == nil ? 1 : orderDict[orderString]! + 1
            return
        }
        
        for idx in beginWith..<arr.count {
            arrForCombination.append(arr[idx])
            combination(depth + 1, idx + 1, size, arr)
            arrForCombination.removeLast()
        }
    }
    
    for course_size in course {
        for order in orders {
            let sortedOrder = order.map{ String($0) }.sorted()
            combination(0, 0, course_size, sortedOrder)
        }
    }
    
    orderDict.filter{$0.value >= 2 }.forEach{
        if countDict[$0.key.count] == nil {
            countDict[$0.key.count] = [($0.key,$0.value)]
        }else {
            countDict[$0.key.count]!.append(($0.key,$0.value))
        }
    }
    
    var answer: [String] = []
    for limit in course {
        if countDict[limit] != nil {
            // count가 큰 순으로 정렬
            let list = countDict[limit]!.sorted(by: {$0.1 > $1.1})
            // list에 숫자가 젤 큰 값과 **같은 걸** filter
            answer.append(contentsOf: list.filter{list.first!.1 == $0.1}.map{$0.0})
        }
    }
    
    return answer.sorted()
    
}


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
//solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
//solution(["XYZ", "XWY", "WXA"], [2,3,4])

//: [Next](@next)
