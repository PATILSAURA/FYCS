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
