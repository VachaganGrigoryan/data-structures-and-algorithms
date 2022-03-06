

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.root = None

    def add(self, value):
        cursor = self.root
        if cursor is None:
            self.root = Node(value)
            return

        while cursor.next:
            cursor = cursor.next
        cursor.next = Node(value)

    def __iter__(self):
        cursor = self.root
        while cursor.next:
            yield cursor.value
            cursor = cursor.next
        yield cursor.value


if __name__ == '__main__':

    ll = LinkedList()

    ll.add(5)
    ll.add(56)
    ll.add(58)

    for v in ll:
        print(v)
