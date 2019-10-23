import numpy as np
from math import log2
from functools import reduce

class ID3:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.entropy = []

    def train_test_split(self, threshold):
        return 0

    def fit(self):
        return 0

    def get_entropy(self):
        temp_x = self.X
        temp_x.append(self.Y)
        for column in temp_x:
            uniques = np.unique(column)
            column_len = len(column)
            probabilities = np.zeros(len(uniques))
            for index, unique in enumerate(uniques):
                probabilities[index] = (column == unique).sum() / column_len
            entropy = -sum(map(lambda x: x * log2(x), probabilities))
            self.entropy.append(entropy)
        return self.entropy

        




