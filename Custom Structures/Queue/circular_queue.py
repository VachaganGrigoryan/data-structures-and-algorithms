from typing import Any

from queue import AbcQueue, LimitError


class CircularQueue(AbcQueue):

    def __init__(self, limit):
        super(CircularQueue, self).__init__(limit=limit)
        self.front = -1
        self.rear = -1

        self.queue = [None] * limit

    def enqueue(self, value: Any):
        if self.is_full():
            raise LimitError('The queue is full\n')

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.limit
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            return None

        elm = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
            return elm

        self.front = (self.front + 1) % self.limit
        return elm

    def is_empty(self):
        return (self.front + 1) % self.limit == self.rear

    def is_full(self):
        return (self.rear + 1) % self.limit == self.front

    def peek(self):
        return self.queue[self.front]