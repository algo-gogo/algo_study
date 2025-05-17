class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # 끝에서 k번째 값을 구하기
    # def get_kth_node_from_last(self, k):
    #     cur_index = 0
    #     cur = self.head
    #     node_list = []
    #     while cur is not None:
    #         node_list.append(cur.data)
    #         cur = cur.next
    #         cur_index += 1
    #
    #     print(node_list)
    #     print(k)
    #     return node_list[-k]

    def get_kth_node_from_last(self, k):
        cur_index = 0
        cur = self.head
        node_list = []
        while cur is not None:
            node_list.append(cur)
            cur = cur.next
            cur_index += 1

        print(node_list)
        print(k)
        return node_list[-k]


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)