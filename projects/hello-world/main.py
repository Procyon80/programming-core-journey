import sqlite3
import os

def setup_database():
    """Initializes the database using the SQL file."""
    conn = sqlite3.connect('journey.db')
    cursor = conn.cursor()

    with open('db_setup.sql', 'r') as f:
        sql_script = f.read()

    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")

def add_user(name, email):
    """Adds a new user to the database."""
    try:
        conn = sqlite3.connect('journey.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()
        print(f"✅ Added user: {name}")
    except sqlite3.IntegrityError:
        print(f"❌ Error: User with email {email} already exists.")

def list_users():
    """Retrieves and prints all users from the database."""
    conn = sqlite3.connect('journey.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    rows = cursor.fetchall()
    conn.close()

    print("\n--- Registered Users ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Email: {row[2]}")

if __name__ == "__main__":
    # Setup the DB if it doesn't exist
    if not os.path.exists('journey.db'):
        setup_database()

    # Add a new user via Python
    add_user("Charlie", "charlie@example.com")

    # List all users
    list_users()
