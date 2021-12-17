class vector:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def _add_(self, other):
        return vector(self.x + other.x, self.y + other.y)

    def _eq_(self, other):
        return self.x == other.x and self.y == other.y

    def _str_(self):
        return f"<Vector x:(self.x), y:(self.y)>"

    def _repr_(self):
        return str(self)