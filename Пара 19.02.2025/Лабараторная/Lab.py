import numpy as np

print("Задание 1")
print()
# Считываем данные из файла, пропуская первую строку (заголовки)
data = np.loadtxt('minutes_n_ingredients.csv', delimiter=',', dtype=np.int32, skiprows=1)

# Выводим первые 5 строк массива
print("Первые 5 строк массива:")
print(data[:5])

print()
print("Задание 2")
print()
# Извлечение второго и третьего столбцов (все столбцы, кроме первого)
columns = data[:, 1:]

# Вычисление статистик для каждого столбца
mean_values = np.mean(columns, axis=0)  # Среднее значение
min_values = np.min(columns, axis=0)    # Минимум
max_values = np.max(columns, axis=0)    # Максимум
median_values = np.median(columns, axis=0)  # Медиана

# Вывод результатов
print("Средние значения:", mean_values)
print("Минимумы:", min_values)
print("Максимумы:", max_values)
print("Медианы:", median_values)

print()
print("Задание 3")
print()

second_column = data[:, 1]

# Вычисляем квантиль q_0.75
q_75 = np.quantile(second_column, 0.75)

print(f"Квантиль q_0,75: {q_75}")

data_minimum_second_column = data.copy()
data_minimum_second_column[:,1] = np.minimum(data_minimum_second_column[:,1], q_75)

print("Данные с ограничением родолжительности выполнения рецепта: ")
print(data_minimum_second_column)

print()
print("Задание 4")
print()

zero_count = np.sum(second_column == 0)

print(f"Количество рецептов с продолжительностью 0: {zero_count}")

data_four = data.copy()
# Заменяем значения, равные нулю, на 1
data_four[second_column == 0, 1] = 1

# Выводим обновленные данные
print("Пример на 693 строке:")
print(data[691])
print(data_four[691])

print()
print("Задание 5")
print()

# Выбираем первый столбец (идентификаторы рецептов)
recipe_ids = data[:, 0]

# Находим уникальные значения и их количество
unique_recipes = np.unique(recipe_ids)

print(f"Количество уникальных рецептов: {len(unique_recipes)}")

print()
print("Задание 6")
print()

unique_ingredients = np.unique(data[:, 2])
print(f"Количество уникальных ингедиентов: {len(unique_ingredients)}")
print("Ингредиенты:")
print(unique_ingredients)
