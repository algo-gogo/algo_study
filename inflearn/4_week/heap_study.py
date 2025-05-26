class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        value_index = len(self.items) - 1
        while value_index > 1:
            if value > self.items[value_index // 2]:
                self.items[value_index // 2], self.items[value_index] = self.items[value_index], self.items[value_index // 2]
                value_index = value_index // 2
            else:
                break

    def delete(self):
        n = len(self.items)
        self.items[1], self.items[n - 1] = self.items[n - 1], self.items[1]
        # 원소 삭제
        self.items.pop()

        n = len(self.items)

        value_index = 1
        # 이진트리 만들자
        while value_index * 2 <= n - 1:
            left_child_index = 2 * value_index
            right_child_index = 2 * value_index + 1
            if self.items[value_index] < self.items[left_child_index] and self.items[value_index] < self.items[right_child_index]:
                self.items[value_index], self.items[right_child_index] = self.items[right_child_index], self.items[value_index]
                value_index = right_child_index
            elif self.items[value_index] < self.items[left_child_index]:
                self.items[value_index], self.items[left_child_index] = self.items[left_child_index], self.items[value_index]
                value_index = left_child_index
            elif self.items[value_index] < self.items[right_child_index]:
                self.items[value_index], self.items[right_child_index] = self.items[right_child_index], self.items[value_index]
                value_index = right_child_index
            else:
                break






max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]