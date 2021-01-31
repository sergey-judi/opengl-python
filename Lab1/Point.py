class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if type(other) is int or type(other) is float:
            return Point(self.x + other, self.y + other)
        else:
            return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__add__(-other)
        # the logic above is equal to logic below
        # if type(other) is int or type(other) is float:
        #     return Point(self.x - other, self.y - other)
        # else:
        #     return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        # overriding a string method
        # used at the beginning of the development
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def offset_x(self, offset_x):
        return Point(self.x + offset_x, self.y)

    def offset_y(self, offset_y):
        return Point(self.x, self.y + offset_y)

    def coordinates(self):
        return [self.x, self.y]
