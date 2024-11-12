#A
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y

    def length(self, p):
        return round(((self.x - p.x)**2 + (self.y - p.y)**2)**0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if not args:
            self.x, self.y = 0, 0
        elif len(args) == 1:
            self.x, self.y = args[0]
        else:
            self.x, self.y = args  


#B
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y

    def length(self, p):
        return round(((self.x - p.x)**2 + (self.y - p.y)**2)**0.5, 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        if not args:
            self.x, self.y = 0, 0
        elif len(args) == 1:
            self.x, self.y = args[0]
        else:
            self.x, self.y = args

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"


#C
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y

    def length(self, p):
        return round(((self.x - p.x)**2 + (self.y - p.y)**2)**0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if not args:
            self.x, self.y = 0, 0
        elif len(args) == 1:
            self.x, self.y = args[0]
        else:
            self.x, self.y = args

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"

    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])

    def __iadd__(self, other):
        self.move(other[0], other[1])
        return self


#D
class Fraction:

    def __simp(self, coords):
        a, b = coords[0], coords[1]
        while b:
            a, b = b, a % b
        return coords[0] // a, coords[1] // a

    def __init__(self, *args):
        if isinstance(args[0], str):
            self.n, self.d = self.__simp(tuple(map(int, args[0].split('/'))))
        else:
            self.n, self.d = self.__simp(args)

    def numerator(self, number=0):
        if number:
            self.n, self.d = self.__simp((number, self.d))
        return self.n

    def denominator(self, number=0):
        if number:
            self.n, self.d = self.__simp((self.n, number))
        return self.d

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __repr__(self):
        return f"Fraction({self.n}, {self.d})"


#E
class Fraction:

    def __simp(self, coords):
        a, b = coords[0], coords[1]
        while b:
            a, b = b, a % b
        return coords[0] // a, coords[1] // a

    def __init__(self, *args):
        if isinstance(args[0], str):
            self.n, self.d = self.__simp(tuple(map(int, args[0].split('/'))))
        else:
            self.n, self.d = self.__simp(args)

    def numerator(self, number=0):
        if number:
            if self.n > 0:
                self.n, self.d = self.__simp((abs(number), self.d))
                self.n = -self.n if number < 0 else self.n
            elif self.n < 0:
                self.n, self.d = self.__simp((abs(number), self.d))
                self.n = -self.n if number > 0 else self.n
        return abs(self.n)

    def denominator(self, number=0):
        if number:
            if self.n > 0:
                self.n, self.d = self.__simp((self.n, abs(number)))
                self.n = -self.n if number < 0 else self.n
            elif self.n < 0:
                self.n, self.d = self.__simp((abs(self.n), abs(number)))
                self.n = -self.n if number > 0 else self.n
        return self.d

    def __neg__(self):
        return Fraction(-self.n, self.d)

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __repr__(self):
        return f"Fraction('{self.n}/{self.d}')"