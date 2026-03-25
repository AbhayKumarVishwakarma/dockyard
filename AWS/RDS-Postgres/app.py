import psycopg2

conn = psycopg2.connect(
    host="test.amazonaws.com",
    database="postgres",
    user="postgres",
    password="password",
    port=5432
)

cur = conn.cursor()

# Create a table
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE
    )
''')
print("Table created successfully.")


# Insert a record
cur.execute(
    "INSERT INTO users (name, email) VALUES (%s, %s)",
    ("John Doe", "john.doe@example.com"),
    # ("Jane Smith", "jane.smith@example.com")
)
print("Records inserted successfully.")

conn.commit()


# Query the table
cur.execute('SELECT * FROM users')

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()