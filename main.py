import requests
from bs4 import BeautifulSoup
import csv
import re
import matplotlib.pyplot as plt


# URL страницы с диванами
url = 'https://www.divan.ru/category/divany'

# Отправляем запрос к странице
response = requests.get(url)
response.raise_for_status()  # Проверяем, что запрос успешен

# Обрабатываем HTML-код страницы
soup = BeautifulSoup(response.text, 'html.parser')

# Создаем список для хранения данных
data = []

# Находим все элементы с ценами
for price_tag in soup.find_all('span', {'data-testid': 'price'}):
    price_text = price_tag.text.strip()
    # Используем регулярное выражение для извлечения только цифр
    price = int(re.sub(r'\D', '', price_text))
    data.append([price])

# Сохраняем данные в CSV
with open('divan_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])  # Заголовок для CSV
    writer.writerows(data)

print("Данные сохранены в divan_data.csv")

prices = []
with open('divan_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Пропустить заголовок
    for row in reader:
        prices.append(int(row[0]))

# Вычисляем среднюю цену
average_price = sum(prices) / len(prices)
print(f"Средняя цена на диваны: {average_price:.2f} ₽")


# Построение гистограммы цен
plt.hist(prices, bins=20, edgecolor='black')  # bins=20 означает 20 столбцов
plt.title("Распределение цен на диваны")
plt.xlabel("Цена (₽)")
plt.ylabel("Частота")
plt.show()
