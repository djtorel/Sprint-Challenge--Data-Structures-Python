from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            self.current.value = item
            self.current = self.storage.head if self.current == self.storage.tail else self.current.next

    def get_recursive(self, curr, arr):
        if curr is None:
            return arr
        else:
            return self.get_recursive(curr.next, [*arr, curr.value])

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return self.get_recursive(self.storage.head, list_buffer_contents)


foo = RingBuffer(3)
foo.append(1)
foo.append(2)
foo.append(3)
print(foo.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
