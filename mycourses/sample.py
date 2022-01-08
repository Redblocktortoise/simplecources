


class Circle:
    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return 3.1415 * self.r**2

c = Circle(10)
print(c.area)

