symbols = 'asdfgfdsa12345431adg'
codes = list(filter(lambda c: c < 127, map(ord, symbols)))
print(codes)