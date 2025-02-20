# Import the MySQL connector package
import mysql.connector

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(
        host='localhost',      # Change to your MySQL server host
        user='your_username',  # Change to your MySQL username
        password='your_password',  # Change to your MySQL password
        database='your_database'   # Change to your target database
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a query to show tables
        cursor.execute("SHOW TABLES")

        # Fetch and display the tables
        print("Tables in the database:")
        for table in cursor.fetchall():
            print(table[0])

except mysql.connector.Error as e:
    print("Error while connecting to MySQL", e)

finally:
    # Close the cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed")
