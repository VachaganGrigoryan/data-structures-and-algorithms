from abc import ABC, abstractmethod
from typing import Any, Iterable, Union


class AbcQueue(ABC):

    def __init__(self, limit=None) -> object:
        super(ABC, self).__init__()
        if not isinstance(limit, Union[int, None]):
            raise ValueError('Enter int value for limit')
        self.limit = limit

    @abstractmethod
    def enqueue(self, value: Any):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def is_full(self):
        pass

    @abstractmethod
    def peek(self):
        pass


class LimitError(ValueError):
    pass


class Queue(AbcQueue):

    def __init__(self, limit=None):
        super(Queue, self).__init__(limit)
        self.queue = []

    def enqueue(self, value: Any):
        if self.is_full():
            raise LimitError('The queue is full\n')
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return not bool(self.queue)

    def is_full(self):
        return len(self.queue) == self.limit

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def __str__(self):
        return f'{self.queue}'


if __name__ == '__main__':

    q = Queue(56)

    q.enqueue(5)
    q.enqueue(56)
    q.enqueue(8)
    q.enqueue(3)
    # q.enqueue(3)
    q.enqueue(35)
    print(q.peek())

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(38)
    q.enqueue(39)
    print(q.dequeue())
    print(q)

