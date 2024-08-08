def create_cat(name, age, features):
    try:
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        collection.insert_one(cat)
        print(f"Кіт {name} доданий до бази даних.")
    except Exception as e:
        print(f"Помилка при додаванні кота: {e}")
