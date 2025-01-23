import requests
import json
import pandas as pd
from sqlalchemy import create_engine

# URL API Wildberries
URL = "https://catalog.wb.ru/catalog/autoproduct33/v2/catalog"

# Параметры запроса
PARAMS = {
    "ab_testing": "false",
    "appType": "1",
    "curr": "rub",
    "dest": "-1570684",
    "hide_dtype": "10",
    "lang": "ru",
    "page": "1",
    "sort": "popular",
    "spp": "30",
    "subject": "3906",
    "uclusters": "0",
    "uiv": "8"
}

# Заголовки для запроса (чтобы не заблокировали)
HEADERS = {
    "accept": "*/*",
    "accept-language": "ru,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

# Подключение к PostgreSQL
DB_URL = "postgresql://user:password@localhost:5432/wildberries"
engine = create_engine(DB_URL)

def parse_wildberries():
    response = requests.get(URL, params=PARAMS, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        products = data.get("data", {}).get("products", [])

        items = []
        for product in products:
            items.append({
                "id": product.get("id"),
                "name": product.get("name"),
                "brand": product.get("brand"),
                "price": product.get("sizes", [{}])[0].get("price", {}).get("total", 0) / 100,  # Цена в рублях
                "rating": product.get("reviewRating", 0),
                "reviews": product.get("feedbacks", 0),
                "supplier": product.get("supplier"),
                "supplier_rating": product.get("supplierRating", 0)
            })

        # Создаем DataFrame
        df = pd.DataFrame(items)

        # Сохраняем в базу данных
        df.to_sql("wildberries_products", engine, if_exists="replace", index=False)

        print("✅ Данные успешно спарсены и сохранены в БД!")

    else:
        print(f"❌ Ошибка запроса: {response.status_code}")

# Запуск парсера
parse_wildberries()
