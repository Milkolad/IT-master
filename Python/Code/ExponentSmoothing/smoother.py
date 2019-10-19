import numpy as np
import time
import matplotlib
matplotlib.rcParams['agg.path.chunksize'] = 10000
import matplotlib.pyplot as plt
from math import floor, sqrt, isnan
import decimal

class Smoother:
    def __init__(self, path, start=None, end=None, alpha=None):
        print(f'Loading and preparing.\t')

        start_t = time.perf_counter()
        self._y = [-floor(decimal.Decimal(x)) for x in np.fromfile(path) if not isnan(x)]
        end_t = time.perf_counter()

        print(f'Loaded and prepared.\t')
        print(f'Time has passed:\t{end_t - start_t}\t\n')

        self._start = self.__isNoneStart(start)
        self._end = self.__isNoneEnd(end)
        self._alpha = self.__isNoneAlpha(alpha)

    '''
        Plot.

        Method for plotting data.

        args: 
            isRaw (False for raw, True for smoother)
            alpha (None for 0.05, another for exact value)
            start (None for 0, another for exact value)
            end (None for length of data, another for exact value)
    '''
    
    def plot(self, isRaw=False, alpha=None, start=None, end=None):
        result = plt.figure()
        self._alpha = self.__isNoneAlpha(alpha)
        self._start = self.__isNoneStart(start)
        self._end = self.__isNoneEnd(end)
        if isRaw:
            plt.plot(self.__generateX(), self._y)
        else:
            plt.plot(self.__generateX(), self.__exponential_smoothing())
        return result

    '''
        Private methods.

        This methods uses only for initializing, preparing and transforming data.
    '''

    def __exponential_smoothing(self):
        result = [self._y[self._start]]
        for index, x in enumerate(self._y[self._start + 1:self._end]):
            result.append(self._alpha * x + (1 - self._alpha) * result[index - 1])
        return result

    def __isNoneAlpha(self, alpha):
        if alpha is None:
            return 0.05
        else:
            return alpha
    
    def __isNoneStart(self, start):
        if start is None:
            return 0
        else:
            return start

    def __isNoneEnd(self, end):
        if end is None:
            return len(self._y)
        else:
            return end

    def __generateX(self):
        return range(self._start, self._end)
