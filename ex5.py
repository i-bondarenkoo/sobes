class Geom:
    def __init__(self, x1, x2, y1, y2):
        print("Инит базового класса")
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class Line(Geom):
    def __init__(self, x1, x2, y1, y2, fill=None):
        print("Инит класса линия")
        super().__init__(x1, x2, y1, y2)
        self.fill = fill


g = Geom(1, 2, 3, 4)
l = Line(0, 0, 0, 0)
print(g.__dict__)
print(l.__dict__)
