from exponentsmoothing import exponential_smoothing
from math import floor, sqrt, isnan
import decimal
import matplotlib.pyplot as plt
import numpy as np
import os

def flooring(x):
    result = 0
    if not isnan(x):
        result = floor(decimal.Decimal(x))
    return result

def open_data(path):
    X = np.array([])
    data = np.fromfile(path)
    a = 0
    b = 200
    y = []
    for j in range(a, b):
        y.append(0.0 - flooring(data[j]))
    X.append([np.array(y)])
    return np.array(X)

def main():
    path = "./I01.dat"
    dataset = open_data(path)
    print(len(dataset))
    with plt.style.context('seaborn-white'):    
        plt.figure(figsize=(20, 8))
        for alpha in [0.3, 0.05]:
            plt.plot(exponential_smoothing(dataset.Users, alpha), label="Alpha {}".format(alpha))
        plt.plot(dataset.Users.values, "c", label = "Actual")
        plt.legend(loc="best")
        plt.axis('tight')
        plt.title("Exponential Smoothing")
        plt.grid(True)

if __name__ == "__main__":
    main()