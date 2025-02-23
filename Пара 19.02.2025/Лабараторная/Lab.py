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

#Находим все рецепты с 0-левым временем
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

print()
print("Задание 7")
print()

#Выбираем третий столбец
recipe_ingredients = data[:, 2]

#Ищем отфильтрованные данные
filtred_data = data[recipe_ingredients <= 5]

print("Отфильтрованные данные: ")
print(filtred_data)

print()
print("Задание 8")
print()

# Выбираем второй и третий столбцы (время и количество ингредиентов)
times = data[:, 1]       # Время приготовления
ingredients = data[:, 2] # Количество ингредиентов

# Вычисляем среднее количество ингредиентов на одну минуту для каждого рецепта
# Обрабатываем случай деления на ноль: если время равно 0, результат будет nan
average_ingredients_per_minute = ingredients / np.where(times == 0, 1, times)

# Находим максимальное значение среди всех рецептов
max_average = np.nanmax(average_ingredients_per_minute)

print(f"Максимальное среднее количество ингредиентов на минуту: {max_average}")

print()
print("Задание 9")
print()

# Отсортируем данные по второму столбцу (время приготовления) в порядке убывания
sorted_data = data[np.argsort(-data[:, 1])]

# Выберем первые 100 рецептов
top_100_recipes = sorted_data[:100]

# Вычислим среднее количество ингредиентов для этих рецептов
average_ingredients = np.mean(top_100_recipes[:, 2])

print(f"Среднее количество ингредиентов для топ-100 рецептов: {average_ingredients}")

print()
print("Задание 10")
print()

# Генерируем 10 уникальных случайных индексов
random_indices = np.random.choice(data.shape[0], size=10, replace=False)

# Выбираем строки по случайным индексам
random_recipes = data[random_indices]

print("Информация о 10 случайных рецептах:")
print(random_recipes)

print()
print("Задание 11")
print()

# Выбираем третий столбец (количество ингредиентов)
ingredients = data[:, 2]

# Вычисляем среднее значение количества ингредиентов
mean_ingredients = np.mean(ingredients)

# Находим количество рецептов, где количество ингредиентов меньше среднего
count_below_mean = np.sum(ingredients < mean_ingredients)

# Рассчитываем процент таких рецептов
total_recipes = len(ingredients)
percentage_below_mean = (count_below_mean / total_recipes) * 100

# Выводим результат
print(f"Среднее количество ингредиентов: {mean_ingredients:.2f}")
print(f"Процент рецептов с количеством ингредиентов меньше среднего: {percentage_below_mean:.2f}%")

print()
print("Задание 12")
print()

# Выбираем второй и третий столбцы (время и количество ингредиентов)
times = data[:, 1]
ingredients = data[:, 2]

# Создаем маску для "простых" рецептов
is_simple = (times <= 20) & (ingredients <= 5)

# Преобразуем маску в числа (True -> 1, False -> 0)
simple_column = is_simple.astype(int)

# Добавляем новый столбец к массиву
data_with_simple = np.hstack((data, simple_column[:, np.newaxis]))

# Выводим результат
print("Обновленный датасет с дополнительным столбцом:")
print(data_with_simple)

print()
print("Задание 13")
print()

print(f"Процент 'простых' рецептов: {np.sum(simple_column)/len(simple_column) * 100}%")

print()
print("Задание 14")
print()

# Выбираем второй столбец (время приготовления)
times = data[:, 1]

# Разделяем данные на три группы
short_recipes = data[times < 10]           # Короткие рецепты
standard_recipes = data[(times >= 10) & (times < 20)]  # Стандарные рецепты
long_recipes = data[times >= 20]           # Длинные рецепты

# Определяем минимальный размер среди групп
min_size = min(len(short_recipes), len(standard_recipes), len(long_recipes))

# Обрезаем каждую группу до минимума
short_recipes = short_recipes[:min_size]
standard_recipes = standard_recipes[:min_size]
long_recipes = long_recipes[:min_size]
# numpy, по не понятным для меня причинам, не может создать стандартный трехмерный массив, если все оси не имеют одинаковую фиксированную длину


# Создаем трехмерный массив
grouped_data = np.array([short_recipes, standard_recipes, long_recipes])

# Выводим форму массива
print("Форма трехмерного массива:", grouped_data)