from faker import Faker
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

# Ініціалізація Faker
fake = Faker()

# Наповнення таблиці users
for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# Наповнення таблиці status
statuses = [('new',), ('in progress',), ('completed',)]
cur.executemany("INSERT INTO status (name) VALUES (%s)", statuses)

# Наповнення таблиці tasks
for _ in range(20):
    title = fake.sentence()
    description = fake.text()
    status_id = fake.random_int(min=1, max=3)
    user_id = fake.random_int(min=1, max=10)
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                (title, description, status_id, user_id))

# Фіксація змін і закриття з'єднання
conn.commit()
cur.close()
conn.close()
