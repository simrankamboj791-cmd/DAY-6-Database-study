import sqlite3

# Connect to database
connection = sqlite3.connect("myapp.db")

# Create cursor
cursor = connection.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# Create expenses table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    date TEXT NOT NULL,
    user_id INTEGER
)
""")

# Insert sample users
cursor.execute("""
INSERT INTO users (name, email)
VALUES ('Aditi Sharma', 'aditi@email.com')
""")

cursor.execute("""
INSERT INTO users (name, email)
VALUES ('Rahul Verma', 'rahul@email.com')
""")

# Insert sample expenses
cursor.execute("""
INSERT INTO expenses (amount, category, date, user_id)
VALUES (500, 'Food', '2026-07-23', 1)
""")

cursor.execute("""
INSERT INTO expenses (amount, category, date, user_id)
VALUES (1000, 'Travel', '2026-07-23', 1)
""")

cursor.execute("""
INSERT INTO expenses (amount, category, date, user_id)
VALUES (300, 'Books', '2026-07-23', 2)
""")

# Save changes
connection.commit()

# Close database
connection.close()

print("Database created and sample data inserted successfully!")