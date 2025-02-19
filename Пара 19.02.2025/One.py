import numpy as np

arr = np.random.uniform(0,20,(4,7))

print(arr)

minn = arr.min()
maxx = arr.max()

print(minn,maxx)

a = 1/(maxx-minn)
print(a)
b = -a * minn
print(b)

print(a*minn+b)

arr = arr*a+b
print(arr)