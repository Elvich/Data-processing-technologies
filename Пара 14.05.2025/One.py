import xml.etree.ElementTree as ET
import json

# Шаг 1: Чтение XML
tree = ET.parse("addres-book-q.xml")
root = tree.getroot()

# Шаг 2: Формирование словаря
result = {}

# Проходим по всем записям в XML
for country in root.findall("country"):
    for addr in country.findall("address"):
        position = addr.find("position").text
        name = addr.find("name").text
        company = addr.find("company").text
        phones = [phone.text for phone in addr.find("phones").findall("phone")]

        # Собираем все телефоны
        person_info = {
            "name": name,
            "company": company,
            "phones": phones
        }

        result.setdefault(position, []).append(person_info)

# Шаг 3: Сохранение в JSON
with open("address_book_by_position.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

# Шаг 4: Загрузка и сравнение
with open("address_book_by_position.json", "r", encoding="utf-8") as f:
    loaded_result = json.load(f)

print("Структуры идентичны:", result == loaded_result)