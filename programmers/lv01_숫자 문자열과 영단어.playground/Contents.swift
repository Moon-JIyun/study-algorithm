import UIKit

func solution(_ s: String) -> Int {

    let stringNum = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    let num = ["0","1","2","3","4","5","6","7","8","9"]
    
    let split = s.map{ (String($0))}
    
    var result: [String] = []
    var resultInt: Int
    var temp: String = ""
    for s in split {
        if num.contains(s){
            result.append(s)
        } else {
            temp += s
//            print(temp)
            if stringNum.contains(temp) {
                result.append(num[stringNum.firstIndex(of: temp)!])
                temp = ""
            }
        }
    }
    resultInt = Int(result.joined())!
    
    
    return resultInt
}

solution("one4seveneight")
