from argparse import ArgumentParser
import time
import cv2
import numpy as np

def integral_image(img):
    int_img = np.zeros(img.shape)
    for i, _ in enumerate(img):
        for j, _ in enumerate(img):
            if i is not 0 and j is not 0:
                int_img[i, j] = img[i, j] + img[i - 1, j]
            elif i is not 0 and j is 0:
                int_img[i, j] = img[i,j] + img[i - 1 ,j]
            elif j is not 0 and i is 0:
                int_img[i, j] = img[i, j] + img[i, j - 1]
    return int_img

def main(path):
    #img = cv2.imread(path)[::-1]
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    clf = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    print(f'========\tSTARTING SCORE TEST OF VIOLA-JONES ALGORITM OF OBJECT DETECTION\t========\n')
    print(cv2.getBuildInformation())

    start_t = time.perf_counter()
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
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