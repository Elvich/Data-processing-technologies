import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("1. Базовые операции с DataFrame \n")

print("1.1 Загрузка файлов")
recipes = pd.read_csv("recipes_sample.csv", parse_dates=['submitted'], header=0)
reviews = pd.read_csv('reviews_sample.csv') # Убираем безымянный индекс
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

print("-"*50)
print("2. Работа с датами в pandas")

print("2.2 Рецепты, добавленные до 2010 года")
otvet22 = recipes[recipes['submitted'].dt.year <= 2010]
print(f"Рецепты, добавленные не позже 2010 года: \n{otvet22.head()}")
# ДЛЯ ПРОВЕРКИ
print(f"Даты рецептов: \n{otvet22['submitted'].head()}")

print("-"*50)
print("3. Работа со строковыми данными")
print("3.1 Добавление description_length (длина описания рецепта)")
recipes["description_length"] = recipes["description"].astype(str).apply(len)
print(recipes.head())

print("3.2 Изменение заглавных букв в названиях")
recipes["name"] = recipes["name"].str.title()
print(recipes.head())

print("3.3 Подсчет слов в названии рецепта")
recipes["name_word_count"] = recipes["name"].str.split().str.len()
print(recipes.head())

print("-"*50)
print("4. Группировки таблиц")
print("4.1 Количество рецептов от каждого contributor_id")

by_id = recipes.groupby('contributor_id')[['id']].count()
print(by_id)
print()
by_id_max = by_id.max()
print(by_id_max)
print()
print(by_id[by_id['id'] == 421])
print()


print("4.2 Средний рейтинг рецептов, количество без отзывов")
rec_rate = reviews.groupby('recipe_id')[['rating']].mean()
print(rec_rate)
print()

rec_an = reviews.groupby('recipe_id')[['rating','review']]
rec_non = reviews[['rating','review']].isna().sum()
print(rec_non)
print()


print("4.3 Количество рецептов по годам")
by_year = reviews.groupby('date')[['recipe_id']].count()
print(by_year)



print("-"*50)
print("5. Объединение таблиц")
print("5.1 DataFrame id, name, user_id, rating (без рецептов без отзывов)")
df_5_1 = recipes.merge(reviews, left_on="id", right_on="recipe_id")[["id", "name", "user_id", "rating"]]
print(df_5_1.head())

print("5.2 DataFrame recipe_id, name, review_count")
review_counts = reviews.groupby("recipe_id")["review"].count().reset_index()
review_counts.columns = ["recipe_id", "review_count"]
df_5_2 = recipes.merge(review_counts, left_on="id", right_on="recipe_id", how="left").fillna(0)
print(df_5_2.head())

print("5.3 Год с наименьшим средним рейтингом")
recipes_with_ratings = recipes.merge(reviews.groupby("recipe_id")["rating"].mean(), left_on="id", right_index=True)
yearly_ratings = recipes_with_ratings.groupby(recipes_with_ratings["submitted"].dt.year)["rating"].mean()
worst_year = yearly_ratings.idxmin()
print(f"Год с худшим средним рейтингом: {worst_year}")

print("-"*50)
print("6. Сохранение результатов")
print("6.1 Сортировка по name_word_count и сохранение в CSV")
recipes_sorted = recipes.sort_values(by="name_word_count", ascending=False)
recipes_sorted.to_csv("recipes_sorted.csv", index=False)

print("6.2 Сохранение 5.1 и 5.2 в Excel")

import re

def clean_text(text):
    if isinstance(text, str):
        return re.sub(r"[\x00-\x1F\x7F]", "", text)  # Удаляем невидимые символы
    return text

df_5_2 = df_5_2.map(clean_text)  # Применяем ко всем ячейкам

with pd.ExcelWriter("laba2_6.2.xlsx") as writer:
    df_5_1.to_excel(writer, sheet_name="Рецепты с оценками", index=False)
    df_5_2.to_excel(writer, sheet_name="Количество отзывов по рецептам", index=False)