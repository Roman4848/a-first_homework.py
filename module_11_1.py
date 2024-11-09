#Я выберу библиотеки requests, pandas и matplotlib,
# так как они предоставляют мощные инструменты для работы с данными,
# анализа и визуализации. Ниже приведено краткое описание возможностей каждой библиотеки,
# примеры кода и ссылки на документацию.

#1. requests - эта библиотека позволяет легко отправлять HTTP-запросы.
# Она проста в использовании и предлагает широкий набор возможностей для работы с веб-сервисами.

#Документация: https://requests.readthedocs.io/en/latest/



import requests

# Получение данных с сайта
response = requests.get('https://www.example.com')

# Вывод статуса ответа
print(response.status_code)

# Вывод заголовков ответа
print(response.headers)

# Вывод текста ответа
print(response.text)



#2. pandas - эта библиотека предоставляет инструменты для работы с данными.
# Она позволяет импортировать, очищать, анализировать, манипулировать и визуализировать данные.

#Документация: https://pandas.pydata.org/docs/

import pandas as pd

# Загрузка данных
data = pd.read_csv('C:/Users/Evgeny PC/PycharmProjects/pythonProject/proect_1/module_11/data.csv')

# Проверка содержимого DataFrame
print(data.head())
print(data.columns)

# Преобразование столбца 'column1' в числовой формат
data['column1'] = pd.to_numeric(data['column1'], errors='coerce')

# Вычисление среднего значения
mean_value = data['column1'].mean()
print("Среднее значение:", mean_value)

#3. matplotlib - эта библиотека предлагает инструменты для создания различных типов графиков.
# Она предоставляет гибкость и настраиваемость для создания высококачественных визуализаций данных.

#Документация: https://matplotlib.org/stable/contents.html

import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание графика
plt.plot(x, y)

# Добавление заголовка и меток
plt.title("Простой график")
plt.xlabel("X")
plt.ylabel("Y")

# Показ графика
plt.show()