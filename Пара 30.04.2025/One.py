import numpy as np

np.random.seed(24)
ar1 = np.random.randint(-5, 6, size=(10, 4))
ar2 = np.random.randint(-5, 6, size=(10, 4))

print("Массив ar1:")
print(ar1)
print("\nМассив ar2:")
print(ar2)

mask = ar1 > ar2
result = np.where(mask, ar1 * 2, 0)

print("\nРезультат:")
print(result)