from math import floor, sqrt, isnan
import decimal
import matplotlib.pyplot as plt
import numpy as np
import os
from exponentsmoothing import exponential_smoothing
import time

def flooring(x):
    result = 0
    if not isnan(x):
        result = floor(decimal.Decimal(x))
    return result

def open_data(path):
    result = []

    print(f'Data is loading.')

    start = time.perf_counter()

    result = np.fromfile(path)

    end = time.perf_counter()

    print(f'Data loaded.\tTime has passed:\t{end - start}')
    return result

def split_data(data, start = 0, end = 0):
    Y = data[:end]
    print(f'Data is starting to preparing.\tLength of data:\t{len(Y)}')

    Y_result = []

    start_t = time.perf_counter()

    for dot in Y:
        Y_result.append(-flooring(dot))

    end_t = time.perf_counter()

    X = range(start, end)
    
    print(f'Data is prepared.\tTime has passed:\t{end_t - start_t}\tLoaded dots:\t{len(Y)}')
    return X, Y_result

def main():
    print('Start')

    path = "./I01.dat"

    start = 0
    end = 200

    dataset = open_data(path)

    X, Y = split_data(dataset, start=start, end=end)

    before = plt.figure()
    plt.plot(X, Y)
    before.savefig('before.png')

    Y_prepared = exponential_smoothing(Y, 0.3)

    after = plt.figure()
    plt.plot(X, Y_prepared)
    after.savefig('after.png')

    print('End')
    return 0
    
if __name__ == "__main__":
    main()