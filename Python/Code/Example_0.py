lst = [[1, 2, 3, 4, 5], [4, 5, 6, 7, 8, 9], [7, 8, 9, 10]]

def example0(_lst):
    result = 0
    for i in range(len(_lst)):
        result += _lst[i][1]
    return result

print(example0(lst))