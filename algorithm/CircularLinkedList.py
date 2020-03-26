class EmptyError(Exception):
    pass


class CircularLinkedList():
    class Node():
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.last = None
        self.size = 0

    def no_items(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert(self, item): # 새 항목을 연결 리스트의 첫 노드로 삽입
        n = self.Node(item, None) # 새 항목을 저장할 노드를 생성하여 n 이 참조
        if self.is_empty(): # 연결 리스트가 empty 인 경우
            n.next = n # 새 노드는 자신을 참조
            self.last = n  # last는 새 노드를 참조
        else :
            n.next = self.last.next #새 노드는 첫 노드를 참조
            self.last.next = n # last가 참조하는 노드와 새 노드 연결
            self.size += 1

    def first(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        f = self.last.next
        return f.item

    def delete(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        x= self.last.next
        if self.size == 1 :
            self.last = None
        else:
            self.last.next = x.next
        self.size -= 1
        return x.item

    def print_list(self):
        if self.is_empty():
            print('List is empty')
        else:
            f = self.last.next
            p = f
            while p.next != f:
                print(p.item, "->", end ='')
                p = p.next
            print(p.item)



