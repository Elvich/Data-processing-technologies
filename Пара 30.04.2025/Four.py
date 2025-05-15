import numpy as np
import pandas as pd

arr = np.random.randint(0, 51, size=(10, 4))

print("Исходный массив:")
print(arr)

flatArr = arr.ravel()

valueCounts = pd.Series(flatArr).value_counts()
mostFrequentValues = valueCounts[valueCounts == valueCounts.max()].index.values

locations = {value: np.argwhere(arr == value) for value in mostFrequentValues}
print("\nСамые частые числа:", mostFrequentValues)
for value, locs in locations.items():
    print(f"Расположение значения {value}:")
    print(locs)

rowCounts = np.stack([(arr == value).sum(axis=1) for value in mostFrequentValues])
topRowIndices = np.argsort(rowCounts.sum(axis=0))[-3:]

topRowsArray = arr[topRowIndices]

print("\nМассив из 3 строк с наибольшим количеством самых частых значений:")
print(topRowsArray)