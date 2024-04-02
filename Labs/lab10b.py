class Time:
    def __init__(self, _hours=0, _minutes=0, _seconds=0):
        """Initializes the time object with the given hours, minutes, and seconds. If no arguments are given, the time is set to 00:00:00."""
        self.hours = _hours
        self.minutes = _minutes
        self.seconds = _seconds

    def __repr__(self):
        """Returns a string representation of the time object."""
        return f"Class Time: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __str__(self):
        """Returns a string representation of the time object."""
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def from_str(self, time_str):
        """Sets the time object to the time represented by the given string."""
        self.hours, self.minutes, self.seconds = map(int, time_str.split(":"))

def main():
    A = Time( 12, 25, 30 )

    print(A)
    print(repr(A))
    print(str(A))
    print()

    B = Time(2, 25, 3)

    print(B)
    print(repr(B))
    print(str(B))
    print()

    C = Time(2, 25)

    print(C)
    print(repr(C))
    print(str(C))
    print()

    D = Time()

    print(D)
    print(repr(D))
    print(str(D))
    print()

    D.from_str("03:09:19")

    print(D)
    print(repr(D))
    print(str(D))


if __name__ == "__main__":
    main()
