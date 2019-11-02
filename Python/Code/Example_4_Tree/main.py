import pandas as pd
import numpy as np
from argparse import ArgumentParser
from ID3 import ID3
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from switcher import Switcher

def main(path, predict_column):
    df = pd.read_csv(path)
    columns = df.columns.values
    X = [df[column].values for column in columns if column != predict_column and column != 'Name']
    y = df[predict_column].values
    

    decisions = ID3()
    fitted = decisions.fit(X, y)
    print(f'Entropy of {predict_column}:\t\t\t{fitted[1]}\n')
    print(f'Information Gains of Xs\n')
    print(f'{str(list(filter(lambda x: x != predict_column and x != "Name", df.columns.values)))}')
    print(f'{fitted[0]}')

    swtch = Switcher()

    sk_X = []
    for column in X:
        converted = np.array(swtch.convert_to(column))
        sk_X.append(converted)
    sk_X = np.array(sk_X).T

    sk_y = np.array(swtch.convert_to(y)).T

    x_train, x_test, y_train, y_test = train_test_split(sk_X, sk_y, test_size=0.3)    

    sk_decisions = DecisionTreeClassifier(random_state=1370)
    sk_decisions.fit(x_train, y_train)
    print(f'SkLearn Tree Decision accuracy:\t{sk_decisions.score(x_train, y_train)}')
    print(f'SkLearn Tree Decision prediction: {sk_decisions.predict(x_test)}')
    return 0

if __name__ == '__main__':
    parser = ArgumentParser(description='Process path to file')
    parser.add_argument('filepath', metavar='PATH', help='path for the file', type=str)
    parser.add_argument('predict_column', metavar='Y', help='Column, which we will predict', type=str)
    args = parser.parse_args()
    print('\n')
    main(args.filepath, args.predict_column)
    print('\n')