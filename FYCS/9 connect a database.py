import sqlite3

def update_and_show():
    # Connect to (or create) the database
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # Create a sample table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        age INTEGER)''')

    # Insert sample data
    cursor.execute("DELETE FROM users")  # Clear table for demonstration
    sample_data = [(1, 'Alice', 30), (2, 'Bob', 25), (3, 'Charlie', 35)]
    cursor.executemany("INSERT INTO users (id, name, age) VALUES (?, ?, ?)", sample_data)
    conn.commit()

    print("Before update:")
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)

    # Update a specific column value
    user_id = 2
    new_age = 28
    cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))
    conn.commit()

    print("\nAfter update:")
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)

    # Close connection
    conn.close()

if __name__ == "__main__":
    update_and_show()
