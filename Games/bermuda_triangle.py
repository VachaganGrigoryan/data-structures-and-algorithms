import random


class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x},{self.y}'

    def __eq__(self, other):
        if not isinstance(other, Coordinate):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if not isinstance(other, Coordinate):
            return NotImplemented
        return self.x != other.x or self.y != other.y

    def to_tuple(self):
        return self.x, self.y


class Ships(list):

    def __init__(self, rx, ry, count):
        super(Ships, self).__init__()
        self.rx = rx
        self.ry = ry
        self.ship_count = count
        self.__run()

    def __run(self):
        for i in range(self.ship_count):
            while True:
                rand_cord = Coordinate(random.randint(0, self.rx), random.randint(0, self.ry))
                if all(rand_cord != cord for cord in self):
                    break
            self.append(rand_cord)

    def show(self):
        print(self)

    def __str__(self):
        return f'|{f"|{chr(10)}|".join(f"{ship}" for ship in self)}|'


class BermudaTriangle(list):

    def __init__(self, rx, ry, ship_count=4):
        super().__init__()
        self.rx = rx
        self.ry = ry
        self.extend([['+']*(self.ry+1) for _ in range(self.rx+1)])
        self.__ship = Ships(self.rx, self.ry, ship_count)

    def run(self):
        while True:
            self.show()
            self.__check(self.__rate())
            if not self.__ship:
                break
        self.__win()

    def __rate(self):
        while True:
            x, y = input(f"Enter (x, y) Coordinates, x ∋ [0, {self.rx}], y ∋ [0, {self.ry}]:\nx = "), input("y = ")
            if x.isdecimal() and y.isdecimal() and int(x) in range(self.rx+1) and int(y) in range(self.ry+1):
                break
        return Coordinate(int(x), int(y))

    def __check(self, rate):
        if any(rate == cord for cord in self.__ship):
            self[rate.x][rate.y] = '⚓'
            self.__ship.remove(rate)
        else:
            self[rate.x][rate.y] = '◽'
            self.__compass(rate)

    def __compass(self, rate):
        note = [['']*5 for _ in range(5)]
        note[2][2] = str(rate)
        for ship in self.__ship:
            if ship.x < rate.x and ship.y < rate.y:
                note[0][0], note[1][1] = "NW", "⇖"
            if ship.x == rate.x and ship.y < rate.y:
                note[0][2], note[1][2] = 'N', "⇑"
            if ship.x > rate.x and ship.y < rate.y:
                note[0][4], note[1][3] = "NE", "⇗"

            if ship.x < rate.x and ship.y == rate.y:
                note[2][0], note[2][1] = "W", "⇐"
            if ship.x > rate.x and ship.y == rate.y:
                note[2][4], note[2][3] = "E", "⇒"

            if ship.x < rate.x and ship.y > rate.y:
                note[4][0], note[3][1] = "SW", "⇙"
            if ship.x == rate.x and ship.y > rate.y:
                note[4][2], note[3][2] = "S", "⇓"
            if ship.x > rate.x and ship.y > rate.y:
                note[4][4], note[3][3] = "SE", "⇘"

        self.__show_compass(note)

    @staticmethod
    def __show_compass(note):
        print(f"\nCompass:\n _____________\n{chr(10).join('|{:<2} {:^1} {:^3} {:^1} {:>2}|'.format(*line) for line in note)}\n ‾‾‾‾‾‾‾‾‾‾‾‾‾")

    def __win(self):
        self.show()
        print("You Won")

    def show(self):
        print(self)

    def __str__(self):
        return f"\nGame Board\n{chr(10).join(' '.join(line) for line in zip(*self))}\n"


if __name__ == '__main__':

    game = BermudaTriangle(9, 9, 4)
    game.run()
