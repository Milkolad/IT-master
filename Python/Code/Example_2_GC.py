class MyClass:
    def __del__(self):
        print(f"Я буду удален {id(self)}")

o = MyClass()
print(id(0))
del o
print(id(o))