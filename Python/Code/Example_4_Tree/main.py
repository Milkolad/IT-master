import pandas as pd
from argparse import ArgumentParser
from ID3 import ID3

def main(path, predict_column):
    df = pd.read_csv(path)
    columns = df.columns.values
    X = [df[column].values for column in columns if column != predict_column]
    Y = df[predict_column].values
    print(X)
    print(Y)

    descisions = ID3(X, Y)
    print(descisions.get_entropy())
    return 0

if __name__ == '__main__':
    parser = ArgumentParser(description='Process path to file')
    parser.add_argument('filepath', metavar='PATH', help='path for the file', type=str)
    parser.add_argument('predict_column', metavar='Y', help='Column, which we will predict', type=str)
    args = parser.parse_args()
    main(args.filepath, args.predict_column)