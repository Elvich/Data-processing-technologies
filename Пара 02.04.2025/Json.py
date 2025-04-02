import json
import pandas as pd

with open("contributors_sample.json", "r") as file:
    data = json.load(file)

print("1.1")
print("*"*100+"\n")
for i, user in enumerate(data[:3], start=1):
    print(f"Пользователь {i}:")
    print(f" Login: {user['username']}")
    print(f" ID: {user['id']}")
    print(f" Пол: {user['sex']}\n")

print()
print("1.2")
print("*"*100+"\n")

unique_domains = set()
for user in data:
    mail = user['mail']
    if mail:
        domain = mail.split('@')[-1]
        unique_domains.add(domain)

print(f"Уникальные домены: {unique_domains}")

print()
print("1.3")
print("*"*100+"\n")

def find_user_by_username(users, username):
    for user in users:
        if user.get('username') == username:
            print("Найден пользователь:")
            print(f"  Login: {user['username']}")
            print(f"  ID: {user['id']}")
            if 'email' in user:
                print(f"  Mail: {user['mail']}")
            else:
                print("  Mail: Не указан")
            return

    raise ValueError(f"Пользователь с именем '{username}' не найден.")

userNameTrue = "uhebert"
userNameFalse = "adsfqwed"
find_user_by_username(data,userNameTrue)

print()
print("1.4")
print("*"*100+"\n")

male_count = 0
female_count = 0
for user in data:
    gender = user["sex"]
    if gender == "M": male_count+=1
    else: female_count+=1

print(f"Мужчин - {male_count} \nЖенщин - {female_count}")

print()
print("1.5")
print("*"*100+"\n")

contributors_data = [
    {
        'id': user['id'],
        'username': user['username'],
        'sex': user['sex']
    }
    for user in data
]

contributors_df = pd.DataFrame(contributors_data)
print(contributors_df.head())

print()
print("1.6")
print("*"*100+"\n")

recipes = pd.read_csv('recipes_sample.csv')
merged_df = recipes.merge(contributors_df, on='id', how='left')
missing_info_count = merged_df['username'].isna().sum() #проверяем столбец username на наличие пропущенных значений (NaN) с помощью метода .isna()

print(f"Количество строк в recipes, для которых отсутствует информация о человеке: {missing_info_count}")
