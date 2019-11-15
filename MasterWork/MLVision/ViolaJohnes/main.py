import numpy as np
import os
from PIL import Image
from argparse import ArgumentParser
import cv2
import time

def integral_image(img):
    new_img = np.array(img.shape)
    

def main(path):
    img = cv2.imread("./face.jpg")[::-1]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    clf = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    print(f'========\tSTARTING SCORE TEST OF VIOLA-JONES ALGORITM OF OBJECT DETECTION\t========\n')
    print(cv2.getBuildInformation())

    start_t = time.perf_counter()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    end_t = time.perf_counter()
    img_to_gray = end_t - start_t

    start_t = time.perf_counter()
    clf.detectMultiScale(gray, 1.3, 125)
    end_t = time.perf_counter()
    detection = end_t - start_t
    
    print(f'Time has passed:\t{img_to_gray + detection}\t\n')
    print(f'Image converting:\t{img_to_gray}')
    print(f'Object detection:\t{detection}')
    print(f'Image shape in numpy:\t{img.shape}')

    return 0

if __name__ == '__main__':
    parser = ArgumentParser(description='Process path to file')
    parser.add_argument('filepath', metavar='PATH', help='path for the file', type=str)
    args = parser.parse_args()
    print('\n')
    main(args.filepath)
    print('\n')