import pandas as pd

print("\n\n" + "#-------------- Т.Н. 'РАЗМИНКА' -----------------#" + "\n\n")

print("\n\n" + "#-------------- ЗАДАНИЕ №1 -----------------#" + "\n\n")

fileName = 'sp500hst.txt'
columns = ["date", "ticker", "open", "high", "low", "close", "volume"]
data = pd.read_csv(fileName, header=None, names=columns)
print(data.head())

print("\n\n" + "#-------------- ЗАДАНИЕ №2 -----------------#" + "\n\n")

otvetRazm2 = data[["open", "high", "low", "close"]].mean()
print(otvetRazm2.values)

print("\n\n" + "#-------------- ЗАДАНИЕ №3 -----------------#" + "\n\n")

data["date"] = pd.to_datetime(data["date"], format='%Y%m%d')
data["month"] = data["date"].dt.month
print(data.head())

print("\n\n" + "#-------------- ЗАДАНИЕ №4 -----------------#" + "\n\n")

otvetRazm4 = data.groupby("ticker")["volume"].sum()
print(otvetRazm4)

print("\n\n" + "#-------------- ЗАДАНИЕ №5 -----------------#" + "\n\n")

data1 = pd.read_csv(fileName, header=None, names=columns)
sp_data2 = pd.read_csv('sp_data2.csv', delimiter=';',
                       names=['ticker','name'],usecols=[0,1])
otvetRazm5 = pd.merge(data, sp_data2, on="ticker", how="left")
otvetRazm5["name"] = otvetRazm5["name"].fillna("Неизвестное имя")
print(otvetRazm5.head())


print("\n\n" + "#-------------- ЛАБОРАТОРНАЯ РАБОТА №2 -----------------#" + "\n\n")

print("#-------------- ЗАДАНИЕ №1.1 + 2.1 -----------------#" + "\n\n")

recipes = pd.read_csv('recipes_sample.csv', parse_dates=['submitted'])
reviews = pd.read_csv('reviews_sample.csv', index_col=0)
print(recipes._typ, reviews._typ)

print("\n\n" + "#-------------- ЗАДАНИЕ №1.2 -----------------#" + "\n\n")

print("Таблица recipes_sample.csv:\n")
print(f"Количество строк: {recipes.shape[0]}")
print(f"Количество столбцов: {recipes.shape[1]}")
print(f"Типы данных каждого столбца:\n{recipes.dtypes}\n")

print("Таблица reviews_sample.csv:\n")
print(f"Количество строк: {reviews.shape[0]}")
print(f"Количество столбцов: {reviews.shape[1]}")
print(f"Типы данных каждого столбца:\n{reviews.dtypes}\n")

print("\n\n" + "#-------------- ЗАДАНИЕ №1.3 -----------------#" + "\n\n")

missingRecipes = recipes.isnull().any(axis=1).mean()
missingReviews = reviews.isnull().any(axis=1).mean()
print(f"Доля строк с пропусками в Recipes: {missingRecipes:.2%}")
print(f"Доля строк с пропусками в Reviews: {missingReviews:.2%}\n")

print("\n\n" + "#-------------- ЗАДАНИЕ №1.4 -----------------#" + "\n\n")

print(f"Средние значения числовых столбцов в Recipes:\n{recipes.mean(numeric_only=True)}")
print(f"\nСредние значения числовых столбцов в Reviews:\n{reviews.mean(numeric_only=True)}")

print("\n\n" + "#-------------- ЗАДАНИЕ №1.5 -----------------#" + "\n\n")
# Если что, random_state тут как своеобразный "seed" для рандома, чтобы выбивало один и тот же результат
# Можно это представить как сид для мира в майнкрафте
otvet15 = recipes['name'].sample(10, random_state=42)
print(otvet15)

print("\n\n" + "#-------------- ЗАДАНИЕ №1.6 -----------------#" + "\n\n")

print(f"Старый индекс в таблице Reviews (для проверки): \n{reviews.head()}")
reviews.reset_index(drop=True, inplace=True)
print(f"Новый индекс в таблице Reviews: \n{reviews.head()}")

print("\n\n" + "#-------------- ЗАДАНИЕ №1.7 -----------------#" + "\n\n")

otvet17 = recipes[(recipes['minutes'] <= 20) & (recipes['n_ingredients'] <= 5)]
print(otvet17.head())

print("\n\n" + "#-------------- ЗАДАНИЕ №2.2 -----------------#" + "\n\n")

otvet22 = recipes[recipes['submitted'].dt.year <= 2010]
print(f"Рецепты, добавленные не позже 2010 года: \n{otvet22.head()}")
# ДЛЯ ПРОВЕРКИ
print(f"Даты рецептов: \n{otvet22['submitted'].head()}")

print("\n\n" + "#-------------- ЗАДАНИЕ №3.1 -----------------#" + "\n\n")

recipes['description_length'] = recipes['description'].str.len()
print(recipes[['name', 'description', 'description_length']].head())

print("\n\n" + "#-------------- ЗАДАНИЕ №3.2 -----------------#" + "\n\n")

recipes['name'] = recipes['name'].str.title()
print(recipes[['name']].head())

print("\n\n" + "#-------------- ЗАДАНИЕ №3.3 -----------------#" + "\n\n")

recipes['name_word_count'] = recipes['name'].str.split().str.len()
print(recipes[['name', 'name_word_count']].head())

print("\n\n" + "#-------------- ЗАДАНИЕ №4.1 -----------------#" + "\n\n")

contributorRecipeCnt = recipes['contributor_id'].value_counts()
maxContributor = contributorRecipeCnt.idxmax()
maxContributorCnt = contributorRecipeCnt.max()
print(f"Количество рецептов, добавленных каждым участником: \n{contributorRecipeCnt}")
print(f"\nУчастник с ID {maxContributor} добавил максимальное количество рецептов: {maxContributorCnt}")

print("\n\n" + "#-------------- ЗАДАНИЕ №4.2 -----------------#" + "\n\n")

actualReviews = reviews[(reviews['rating']).notnull() & (reviews['review'].notnull())]
avgRatings = actualReviews.groupby('recipe_id')['rating'].mean()
rcpsNoReviews = recipes[~recipes['id'].isin(avgRatings.index)]
print(f"Количество рецептов без отзывов: {len(rcpsNoReviews)}")

print("\n\n" + "#-------------- ЗАДАНИЕ №4.3 -----------------#" + "\n\n")

rcpsByYear = recipes['submitted'].dt.year.value_counts().sort_index()
print(f"Количество рецептов с разбивкой по годам: \n{rcpsByYear}")

print("\n\n" + "#-------------- ЗАДАНИЕ №5.1 -----------------#" + "\n\n")

dfMerged = pd.merge(reviews, recipes[['id', 'name']], left_on='recipe_id', right_on='id', how='inner')
otvet51 = dfMerged[['id', 'name', 'user_id', 'rating']]
print(otvet51.head())
# ЧИСТО ПРОВЕРОЧКА
rcpNoReviews = recipes[~recipes['id'].isin(reviews['recipe_id'])].iloc[0]
print(f"Рецепт без отзывов (id={rcpNoReviews['id']}):")
print(otvet51[otvet51['id'] == rcpNoReviews['id']])  # Ожидается пусто и точка

print("\n\n" + "#-------------- ЗАДАНИЕ №5.2 -----------------#" + "\n\n")

rvwCnt = reviews.groupby('recipe_id').size().reset_index(name='review_count')
otvet52 = pd.merge(recipes[['id', 'name']], rvwCnt, left_on='id', right_on='recipe_id', how='left')
otvet52['review_count'] = otvet52['review_count'].fillna(0).astype(int)
print(otvet52.head())
# ещё одна проверка..
print(f"Рецепт без отзывов (id={rcpNoReviews['id']}):")
print(otvet52[otvet52['id'] == rcpNoReviews['id']])  # Если в review_count не 0, значит я напортачил
# UPD: не, не напортачил

print("\n\n" + "#-------------- ЗАДАНИЕ №5.3 -----------------#" + "\n\n")

rcpYears = recipes.copy()
rcpYears['year'] = rcpYears['submitted'].dt.year
ratingsMrgd = pd.merge(reviews, rcpYears[['id', 'year']], left_on='recipe_id', right_on='id', how='inner')
avgRateByYear = ratingsMrgd.groupby('year')['rating'].mean()
print(f"Год с наименьшим средним рейтингом: {avgRateByYear.idxmin()}")

print("\n\n" + "#-------------- ЗАДАНИЕ №6.1 -----------------#" + "\n\n")

rcpsSorted = recipes.sort_values(by='name_word_count', ascending=False)
rcpsSorted.to_csv('laba2_6.1.csv', index=False)

print("\n\n" + "#-------------- ЗАДАНИЕ №6.2 -----------------#" + "\n\n")

# боже, какой же питон моментами медленный..
with pd.ExcelWriter('laba2_6.2.xlsx') as writer:
    otvet51.to_excel(writer, sheet_name='Рецепты с оценками', index=False)
    otvet52.to_excel(writer, sheet_name='Количество отзывов по рецептам', index=False)