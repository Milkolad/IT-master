class MyClass:
    def __init__(self, x):
        self.x = x
        print(f"MyClass id = {id(self)}")

my_object = MyClass(10)*10
print(f"{my_object.x}")