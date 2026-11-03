import sqlite3
from contextlib import closing
from pathlib import Path

# Resolve files relative to this script, not the current working directory.
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "journey.db"
SQL_PATH = BASE_DIR / "db_setup.sql"


def setup_database():
    """Initializes the database using the SQL file."""
    sql_script = SQL_PATH.read_text()

    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.executescript(sql_script)
        conn.commit()
    print("✅ Database ready.")


def add_user(name, email):
    """Adds a new user to the database."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        try:
            conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
            print(f"✅ Added user: {name}")
        except sqlite3.IntegrityError as e:
            if "UNIQUE" in str(e):
                print(f"❌ Error: User with email {email} already exists.")
            else:
                print(f"❌ Error: Could not add user ({e}).")


def list_users():
    """Retrieves and prints all users from the database."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        rows = conn.execute("SELECT id, name, email FROM users").fetchall()

    print("\n--- Registered Users ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Email: {row[2]}")


if __name__ == "__main__":
    # Safe to run every time: the SQL script only creates/seeds what's missing,
    # so a half-built database gets repaired on the next run.
    setup_database()

    # Add a new user via Python
    add_user("Charlie", "charlie@example.com")

    # List all users
    list_users()
