import sqlite3

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO Publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher {name} is already in the database.")

def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute("INSERT INTO Magazines (name,publisher_id) VALUES (?,?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")


def add_subscriber(cursor, name, address):
    try:
        cursor.execute("SELECT * FROM Subscribers WHERE name = ? AND address = ?", (name, address))
        results = cursor.fetchall()
        if len(results) > 0:
            print(f"There was already a subscriber named {name}.")
            return
    
        cursor.execute("INSERT INTO Subscribers (name, address) VALUES (?,?)", (name, address))
    except sqlite3.IntegrityError:
        print(f"Subscriber {name} is already in the database.")


def purchase_subscription(cursor, subscriber, magazine, exp_date):
    try:
        cursor.execute("SELECT * FROM Subscribers WHERE name = ?", (subscriber,)) 
        results = cursor.fetchall()
        if len(results) > 0:
            subscriber_id = results[0][0]
        else:
            print(f"There was no subscriber named {subscriber}.")
            return
        cursor.execute("SELECT * FROM Magazines WHERE name = ?", (magazine,))
        results = cursor.fetchall()
        if len(results) > 0:
            magazine_id = results[0][0]
        else:
            print(f"There was no magazine named {magazine}.")
            return
        cursor.execute("INSERT INTO Subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, exp_date))
    except sqlite3.IntegrityError:
        print(f"{subscriber} is already subscribed to {magazine}.")

try:
    with  sqlite3.connect("../db/magazines.db") as conn:  
        print("Database created and connected successfully.")
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE)
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id))
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL)
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id))
        """)

        print("Tables created successfully.")

        add_publisher(cursor, 'Alice')  
        add_publisher(cursor, 'Bob')  
        add_publisher(cursor, 'Charlie')  

        add_magazine(cursor, 'Math 101', 1)
        add_magazine(cursor, 'English 101', 2)
        add_magazine(cursor, 'Chemistry 101', 3)

        add_subscriber(cursor, 'Alice', '123 Main St')
        add_subscriber(cursor, 'Bob', '456 Oak Ave')
        add_subscriber(cursor, 'Charlie', '789 Pine Rd')


        purchase_subscription(cursor, "Alice", "Math 101","2026-12-31")
        purchase_subscription(cursor, "Alice", "Chemistry 101","2026-06-01")
        purchase_subscription(cursor, "Bob", "Math 101", "2027-01-01")
        purchase_subscription(cursor, "Bob", "English 101", "2027-06-01")
        purchase_subscription(cursor, "Charlie", "English 101", "2027-06-01")

        conn.commit() 
        print("Sample data inserted successfully.")

        cursor.execute("SELECT * FROM subscribers;")
        results = cursor.fetchall()
        for row in results:
            print(row)

        cursor.execute("SELECT name FROM magazines ORDER BY name;")
        results = cursor.fetchall()
        for row in results:
            print(row)

        cursor.execute("SELECT * FROM publishers p JOIN magazines m ON p.publisher_id = m.publisher_id where p.name = 'Alice';")
        results = cursor.fetchall()
        for row in results:
            print(row)


except sqlite3.Error as e:
    print(f"An error occurred while connecting to the database: {e}")