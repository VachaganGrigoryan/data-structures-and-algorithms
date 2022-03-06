from typing import Any
from queue import AbcQueue, LimitError


class Node:

    def __init__(self, _value_: Any):
        self._next_ = None
        self._value_ = _value_

    @property
    def value(self) -> Any:
        return self._value_

    @property
    def next(self) -> 'Node':
        return self._next_

    @next.setter
    def next(self, node):
        self._next_ = node

    def __str__(self):
        return str(self.value)


class LinkedQueue(AbcQueue):

    def __init__(self, limit=None):
        super(LinkedQueue, self).__init__(limit)
        self._len = 0
        self.front: Node = None
        self.rear: Node = None

    def enqueue(self, value: Any):
        if isinstance(self.limit, int) and len(self) > self.limit:
            raise LimitError('The QueueLinkedList is full\n')

        node = Node(value)
        last = self.rear
        self.rear = node
        self._len += 1

        if self.front is None:
            self.front = node
            return
        last.next = self.rear

    def dequeue(self):
        if self.front is None:
            return None
        first, self.front = self.front, self.front.next
        self._len -= 1
        return first.value

    def is_empty(self):
        return self._len == 0

    def is_full(self):
        return self._len == self.limit

    def peek(self):
        return self.front.value

    def __len__(self):
        return self._len

    def __iter__(self):
        elm = self.front
        while elm.next:
            yield elm.value
            elm = elm.next
        yield elm.value
