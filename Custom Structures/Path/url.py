
class Url:

    def __init__(self, url: str):
        if not isinstance(url, str):
            raise TypeError(f"unsupported type {type(url)}")
        self.url = url

    def __truediv__(self, other):
        if not isinstance(other, (Url, str)):
            raise TypeError(f"unsupported operand type(s) for /: 'Url' and '{type(other)}'")
        return f'{self}/{other}'

    def __str__(self):
        return self.url
