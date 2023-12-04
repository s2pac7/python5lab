import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('test.csv')
sample = dataset.head(1000)

missing_values = sample.isnull().sum()
print("Пропущенные значения в данных:\n", missing_values)

plt.figure(figsize=(10, 6))
sample.boxplot(column='Rooms', vert=False, showfliers=True)
plt.xscale('log')
plt.title('Ящик с усами для Rooms')
plt.show()

sample['Rooms'].hist()
plt.title('Гистограмма для Rooms')
plt.show()

# для безопасной обработки
sample_copy = sample.copy()

# Заполнение пропущенных значений медианой
sample_copy['Rooms'].fillna(sample_copy['Rooms'].median(), inplace=True)

# Удаление выбросов по правилу трех сигм
mean = sample_copy['Rooms'].mean()
std = sample_copy['Rooms'].std()
sample_cleaned = sample_copy[(sample_copy['Rooms'] > mean - 3 * std) & (sample_copy['Rooms'] < mean + 3 * std)]

rooms_count = sample_cleaned['Rooms'].value_counts()

# Построение сводной таблицы
pivot_table = sample_cleaned.pivot_table(index='DistrictId', columns='Rooms', aggfunc='size', fill_value=0)

sample_cleaned.to_csv('surname.csv', index=False)
