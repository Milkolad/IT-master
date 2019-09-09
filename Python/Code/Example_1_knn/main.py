import pandas as pd
import numpy as np
import math


def metric(station1, station2):
    return math.fabs(station1['Order'] - station2['Order'])

def main():
    metro_df = pd.read_csv("list_of_moscow_metro_stations.csv")
    station1 = metro_df.loc[0, :]
    station2 = metro_df.loc[3, :]
    print(station1['Name'])
    print(station2['Name'])
    print(metric(station1, station2))

    
if __name__ == "__main__":
    main()