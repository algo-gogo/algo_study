
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    # 맨 뒤에 데이터 삽입
    def append_node(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = Node(data)

    # 몇번째 인덱스에 데이터 삽입
    # 만약 index가 0이면 맨 앞에 들어감
    # [3] -> [1]
    # [2] -> [3] -> [1]
    def append_index_node(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    # 데이터 조회 (모든 데이터들 조회)
    def print_all(self):
        cur = self.head
        while cur is not None:
            print('데이터: ', cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur

    # 데이터 삭제
    def delete_index(self, index):
        if index == 0:
            self.head = self.head.next
            return

        node = self.get_node(index - 1)
        node.next = node.next.next


# linkedList
# [3] -> [1] -> [2]
linkedList_0 = LinkedList(3)
linkedList_0.append_node(1)
linkedList_0.append_node(2)
linkedList_0.print_all()
print(linkedList_0.get_node(0).data)
print('----')

linkedList_0.append_index_node(1, 4)
linkedList_0.print_all()
print('----')

linkedList_0.delete_index(1)
linkedList_0.print_all()
