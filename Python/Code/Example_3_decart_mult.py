m1 = ['a', 'b', 'c']
m2 = [1, 2]
cp = [(x, y) for x in m1
             for y in m2
    ]
print(cp)

for c in ((x, y) for x in m1 for y in m2):
    print(c)