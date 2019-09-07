import numpy as np

lst = [[1, 2, 3, 4, 5], [4, 5, 6, 7, 8, 9], [7, 8, 9, 10]]

print(np.sum(x[1] for x in lst))