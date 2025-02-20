import sqlite3

# Connect to SQLite (or create a new database if it doesn't exist)
conn = sqlite3.connect("example.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER,
                    grade TEXT
                )''')

# Insert some records
students_data = [
    (1, 'Alice', 20, 'A'),
    (2, 'Bob', 22, 'B'),
    (3, 'Charlie', 21, 'A'),
]

cursor.executemany("INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)", students_data)

# Commit the transaction
conn.commit()

# Retrieve and display all rows
cursor.execute("SELECT * FROM students")

print("Students Table:")
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()
