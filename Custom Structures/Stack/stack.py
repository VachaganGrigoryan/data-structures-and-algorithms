from abc import ABC, abstractmethod
from typing import Any, Iterable


class AbcStack(ABC):

    def __init__(self, data: Iterable = None) -> object:
        super(ABC, self).__init__()
        self._data = list(data or [])

    @abstractmethod
    def push(self, elem: Any):
        pass

    @abstractmethod
    def pop(self):
        pass


class Stack(AbcStack):

    def __repr__(self):
        return f'Stack<{self._data}>'

    def __str__(self):
        return f'Stack<{self._data}>'

    def __len__(self):
        return len(self._data)

    def __contains__(self, elem: Any):
        return elem in self._data

    def __add__(self, other):
        if not isinstance(other, Stack):
            raise TypeError(
                f"Only supported two Stack type instances. Actual cant do (<class 'Stack'> + {type(other)})")
        return self._data + other._data

    def copy(self):
        return Stack(self._data)

    def push(self, elem: Any):
        self._data.append(elem)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty Stack")
        return self._data.pop()


if __name__ == '__main__':
    stack = Stack()
    stack.push("Str")
    stack.push("Str")
    stack.push([4, 5])

    copy_stack = stack.copy()
    copy_stack.push(5)

    print(stack)
    print(copy_stack)
