import requests
from bs4 import BeautifulSoup
import csv
import re
import matplotlib.pyplot as plt

url = 'https://www.divan.ru/category/divany'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

data = []

for price_tag in soup.find_all('span', {'data-testid': 'price'}):
    price_text = price_tag.text.strip()

    price = int(re.sub(r'\D', '', price_text))
    data.append([price])

with open('divan_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])
    writer.writerows(data)

print("Данные сохранены в divan_data.csv")

prices = []
with open('divan_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
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
