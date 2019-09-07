lst = [[1, 2, 3, 4, 5], [4, 5, 6, 7, 8, 9], [7, 8, 9, 10]]

def example0(_lst):
    result = 0
    for item in _lst:
        result += item[1]
    return result

print(example0(lst))