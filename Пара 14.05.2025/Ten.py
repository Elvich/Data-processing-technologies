import pandas as pd

# Загрузка данных
# Данные из sp500hst.txt
file_path = 'sp500hst.txt'
sp500hst = pd.read_csv(file_path, header=None, names=['Date', 'Symbol', 'Open', 'High', 'Low', 'Close', 'Volume'])

# Данные из sp_data2.csv
file_path = 'sp_data2.csv'
sp_data2 = pd.read_csv('sp_data2.csv', header=None, names=['Symbol', 'Name', 'Volume'], delimiter=";")

# Обработка данных
# Создание словаря для маппинга тикеров на их расшифровки
ticker_mapping = sp_data2.set_index('Symbol')['Name'].to_dict()

# Добавление столбца 'Name' с расшифровкой тикеров
sp500hst['Name'] = sp500hst['Symbol'].map(ticker_mapping)

# Сохранение результата
sp500hst.to_csv('sp500hst_names.txt', index=False)