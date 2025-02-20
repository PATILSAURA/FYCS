import sqlite3

def main():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # Create a table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
    """)

    # Insert records
    students = [
        ("Alice", 20, "A"),
        ("Bob", 22, "B"),
        ("Charlie", 21, "A"),
    ]
    cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", students)

    # Commit changes
    conn.commit()

    # Select and display all rows
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\nStudent Records:")
    for row in rows:
        print(row)

    # Close connection
    conn.close()

if __name__ == "__main__":
    main()
