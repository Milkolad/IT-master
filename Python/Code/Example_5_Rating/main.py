import pandas as pd 
import numpy as np 
from rating_counter import RatingCounter
from argparse import ArgumentParser

def main(path):
    df = pd.read_table(path, sep="\t")
    rg = RatingCounter(df)
    print(df)
    return 0

if __name__ == '__main__':
    parser = ArgumentParser(description='Process path to file')
    parser.add_argument('filepath', metavar='PATH', help='path for the file', type=str)
    args = parser.parse_args()
    print('\n')
    main(args.filepath)
    print('\n')