class MyClass:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x

o1 = MyClass(10)
o2 = MyClass(10)
print(o1 == o2)