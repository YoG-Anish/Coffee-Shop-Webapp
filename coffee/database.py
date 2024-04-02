import sqlite3
import streamlit as st

# Function to create a SQLite connection
def create_connection():
    try:
        conn = sqlite3.connect('accounting.db')
        return conn
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    return None


def dump(conn, username, password, email):
    cursor = conn.cursor()
    # cursor.execute('''INSERT INTO IF NOT EXISTS user(username, password, email)
    #                     VALUES (?,?,?)''', (username, password, email))
    cursor.execute('''INSERT INTO user(username, password, email)
                        SELECT ?, ?, ?
                        WHERE NOT EXISTS (SELECT 1 FROM user WHERE username = ?)''', (username, password, email, username))
    conn.commit()
    return True

# Function to create tables if they don't exist
def create_tables(conn):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS user(
                                username TEXT UNIQUE NOT NULL,
                                password TEXT NOT NULL,
                                email TEXT NOT NULL         
                            )''')
            conn.commit()
            dump(conn, 'admin', 'admin', 'admin@example.com')
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
        

# def insert_user(conn):
#     cursor = conn.cursor()
#     cursor.execute('''INSERT INTO user(username,password, email) 
#                    VALUES ('admin', 'admin', 'admin@example.com')''')
#     conn.commit()





