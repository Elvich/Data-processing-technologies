import xml.etree.ElementTree as ET
import json
import pandas as pd

print("3.1")
print("*"*100+"\n")

tree = ET.parse('steps_sample.xml')  # Парсим XML-файл
root = tree.getroot()  # Получаем корень документа


steps_dict = {}

for recipe in root.findall('recipe'):
    recipe_id = recipe.find('id').text
    steps = [step.text for step in recipe.find('steps').findall('step') if step.text]
    steps_dict[recipe_id] = steps

with open('steps_sample.json', 'w', encoding='utf-8') as json_file:
    json.dump(steps_dict, json_file, ensure_ascii=False, indent=4)

print("Словарь успешно сохранен в steps_sample.json")

print()
print("3.2")
print("*"*100+"\n")

steps_count_dict = dict()

for recipe in root.findall('recipe'):
    recipe_id = recipe.find('id').text
    steps = recipe.find('steps').findall('step')
    step_count = len(steps)
    if step_count not in steps_count_dict: steps_count_dict[step_count] = []
    steps_count_dict[step_count].append(recipe_id)

print("Сформированный словарь:")
print(list(steps_count_dict.items())[0])

print()
print("3.3")
print("*"*100+"\n")

recipes_with_time = []

for recipe in root.findall('recipe'):
    recipe_id = recipe.find('id').text
    steps = recipe.find('steps').findall('step')

    for step in steps:
        if step.attrib.get('has_minutes') or step.attrib.get('has_hours'):
            recipes_with_time.append(recipe_id)
            break


print("Список рецептов с информацией о времени:")
print(list(recipes_with_time)[:15])

print()
print("3.4")
print("*"*100+"\n")

recipes_df = pd.read_csv('recipes_sample.csv')

IdToStepsNum = {rid: len(steps) for rid, steps in steps_dict.items()}
recipes_df['n_steps'] = recipes_df.apply(
    lambda row: IdToStepsNum.get(row['id'], row['n_steps']) if
    pd.isna(row['n_steps']) else row['n_steps'],
    axis=1
)
print(recipes_df.head())

print()
print("3.5")
print("*"*100+"\n")

if recipes_df['n_steps'].isnull().sum() == 0: recipes_df['n_steps'] = recipes_df['n_steps'].astype(int)
recipes_df.to_csv('recipes_sample_with_filled_nsteps.csv', index=False)
print(recipes_df['n_steps'].dtype, recipes_df['n_steps'].isnull().sum())