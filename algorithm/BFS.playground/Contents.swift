// Node 구현

class Node<T> {
    let value: T
    var edges = [Edge<T>]()
    var visited = false
    
    init(value: T) {
        self.value = value
    }
    
    func appendEdgeTo(_ node: Node<T>) {
        let edge = Edge<T>(from: self, to: node)
        self.edges.append(edge)
    }
}

// Edge
class Edge<T> {
    weak var source: Node<T>?
    let destination: Node<T>
    
    init(from source: Node<T>, to destination: Node<T>) {
        self.source = source
        self.destination = destination
    }
}

// Queue
struct Queue<T> {
    private var queue: [T?] = []
    private var head: Int = 0
    
    public var count: Int {
        return queue.count
    }
    
    public var isEmpty: Bool {
        return queue.isEmpty
    }
    
    public mutating func enqueue(_ element: T) {
        queue.append(element)
    }
    
    public mutating func dequeue() -> T? {
        guard head <= queue.count, let element = queue[head] else { return nil }
        // 맨 앞 원소를 nil 로 변경해줌.
        queue[head] = nil
        head += 1
        
        // 배열의 길이가 계속해서 길어질 수 있으니, 일정 조건에서
        if head > queue.count / 4 {
            queue.removeFirst(head)
            head = 0
        }
        return element
    }
}




// BFS 구현

func BFS(n: Int, edges: [(Int, Int)]) {
    // Node, Edge setup
    let nodes = (0..<n).map({ Node<Int>(value: $0 + 1) })
    for (from, to) in edges {
        nodes[from - 1].appendEdgeTo(nodes[to - 1])
    }
    
    // 1. 궁극적으로 원하는 값
    var shortest = Array(repeating: [1], count: n)
    
    var queue = Queue<Node<Int>>()
    queue.enqueue(nodes[0])
    nodes[0].visited = true
    
    while let node = queue.dequeue() {
        for edge in node.edges {
            let dest = edge.destination
            guard dest.visited == false else { continue }
            queue.enqueue(dest)
            dest.visited = true
            // 2. Node를 방문할 때 해야하는 처리
            shortest[dest.value - 1] = shortest[node.value - 1] + [dest.value]
        }
    }
    
    print(shortest)
}

BFS(n: 6, edges: [(1,5), (2,4), (2,5), (3,2), (3,6), (4,2), (4,5), (5,3), (5,6)])



// Dictionary 로 그래프 구현 후, BFS
let graphSample = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]




func bfs (graph: [String: [String]], start: String) -> [String] {
    var visitedQueue: [String] = []
    var needVisitQueue = Queue<String>()
    
    needVisitQueue.enqueue(start)
    
    while !needVisitQueue.isEmpty {
        guard let a = needVisitQueue.dequeue() else { return [] }
        if visitedQueue.contains(a) { continue }
        
        visitedQueue.append(a)
        graph[a]?.forEach { needVisitQueue.enqueue($0)}
    }
    
    return visitedQueue
}
