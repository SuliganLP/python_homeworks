import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(".env")

mongo_uri = os.getenv("MONGO_URI")
db_name = os.getenv("MONGO_DB")

client = MongoClient(mongo_uri)

db = client[db_name]
collection = db["products_121225ptm_Suligan"]

collection.delete_many({})

items = [
    {"name": "Pen", "price": 1.50, "stock": 300},
    {"name": "Pencil", "price": 0.99, "stock": 500},
    {"name": "Eraser", "price": 0.75, "stock": 200},
]

result = collection.insert_many(items)

print(f"{len(result.inserted_ids)} inserted")

print("-" * 30)

result = collection.update_many({}, {"$mul": {"price": 1.2}})

print(f"Price updated for {result.modified_count} products.")

print("Updated products:")
for product in collection.find({}, {"_id": 0, "name": 1, "price": 1}):
    print(f"- {product['name']} - ${product['price']:.2f}")

client.close()
