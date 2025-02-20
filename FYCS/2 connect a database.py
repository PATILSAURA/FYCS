import mysql.connector

# Establish connection to MySQL server
try:
    connection = mysql.connector.connect(
        host='localhost',       # Change if your MySQL server is on a different host
        user='your_username',    # Replace with your MySQL username
        password='your_password' # Replace with your MySQL password
    )

    if connection.is_connected():
        print("Successfully connected to MySQL server")

        # Fetch and print MySQL version
        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print("MySQL Database Version:", version[0])

        # Create a new database
        cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
        print("Database 'test_db' created successfully (if not existed)")

        # Clean up
        cursor.close()
        connection.close()

except mysql.connector.Error as err:
    print("Error:", err)
# Import MySQL connector
import mysql.connector

# Connect to MySQL server
try:
    connection = mysql.connector.connect(
        host='localhost',       # Change to your MySQL server host
        user='your_username',   # Replace with your MySQL username
        password='your_password' # Replace with your MySQL password
    )

    if connection.is_connected():
        print("Connected to MySQL server")

        # Create a cursor object
        cursor = connection.cursor()

        # Execute the SHOW DATABASES command
        cursor.execute("SHOW DATABASES")

        print("Databases available:")
        for db in cursor:
            print(db[0])

        # Close cursor and connection
        cursor.close()
        connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
