import sys
from smoother import Smoother

def main(filepath, start, end, alpha):
    print(f'Start\t\n')

    print(f'{filepath}\t{start}\t{end}\t{alpha}')

    smoother = Smoother(filepath, start, end, alpha)

    if start is None and end is None and alpha is None:
        smoother.plot(isRaw=True).savefig('Raw.png')
    else:
        smoother.plot(isRaw=False, alpha=alpha, start=start, end=end).savefig(f'smoothed_from_{start}_to_{end}_with_{alpha}.png')
    print(f'End\t\n')
    return 0

def help():
    print('=== Welcome to exponent smoothing method. ===\n\n')
    print('For usage input next args:\n')
    print('main.py <filepath> <start part of serial> <end part of serial> <filter coef> or main.py <filepath> -r, --raw')
    print('<filepath>\tpath in unix way with .dat format')
    print('<start>\tint number, which defines the start of the serial for smoothing')
    print('<end>\tint number,which defines the end of the serial for smoothing')
    print('<filter coef>\tcoefficient which defines the deep of smoothing. The less number makes the deeper smoothing')
    print('-r, --raw for generating raw plot')
    
if __name__ == "__main__":
    if len(sys.argv) < 1:
        raise SyntaxError("No args. Please, start the program with needed arguments or start with -h, --help to read startup guide.")
    elif len(sys.argv) < 4:
        if str(sys.argv[1]) == '-h' or str(sys.argv[1]) == '--help':
            help()
        elif str(sys.argv[2]) == '-r' or str(sys.argv[2]) == '--raw':
            main(str(sys.argv[1]), None, None, None)
    else:
        main(str(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]))