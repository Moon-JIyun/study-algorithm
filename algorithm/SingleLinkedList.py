# LinkedList

# #Liked List 설계
# root : 리스트 노드이고, Liked List는 노드의 주소를 가진다.
# root = Node()
# append method - 마지막 노드 뒤에 추가
# insert method - 중간에 노드 추가
# find method - Node 를 찾고 index 값 반환
# delete method - 주어진 값을 이용해 해당 노드를 찾고 지운다.

# 단방향 Linked List 구현

class SingleLinkedList():
    class Node():
        def __init__(self, item, link):
            self.item = item #항목
            self.next = link #다음 노드 참조

    def __init__(self): #단순 연결 리스트 생성자
        self.head = None
        self.size = 0

    def size(self):
        return self.size()

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item): #연결리스트 맨앞에 노드 삽입
        if self.is_empty(): #연결 리스트가 비어있는 경우
            self.head = self.Node(item, None) #해드가 새 노드 참조
        else:
            self.head = self.Node(item, self.head) # 해드가 새 노드 참조
        self.size +=1

    def insert_after(self, item, idx):
        idx.next = SingleLinkedList.Node(item,idx.next)
        self.size += 1

    def delete_front(self, idx): #idx 가 가르키는 앞 노드 삭제
        if self.is_empty():
            print('비어있습니다.')
        else:
            self.head = self.head.next #해드가 둘째 노드를 참조
            self.size -=1

    def delete_after(self, idx):
        if self.is_empty():
            print('비어있습니다.')
        else:
            t = idx.next
            idx.netx = t.next
            self.size -=1

    def search(self, target):
        idx = self.head
        for i in range(self.size):
            if target == idx.item:
                return i
            idx = idx.next

        return None

    def print_list(self):
        idx=self.head
        while idx:
            if idx.next != None:
                print(idx.item ,"->",end="")
            else:
                print(idx.item)
            idx = idx.next



