import mysql.connector

def count_rows(database_name, table_name, host='localhost', user='your_username', password='your_password'):
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )

        cursor = conn.cursor()

        # Query to count rows
        query = f"SELECT COUNT(*) FROM {table_name}"
        cursor.execute(query)

        # Fetch and print the row count
        row_count = cursor.fetchone()[0]
        print(f"Total rows in '{table_name}':", row_count)

        # Clean up
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print("Error:", err)

# Replace with your MySQL details
count_rows('your_database', 'your_table')
