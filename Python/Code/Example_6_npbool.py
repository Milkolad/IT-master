import numpy as np 


rng = np.random.RandomState(1)
x = rng.randint(10, size=(3, 4))
print(f'count_nonzero: {np.count_nonzero(x < 6)}')

print(f'sum: {np.sum(x < 6)}')

print(f'{np.sum(x < 6) * x}')
print(f'{np.sum(x[x < 6])}')

print(f'{np.sum(x < 6, axis=1)}')

print(f'{np.sum((x > 3) & (x < 7))}')

print(f'{np.sum(~( (x <= 3) | (x >=7 ) ))}')

print(f'Прихотливая индексация: {x[x<5]}')

print(f'{x < 5}')

print(f'{np.mean(x[x<5])}')

print(f'{x[1,1]}')