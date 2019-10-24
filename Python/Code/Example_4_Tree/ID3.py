import numpy as np
from math import log2
from functools import reduce
from random import randint
from sys import maxsize

class ID3:
    def __init__(self, random_state=randint(-maxsize - 1, maxsize)):
        self.accuracy = 0
        self.random_state = random_state
        self.x_entropy = []
        self.y_entropy = 0

    def train_test_split(self, threshold):
        return 0

    def fit(self, X, y):
        for x in X:
            self.x_entropy.append(self.__entropy__(x))
        self.y_entropy = self.__entropy__(y)
        return self.x_entropy, self.y_entropy

    def __entropy__(self, vector):
        uniques = np.unique(vector)
        column_len = len(vector)
        probabilities = np.zeros(len(uniques))
        for index, unique in enumerate(uniques):
            probabilities[index] = (vector == unique).sum() / column_len
        entropy = -sum(map(lambda x: x * log2(x), probabilities))
        return entropy