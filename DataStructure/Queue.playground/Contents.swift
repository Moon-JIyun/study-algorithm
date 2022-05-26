// dequeue 시, O(n) 의 복잡도로 인해, 오버헤드가 발생할 수 있음
struct Queue1<T> {
    private var queue: [T] = []
    
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
        return isEmpty ? nil : queue.removeFirst()
    }
}

// dequeue 의 오버헤드를 줄이고자, 삭제가 아닌 첫번째 head 만 변경하여 시간 복잡도를 O(1) 로 개선할 수 있음.

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


