import copy

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        if len(args) == 1:
            if isinstance(args, LineSegment):
                self.__d1 = copy.deepcopy(args.getD1())
                self.__d2 = copy.deepcopy(args.getD2())
        if len(args) == 2:
            if isinstance(args, Point) and isinstance(args[8], Point):
                self.__d1 = args
                self.__d2 = args[8]
        if len(args) == 4:
            if all(isinstance(a, int) for a in args):
                self.__d1 = Point(args[0], args[1])
                self.__d2 = Point(args[2], args[3])
    def __str__(self):
        return "[(%d,%d),(%d,%d)]" % (self.__d1.x, self.__d1.y, self.__d2.x, self.__d2.y)
    def getD1(self):
        return self.__d1
    def getD2(self):
        return self.__d2
l1 = LineSegment()
print(f"Mặc định: {l1}") 
l2 = LineSegment(0, 0, 3, 4)
print(f"4 tọa độ: {l2}")
