from math import floor, sqrt, isnan
import decimal
import matplotlib.pyplot as plt
import numpy as np
import os
from exponentsmoothing import exponential_smoothing
import time
import sys

def flooring(x):
    result = 0
    if not isnan(x):
        result = floor(decimal.Decimal(x))
    return result

def open_data(path):
    result = []

    print(f'Loading.\t')

    start_t = time.perf_counter()

    result = np.fromfile(path)

    end_t = time.perf_counter()

    print(f'Loaded.\t')
    print(f'Time has passed:\t{end_t - start_t}\t\n')
    return result

def split_data(data, start = 0, end = 0):
    Y = data[:end]
    print(f'Preparing.\t')
    print(f'Data Length:\t{len(Y)}\t')

    Y_result = []

    start_t = time.perf_counter()

    for dot in Y:
        Y_result.append(-flooring(dot))

    end_t = time.perf_counter()

    X = range(start, end)
    
    print(f'Prepared.\t')
    print(f'Time has passed:\t{end_t - start_t}\tData Length:\t{len(Y)}\t\n')
    return X, Y_result

def main():
    print(f'Start\t\n')

    path = "./I01.dat"

    start = 0
    end = 5000
    alpha = 0.05

    dataset = open_data(path)

    X, Y = split_data(dataset, start=start, end=end)

    before = plt.figure()
    plt.plot(X, Y)
    before.savefig('raw.png')

    Y_prepared = exponential_smoothing(Y, alpha)

    after = plt.figure()
    plt.plot(X, Y_prepared)
    after.savefig(f'smoothed_{alpha}.png')

    print(f'End\t\n')
    return 0
    
if __name__ == "__main__":
    main()