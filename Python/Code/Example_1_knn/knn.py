import math
import pandas as pd

def metric(station1, station2):
    return math.fabs(station1['Order'] - station2['Order'])

def indexer(data, indexies):
    result = pd.DataFrame({'Name' : [], 'Type' : []})
    
    return result

def compute(data, scored_data, station):
    result = 0
    return result