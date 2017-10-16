class Rectangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def square(self):
        return self.side1 * self.side2

    def perimeter(self):
        return self.side1 + self.side2


if __name__ == "__main__":
    rec = Rectangle(2,4)
    print(rec.square())
    print(rec.perimeter())
