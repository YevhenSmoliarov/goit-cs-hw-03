from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["cat_database"]
collection = db["cats"]

# Створення документів (Create)
def create_cat(name, age, features):
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    collection.insert_one(cat)
    print(f"Кіт {name} доданий до бази даних.")

# Читання документів (Read)
def read_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)

def read_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Кота з ім'ям {name} не знайдено.")

# Оновлення документів (Update)
def update_cat_age(name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.modified_count > 0:
        print(f"Вік кота {name} оновлено до {new_age}.")
    else:
        print(f"Кота з ім'ям {name} не знайдено або вік вже був {new_age}.")

def add_feature_to_cat(name, feature):
    result = collection.update_one({"name": name}, {"$push": {"features": feature}})
    if result.modified_count > 0:
        print(f"Характеристика '{feature}' додана до кота {name}.")
    else:
        print(f"Кота з ім'ям {name} не знайдено.")

# Видалення документів (Delete)
def delete_cat_by_name(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Кіт з ім'ям {name} видалений.")
    else:
        print(f"Кота з ім'ям {name} не знайдено.")

def delete_all_cats():
    result = collection.delete_many({})
    print(f"Видалено {result.deleted_count} котів.")

# Основна функція для тестування
if __name__ == "__main__":
    # Створення кількох котів
    create_cat("Barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    create_cat("Murzik", 5, ["любит м'ясо", "активний", "чорний"])

    # Читання всіх котів
    print("\nВсі коти в базі даних:")
    read_all_cats()

    # Читання кота за ім'ям
    print("\nІнформація про кота 'Barsik':")
    read_cat_by_name("Barsik")

    # Оновлення віку кота
    print("\nОновлення віку кота 'Barsik':")
    update_cat_age("Barsik", 4)

    # Додавання нової характеристики
    print("\nДодавання характеристики 'любить молоко' до кота 'Barsik':")
    add_feature_to_cat("Barsik", "любить молоко")

    # Видалення кота за ім'ям
    print("\nВидалення кота 'Murzik':")
    delete_cat_by_name("Murzik")

    # Видалення всіх котів
    print("\nВидалення всіх котів:")
    delete_all_cats()
