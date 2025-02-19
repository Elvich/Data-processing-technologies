import numpy as np

# Определение двух векторов
vector1 = np.random.randint(0, 10, 1)
vector2 = np.random.randint(0, 10, 1)

# Вычисление евклидова расстояния
distance = np.linalg.norm(vector1 - vector2)

print("Евклидово расстояние:", distance)