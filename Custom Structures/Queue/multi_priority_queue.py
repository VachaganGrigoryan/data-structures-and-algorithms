from typing import Any, Dict

from queue import AbcQueue, Queue, LimitError


class MultiPriorityQueue(AbcQueue):

    def __init__(self, limit=None):
        super(MultiPriorityQueue, self).__init__(limit)
        self._len = 0
        self.priorities = []
        self.queues: Dict[Any, Queue] = dict()

    def enqueue(self, value: Any, priority=0):
        if self.is_full():
            raise LimitError('The queue is full\n')

        queue = self.queues.get(priority)
        if not queue:
            queue = Queue()
            self.queues[priority] = queue
            self.priorities = sorted(self.queues.keys(), reverse=True)
        self._len += 1
        queue.enqueue(value)

    def dequeue(self):
        if self.is_empty():
            return None

        priority = self.priorities[-1]
        queue: Queue = self.queues.get(priority)
        elm = queue.dequeue()

        if queue.peek() is None:
            self.priorities.pop()
            del self.queues[priority]

        self._len -= 1
        return elm

    def is_empty(self):
        return len(self.priorities) == 0

    def is_full(self):
        return self._len == self.limit

    def peek(self):
        if self.is_empty():
            return None

        priority = self.priorities[-1]
        queue: Queue = self.queues.get(priority)
        return queue.peek()

    def __str__(self):
        return f'{self.queues}'


if __name__ == '__main__':

    q = MultiPriorityQueue(22)

    q.enqueue(5)
    q.enqueue(55, 9)
    q.enqueue(5, 1)
    q.enqueue(6, 1)
    q.enqueue(5)
    q.enqueue(55, 9)
    q.enqueue(5, 1)
    q.enqueue(6, 1)

    print(q.priorities)
    print(q.queues)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    print(q.peek())
