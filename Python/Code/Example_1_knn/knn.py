import math

class Knn:
    def __init__(self, trainData, testData, k, numberOfClasses):
        self.trainData = trainData
        self.testData = testData
        self.k = k
        self.numberOfClasses = numberOfClasses

    def compute(self, station):
        result = 0
        return result