import numpy as np

# Broadcasting

a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
print(a + b)

print(a + 5)

M = np.ones((3, 3))
print(M)

print(M + a)

a = np.arange(3)
b = np.arange(3)[:, np.newaxis]

print(a, '\n', b)

print(a + b)

print('Двумерный массив и одномерный')
M = np.ones((2, 3))
a = np.arange(3)

print(M, ' + ', a, ' = \n', M + a)

print('Оба массива растягиваются')
a = np.arange(3).reshape((3, 1))
b = np.arange(3)
print(a, ' + ', b, ' = \n', a + b)

print()
M = np.ones((3, 2))
a = np.arange(3)
print(M, ' + ', a, ' = \n', M + a[:, np.newaxis])
print(a[:, np.newaxis].shape)

print('Центрирование слуайной величины')
X = np.random.random((10, 3))
print(X)

Xmean = X.mean(0)
print(f'Meaned: {Xmean}')

X_centered = X - Xmean
print(f'Centered: {X_centered}')
print(f'Centered mean: {X_centered.mean(0)}')

print('График двумерной плоскости')
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]

z = np.cos(13 + y * x) * np.cos(x) + np.sin(x) ** 8

print(x, y, z)


import matplotlib.pyplot as plt

result = plt.figure()
plt.imshow(z, extent=[0, 5, 0, 5], cmap='gray')
plt.colorbar()
result.savefig('plot.png')