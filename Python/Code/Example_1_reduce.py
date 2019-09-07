from functools import reduce

lst = [[1, 2, 3, 4, 5], [4, 5, 6, 7, 8, 9], [7, 8, 9, 10]]

print(reduce(lambda x, y: x + y[1], lst, 0))