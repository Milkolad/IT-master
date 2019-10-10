symbols = 'asdfgfdsa12345431adg'
cg = tuple(ord(symbol) for symbol in symbols if ord(symbol) < 127)
print(cg)