import math

class Vector:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def magnitude(self):
        return round(math.sqrt(self.x**2 + self.y**2), 2)

    def unit(self):
        if self.x == 0 and self.y == 0:
            raise ValueError("Cannot convert zero vector to a unit vector")
        mag = self.magnitude()
        self.x /= mag
        self.y /= mag
        return None

    def __str__(self):
        return f"({self.x:.02f}, {self.y:.02f})"

    def __repr__(self):
        return f"({self.x:.02f}, {self.y:.02f})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) == Vector:
            return self.x * other.x + self.y * other.y
        elif type(other) == int or type(other) == float:
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("Invalid type for multiplication")

    def __rmul__(self, other):
        return self.__mul__(other)


def main():
    zero = Vector()
    right = Vector(1, 0)
    up = Vector(0, 1)
    left2 = Vector(-2, 0)
    arb1 = Vector(5, 5)
    arb2 = Vector(-18.67, 6)

    vectors = [zero, right, up, left2, arb1, arb2]
    names = ["zero", "right", "up", "left2", "arb1", "arb2"]

    print(f"zero:{zero}, right:{right}, up:{up}, left2: {left2}, arb1: {arb1}, arb2: {arb2}")
    print("\nMagnitudes:")
    for name, vector in zip(names, vectors):
        print(f"{name}:{vector.magnitude()}", end=", ")
    print()

    new = Vector(1, 1)
    print("New:", new)
    new.unit()
    print("New:", new)

    up_arb1 = up * arb1
    print(f"up * arb1: {up_arb1:.01f}")

    check_add = up + right == Vector(1, 1)
    print("up + right == Vector(1,1):", check_add)

    print(Vector(3.55, 3.55))
    print(arb1)

    new_five = 5 * new
    print("5*new == arb1:", new_five == arb1)

    print("arb1 == arb2:", arb1 == arb2)

    try:
        zero.unit()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()