import numpy as np

ar1 = np.random.randint(0, 16, size=(25, 4))

print("Исходный массив ar1:")
print(ar1)

maxRow = ar1.max(axis=1, keepdims=True)

isMaxInRow = ar1 == maxRow

countMaxPerCol = isMaxInRow.sum(axis=0)

columnsWithMin5 = np.where(countMaxPerCol >= 5)[0]

print("\nСтолбцы, где максимальное значение встречается не менее 5 раз:")
print(columnsWithMin5)

columnWithMaxCount = np.argmax(countMaxPerCol)

ar1[isMaxInRow[:, columnWithMaxCount], columnWithMaxCount] = -1

print("\nМассив после замены максимумов в столбце с наибольшим количеством максимумов на -1:")
print(ar1)