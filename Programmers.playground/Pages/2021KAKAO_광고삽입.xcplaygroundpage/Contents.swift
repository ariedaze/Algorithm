//: [Previous](@previous)

import Foundation

// 1. 시각을 초로 환산한다.
// 2. total_time 배열을 정의한다
//      total_time[x] = 재생 - 종료
// tota

func solution(_ play_time:String, _ adv_time:String, _ logs:[String]) -> String {
    let playTime: Int = makeSeconds(time: play_time)
    var playTimeList: [Int] = Array(repeating: 0, count: playTime + 1)
    let advTime: Int = makeSeconds(time: adv_time)

    for log in logs {
        let playLog: [String] = log.components(separatedBy: "-")
        let start: Int = makeSeconds(time: playLog[0])
        let end: Int = makeSeconds(time: playLog[1])
        playTimeList[start] += 1
        playTimeList[end] -= 1
    }
    
    // 구간별시청자수
    for i in 1...playTime { // 종료 시점은 포함 x
        playTimeList[i] += playTimeList[i-1]
    }
    //구간별누적시청자수
    for i in 1...playTime {
        playTimeList[i] += playTimeList[i-1]
    }
    
    var startTime = 0
    var maxTime = 0
    
    for i in (advTime-1)..<playTime {
        if i >= advTime {
            let view = playTimeList[i] - playTimeList[i - advTime]
            if maxTime < view {
                maxTime = view
                startTime = i - advTime + 1
            }
        } else {
            if maxTime < playTimeList[i] {
                maxTime = playTimeList[i]
                startTime = i - advTime + 1
            }
        }

    }
    return makeString(seconds: startTime)
}

func makeSeconds(time: String) -> Int {
    let timeArray = time.components(separatedBy: ":")
    guard let hour = Int(timeArray[0]) else { return 0 }
    guard let minute = Int(timeArray[1]) else { return 0 }
    guard let second = Int(timeArray[2]) else { return 0 }
    return hour * 3600 + minute * 60 + second
}

func makeString(seconds: Int) -> String {
    let hourString = 0...9 ~= seconds/3600 ? "0\(seconds/3600)" : "\(seconds/3600)"
    let minuteString = 0...9 ~= seconds/60%60 ? "0\(seconds/60%60)" : "\(seconds/60%60)"
    let secondString = 0...9 ~= seconds%60 ? "0\(seconds%60)" : "\(seconds%60)"

    return "\(hourString):\(minuteString):\(secondString)"
}

solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])


solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])

//: [Next](@next)
