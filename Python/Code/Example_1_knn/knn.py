import math
import numpy as np

class KNeighborsClassifier:
    def __init__(self, n_neighbors=5, leaf_size=30, p=2, metric=None):
        self.n_neighbors = n_neighbors
        self.metric = metric
        self.leaf_size = leaf_size
        self.p = p

    def fit(self, X, y):
        return 0