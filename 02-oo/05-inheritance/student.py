class Position:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def move(self, dx, dy):
        """
        Returns a new Position object that has been moved horizontally by dx
        and vertically by dy.
        """
        return Position(self.x + dx, self.y + dy)
