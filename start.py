import requests

API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhZHZlcnRpc2luZy5wZXJmb3JtYW5jZS5vem9uLnJ1IiwiZXhwIjoxNzM3MjQ0NTQ4LCJpYXQiOjE3MzcyNDI3NDgsImlzcyI6InBlcmZvcm1hbmNlLWF1dGgub3pvbi5ydSIsInN1YiI6IjUxNDYxNjc5LTE3MzcyNDI2NjkzMzNAYWR2ZXJ0aXNpbmcucGVyZm9ybWFuY2Uub3pvbi5ydSJ9.mEgRNS48b-37QlCVRK3FFirZG07AV1vFRmGZLFYNYog'
BASE_URL = 'https://api-performance.ozon.ru'

headers = {
    'Client-Id': '51461679-1737242669333@advertising.performance.ozon.ru',  # Получается на платформе Ozon
    'Api-Key': API_KEY
}

# Пример запроса на получение списка товаров
response = requests.get(f"{BASE_URL}/api/client/statistics", headers=headers)

if response.status_code == 200:
    products = response.json()
    print(products)
else:
    print(f"Ошибка: {response.status_code}")
