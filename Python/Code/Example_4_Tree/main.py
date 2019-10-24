import pandas as pd
import numpy as np
from argparse import ArgumentParser
from ID3 import ID3
from sklearn.tree import DecisionTreeClassifier
from switcher import Switcher

def main(path, predict_column):
    df = pd.read_csv(path)
    columns = df.columns.values
    X = [df[column].values for column in columns if column != predict_column and column != 'Name']
    y = df[predict_column].values

    swtch = Switcher()

    sk_X = []
    for column in X:
        converted = np.array(swtch.convert_to(column))
        sk_X.append(converted)
    sk_X = np.array(sk_X).T

    sk_y = np.array(swtch.convert_to(y)).T

    decisions = ID3()
    entropy= decisions.fit(X, y)
    print(f'Entropies:\t\t\t{entropy}')

    sk_decisions = DecisionTreeClassifier(random_state=1370)
    sk_decisions.fit(sk_X, sk_y)
    print(f'SkLearn Tree Decision accuracy:\t{sk_decisions.score(sk_X, sk_y)}')
    #print(sk_decisions.predict(['pycharm', 'Java', 'tea']))
    return 0

if __name__ == '__main__':
    parser = ArgumentParser(description='Process path to file')
    parser.add_argument('filepath', metavar='PATH', help='path for the file', type=str)
    parser.add_argument('predict_column', metavar='Y', help='Column, which we will predict', type=str)
    args = parser.parse_args()
    print('\n')
    main(args.filepath, args.predict_column)
    print('\n')