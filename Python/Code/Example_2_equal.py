real_ivan = {'name' : 'Ivan'}
fake_ivan = {'name' : 'Ivan'}

print(id(real_ivan), id(fake_ivan))
print(real_ivan == fake_ivan)
print(real_ivan is fake_ivan)