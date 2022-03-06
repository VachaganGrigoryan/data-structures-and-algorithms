

class Deque:

    def __init__(self):
        self.deque = []

    def is_empty(self):
        return bool(self.deque)

    def is_full(self):
        pass

    def add_in_front(self, value):
        self.deque.insert(0, value)

    def add_in_back(self, value):
        self.deque.append(value)

    def get_from_front(self):
        return self.deque.pop(0)

    def get_from_back(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)


if __name__ == '__main__':
    d = Deque()

    d.add_in_back(5)
    d.add_in_back(46)
    d.add_in_front(45)

    print(d.get_from_back())
    print(d.get_from_front())
