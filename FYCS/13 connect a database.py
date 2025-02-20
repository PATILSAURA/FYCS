import os
import time

def backup_mysql_database(host, user, password, database_name, backup_dir):
    # Ensure backup directory exists
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Create a timestamped backup filename
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    backup_file = f"{backup_dir}/{database_name}_backup_{timestamp}.sql"

    # Construct the mysqldump command
    dump_command = f"mysqldump -h {host} -u {user} -p{password} {database_name} > {backup_file}"

    # Execute the command
    os.system(dump_command)

    print(f"Backup completed: {backup_file}")

if __name__ == "__main__":
    # MySQL connection details
    host = "localhost"
    user = "your_username"
    password = "your_password"
    database_name = "your_database"

    # Directory to save backups
    backup_dir = "./backups"

    backup_mysql_database(host, user, password, database_name, backup_dir)
