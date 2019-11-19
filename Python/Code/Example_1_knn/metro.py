import pandas as pd
import numpy as np
import ast

def parse_to_dict(array):
    array[-1] = ast.literal_eval(array[-1])
    return array


class Metro:
    def __init__(self, filepath):
        df = pd.read_csv(filepath, sep='\t', error_bad_lines=False)
        self.raw_data = np.apply_along_axis(parse_to_dict, 1, df.to_numpy())
        self.adj_matrix = pd.DataFrame(np.zeros(shape=(self.raw_data.shape[0], self.raw_data.shape[0])), \
            columns=df['LineOrder'] + '|' + df['Name'], \
            index=df['LineOrder'] + '|' + df['Name'])
    
    def __metric__(self, st_from, st_to):
        if st_from['LineOrder'] == st_to['LineOrder']:
            return 0

    
    def print(self):
        print(self.raw_data)
        print(self.adj_matrix)

    