# q1
class Example:
    def __init__(self, v1=0, v2=0):
        self._v1 = v1
        self._v2 = v2

    def __str__(self):
        return f"Value 1: {self._v1}, Value 2: {self._v2}"

    def __add__(self, other):
        new_v1 = self._v1 + other._v1
        new_v2 = self._v2 + other._v2
        return Example(new_v1, new_v2)

# q2
class Example:
    def __init__(self, obj):
        self._obj = obj

    def __sub__(self, other):
        return abs(len(self._obj) - len(other._obj))

    def __gt__(self, other):
        return len(self._obj) > len(other._obj)
