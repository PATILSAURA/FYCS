import mysql.connector

# Establish the connection
try:
    conn = mysql.connector.connect(
        host='localhost',        # Replace with your MySQL host
        user='your_username',     # Replace with your MySQL username
        password='your_password', # Replace with your MySQL password
        database='your_database'  # Replace with your MySQL database
    )

    if conn.is_connected():
        print("Connected to MySQL database")

    cursor = conn.cursor()

    # ALTER TABLE - Add a new column
    alter_query = """
    ALTER TABLE employees
    ADD COLUMN birthdate DATE;
    """

    cursor.execute(alter_query)
    print("Table altered successfully")

    # Commit changes
    conn.commit()

except mysql.connector.Error as e:
    print("Error:", e)

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("MySQL connection closed")
