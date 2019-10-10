symbols = 'asdfgfdsa12345431adg'
codes = [ord(symbol) for symbol in symbols if ord(symbol) < 127]
print(codes) 