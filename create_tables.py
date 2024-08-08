import psycopg2

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)

# Створення курсора
cur = conn.cursor()

# Створення таблиці users
cur.execute("""
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
""")

# Створення таблиці status
cur.execute("""
CREATE TABLE status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);
""")

# Створення таблиці tasks
cur.execute("""
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER REFERENCES status(id),
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
""")

# Фіксація змін і закриття з'єднання
conn.commit()
cur.close()
conn.close()
