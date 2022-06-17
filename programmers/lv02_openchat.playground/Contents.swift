import Foundation

func solution(_ record:[String]) -> [String] {
    
    var userDict: [String: String] = [:]
    var result: [String] = []
    var split: [[String]] = []
    
    
    for user in record {
        split.append( user.split(separator: " ").map{(String($0))})
        
    }
    for info in split {
        if info[0] == "Enter" || info[0] == "Change" {
            userDict[info[1]] = info[2]
        }
    }
    for info in split {
        switch info[0] {
            case "Enter":
            let enterMsg: String = "\(userDict[info[1]]!)님이 들어왔습니다."
            result.append(enterMsg)
            print(result)
            case "Leave":
            let leaveMsg: String = "\(userDict[info[1]]!)님이 나갔습니다."
            result.append(leaveMsg)
            print(result)
            
            default:
            break
            
        }
    }
   

    return result
}

let record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

solution(record)
