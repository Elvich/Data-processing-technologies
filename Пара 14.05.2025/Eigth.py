import pandas as pd

file_path = 'sp500hst.txt'

# Чтение файла
df = pd.read_csv(file_path, header=None, names=['Date', 'Symbol', 'Open', 'High', 'Low', 'Close', 'Volume'])

# Преобразование даты в формат datetime
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')

# Выбор данных для NVDA и AAPL
df_nvda = df[df['Symbol'] == 'NVDA'].copy()
df_aapl = df[df['Symbol'] == 'AAPL'].copy()

# Объединение данных NVDA и AAPL по дате
merged_df = pd.merge(df_nvda, df_aapl, on='Date', suffixes=('_NVDA', '_AAPL'))

# Создание столбца с разницей в объемах
merged_df['Volume_Diff'] = merged_df['Volume_NVDA'] - merged_df['Volume_AAPL']

# Фильтрация строк, где обе акции закрылись выше цены открытия
filtered_df = merged_df[
    (merged_df['Close_NVDA'] > merged_df['Open_NVDA']) &
    (merged_df['Close_AAPL'] > merged_df['Open_AAPL'])
]

# Выбор необходимых столбцов
result_df = filtered_df[['Date', 'Open_NVDA', 'Close_NVDA', 'Volume_NVDA', 'Open_AAPL', 'Close_AAPL', 'Volume_AAPL', 'Volume_Diff']]

# Вывод результата
print(result_df)