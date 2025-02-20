import mysql.connector

def update_column(database, table, column, new_value, host='localhost', user='your_username', password='your_password'):
    try:
        # Establish connection to MySQL
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            cursor = connection.cursor()

            # SQL query to update all rows in a column
            update_query = f"""
            UPDATE {table}
            SET {column} = %s
            """

            # Execute update query
            cursor.execute(update_query, (new_value,))

            # Commit changes
            connection.commit()

            print(f"Updated all rows in '{column}' to '{new_value}'")

    except mysql.connector.Error as error:
        print("Error updating column:", error)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

# Example usage
update_column(database='test_db', table='employees', column='salary', new_value=50000, user='root', password='yourpassword')
