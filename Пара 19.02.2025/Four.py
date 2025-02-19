import numpy as np

# Определение матриц A, B и C
A = np.array([[-1, 2, 4], [-3, 1, 2], [-3, 0, 1]])
B = np.array([[3, -1], [2, 1]])
C = np.array([[7, 21], [11, 8], [8, 4]])

# Находим обратные матрицы A^(-1) и B^(-1)
A_inv = np.linalg.inv(A)
B_inv = np.linalg.inv(B)

# Вычисляем матрицу X
X = -np.dot(np.dot(A_inv, C), B_inv)

print("Матрица X:")
print(X)