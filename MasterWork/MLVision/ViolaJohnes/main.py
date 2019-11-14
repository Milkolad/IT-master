import numpy as np
import os
from PIL import Image
from argparse import ArgumentParser

def integral_image(img):
    new_img = np.array(img.shape)
    

def main(path):
    return 0

if __name__ == '__main__':
    parser = ArgumentParser(description='Process path to file')
    parser.add_argument('filepath', metavar='PATH', help='path for the file', type=str)
    args = parser.parse_args()
    print('\n')
    main(args.filepath)
    print('\n')