import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("1. Базовые операции с DataFrame \n")

print("1.1 Загрузка файлов")
recipes = pd.read_csv("recipes_sample.csv")
reviews = pd.read_csv('sp_data2.csv',delimiter=";", skiprows=1) # Убираем безымянный индекс
print()

print("1.2 Основные параметры таблиц")
print(recipes.info())  # Информация о recipes
print(reviews.info())  # Информация о reviews
print()

print("1.3 Пропущенные значения")
missing_recipes = recipes.isnull().mean() * 100
missing_reviews = reviews.isnull().mean() * 100

print("Пропуски в recipes:\n", missing_recipes)
print("Пропуски в reviews:\n", missing_reviews)
print()

print("1.4 Средние значения числовых столбцов")
print(recipes.describe())
print(reviews.describe())
print()

print("1.5 10 случайных названий рецептов")
print(recipes["name"].sample(10))
print()

print("1.6 Изменение индекса в reviews")
reviews.reset_index(drop=True, inplace=True)
print(reviews.head())
print()

print("1.7 Фильтр: рецепты до 20 минут и ≤ 5 ингредиентов")
filtered_recipes = recipes[(recipes["minutes"] <= 20) & (recipes["n_ingredients"] <= 5)]
print(filtered_recipes)
print()