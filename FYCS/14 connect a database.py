import sqlite3

# Connect to SQLite (or create database if it doesn't exist)
conn = sqlite3.connect("hospital_db.db")
cursor = conn.cursor()

# Exercise 1: Create Hospital and Doctor Tables
cursor.execute('''CREATE TABLE IF NOT EXISTS Hospital (
    hospital_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Doctor (
    doctor_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    specialty TEXT NOT NULL,
    salary REAL NOT NULL,
    experience INTEGER NOT NULL,
    hospital_id INTEGER,
    FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id)
)''')

conn.commit()

def insert_sample_data():
    cursor.executemany('''INSERT INTO Hospital (hospital_id, name, location) VALUES (?, ?, ?)''', [
        (1, 'City Hospital', 'New York'),
        (2, 'Green Valley Hospital', 'California'),
        (3, 'Sunrise Clinic', 'Texas')
    ])

    cursor.executemany('''INSERT INTO Doctor (doctor_id, name, specialty, salary, experience, hospital_id) VALUES (?, ?, ?, ?, ?, ?)''', [
        (1, 'Dr. John', 'Cardiology', 150000, 10, 1),
        (2, 'Dr. Smith', 'Neurology', 180000, 8, 2),
        (3, 'Dr. Jane', 'Orthopedics', 130000, 4, 1),
        (4, 'Dr. Emily', 'Pediatrics', 140000, 6, 3),
        (5, 'Dr. Mark', 'Cardiology', 155000, 12, 2)
    ])
    conn.commit()

# Uncomment to insert sample data (only run once to avoid duplicate entries)
# insert_sample_data()

# Exercise 2: Fetch Hospital and Doctor Information
def fetch_hospital_doctor_info(hospital_id, doctor_id):
    cursor.execute('''SELECT * FROM Hospital WHERE hospital_id = ?''', (hospital_id,))
    print("Hospital Info:", cursor.fetchone())

    cursor.execute('''SELECT * FROM Doctor WHERE doctor_id = ?''', (doctor_id,))
    print("Doctor Info:", cursor.fetchone())

# Exercise 3: Get list of doctors by specialty and salary
def get_doctors_by_specialty_and_salary(specialty, min_salary):
    cursor.execute('''SELECT * FROM Doctor WHERE specialty = ? AND salary >= ?''', (specialty, min_salary))
    for doctor in cursor.fetchall():
        print(doctor)

# Exercise 4: Get list of doctors from a given hospital
def get_doctors_by_hospital(hospital_id):
    cursor.execute('''SELECT * FROM Doctor WHERE hospital_id = ?''', (hospital_id,))
    for doctor in cursor.fetchall():
        print(doctor)

# Exercise 5: Update doctor experience
def update_doctor_experience(doctor_id, new_experience):
    cursor.execute('''UPDATE Doctor SET experience = ? WHERE doctor_id = ?''', (new_experience, doctor_id))
    conn.commit()
    print("Updated experience for doctor_id:", doctor_id)

# Exercise 6: Delete doctors with experience less than 5 years
def delete_doctors_with_low_experience():
    cursor.execute('''DELETE FROM Doctor WHERE experience < 5''')
    conn.commit()
    print("Deleted doctors with less than 5 years of experience")

# Example usage:
fetch_hospital_doctor_info(1, 1)
get_doctors_by_specialty_and_salary('Cardiology', 150000)
get_doctors_by_hospital(1)
update_doctor_experience(3, 7)
delete_doctors_with_low_experience()

# Close connection
conn.close()
