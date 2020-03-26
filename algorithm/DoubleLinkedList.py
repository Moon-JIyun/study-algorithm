# 기존 SinglyLinkedList 의 경우 한 방향으로만 연결
# -> 삽입 또는 삭제할 때, 이전 노드를 가리키는 레퍼런스를 알아야하고, 역방향 노드 탐색이 불가함.
# 이 문제점을 보완, but 노드에 레퍼런스가 2개 필요한 것이 단점..

class DoubleLinkedList():
    class Node():
        def __init__(self,item,prev,link): #Node 생성자
            self.item = item
            self.prev = prev # 앞 노드 레퍼런스
            self.next = link # 뒤 노드 레퍼런스
    def __init__(self): # 이중 링크드 리스트 생성자
        # 두 더미 노드를 생성하는데 항목을 저장은 안함
        self.head = self.Node(None,None,None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def size(self):
        return self.size

    def isempty(self):
        return self.size == 0

    def insert_befor(self, p, item): #새 노드를 p 앞에 삽입
        t = p.prev
        n = self.Node(item, t, p)
        p.prev = n
        t.next = n
        self.size += 1

    def insert_after(self, p, item): #새 노드를 p 뒤에 삽입
        t = p.next
        n = self.Node(item, p, t)
        t.prev = n
        p.next = n
        self.size += 1

    def delete(self, x): #Node x 삭제
        # x가 참조하는 노드는 링크드 리스트에서 분리되어 가비지 컬렉션에 의해 처리됨
        f = x.prev
        r = x.next
        f.next = r # x를 건너뛰고 x의 앞뒤 노드를 연결
        r.prev = f # x를 건너뛰고 x의 앞뒤 노드를 연결
        self.size -= 1

    def print_list(self):
        if self.isempty():
            print("List is empty")
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, "<=>", end="")
                else:
                    print(p.item)
                p = p.next
