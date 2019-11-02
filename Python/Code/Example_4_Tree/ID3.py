from math import log2
from functools import reduce
from random import randint
from sys import maxsize
from collections import Counter

class ID3:
    def __init__(self, random_state=randint(-maxsize - 1, maxsize)):
        self.accuracy = 0
        self.random_state = random_state
        self.x_igs = []
        self.y_entropy = 0
        self.entropy = 0

    def train_test_split(self, threshold):
        return 0

    def fit(self, X, y):
        self.y_entropy = self.__entropy__(y)
        for x in X:
            self.x_igs.append(self.__IG__(x, y))
        
        return self.x_igs, self.y_entropy

    def __entropy__(self, vector):
        uniques, freqs = self.__get_freqs__(vector)
        uniques_len = len(uniques)
        column_len = len(vector)
        if uniques_len < 2:
            return 0
        elif uniques_len == 2:
            p_a = freqs[0] / column_len
            p_b = freqs[1] / column_len
            return (-(p_a * log2(p_a)) - p_b * log2(p_b))
        else:
            return -sum(map(lambda x: x * log2(x), [freqs[index] / column_len for index, unique in enumerate(uniques)]))


    def __IG__(self, vector, attributes):
        uniques, freqs = self.__get_freqs__(vector)
        weights = [freqs[index] / len(vector) for index, _ in enumerate(uniques)]
        weighted_entropies = self.y_entropy
        for index, unique in enumerate(uniques):
            weighted_entropies -= weights[index] * self.__entropy__([attributes[idx] for idx, elem in enumerate(vector) if elem == unique])
        return weighted_entropies

    def __get_freqs__(self, vector):
        counter = Counter(vector)
        return list(counter.keys()), list(counter.values())