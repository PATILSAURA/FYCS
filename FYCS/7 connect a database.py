import sqlite3

def create_table():
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

def insert_user(name, age):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Insert user data
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

    conn.commit()
    print("User inserted successfully!")
    conn.close()

def main():
    create_table()

    print("Enter user details to insert into the database:")
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    insert_user(name, age)

if __name__ == "__main__":
    main()
