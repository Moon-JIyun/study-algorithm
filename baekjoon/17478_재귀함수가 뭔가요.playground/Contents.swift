import UIKit

let inputNum = readLine().map{Int($0)!}

func recursive(_ n: Int, inputNum: Int ) {
    
    let dash = String(repeating: "____", count: n)

    
    print("\(dash)\"재귀함수가 뭔가요?\"")
    
    if n == inputNum {
        print("\(dash)\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print("\(dash)라고 답변하였지.")
        return
    }
    print("\(dash)\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
    print("\(dash)마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print("\(dash)그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    recursive(n+1, inputNum: inputNum)
    print("\(dash)라고 답변하였지.")
}

recursive(0, inputNum: 4)




