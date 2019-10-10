import array
symbols = 'asdfgfdsa12345431adg'
cg = array.array('I', (ord(symbol) for symbol in symbols if ord(symbol) < 127))
print(cg)