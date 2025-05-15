import numpy as np

ar = np.random.randint(0, 101, size=(30, 4))

print("Исходный массив:")
print(ar)

norms = np.linalg.norm(ar, axis=1)
top5Indices = np.argsort(norms)[-5:]
top5Vectors = ar[top5Indices]

print("\nМассив из 5 строк с наибольшими нормами:")
print(top5Vectors)