import numpy as np

# Параметры
x_min, x_max = 0, 5
y_min, y_max = 0, 5
step = 0.01  # Шаг дискретизации

# Создание сетки точек
x = np.arange(x_min, x_max + step, step)
y = np.arange(y_min, y_max + step, step)
X, Y = np.meshgrid(x, y)

# Вычисление значения функции z(x, y)
Z = X * Y * np.sin(X) * np.cos(Y)

# Определение области, где z(x, y) > 0.25
condition = Z > 0.25

# Доля точек, удовлетворяющих условию
fraction = np.mean(condition)

# Общая площадь прямоугольника
total_area = (x_max - x_min) * (y_max - y_min)

# Площадь области, где z(x, y) > 0.25
area_of_interest = fraction * total_area

# Вывод результата
print(f"Площадь области, где z(x, y) > 0.25: {area_of_interest:.2f}")