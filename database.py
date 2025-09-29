import sqlite3
import os

def init_db():
    if os.path.exists('test.db'):
        os.remove('test.db')
    
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')
    
	# mails

    test_users = [
        (1, 'admin', 'admin@example.com'),
        (2, 'user1', 'user1@test.com'),
        (3, 'test', 'test@domain.com'),
        (4, 'alice', 'alice@wonderland.com'),
        (5, 'bob', 'bob@builder.com'),
		(6, 'user15', 'mail@mainmail.en'),
		(7, 'deepseek', 'deepseek@dpsk.com'),
		(8, 'github', 'github@git.com')
    ]
    
    cursor.executemany('INSERT INTO users VALUES (?, ?, ?)', test_users)
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect('test.db')
    conn.row_factory = sqlite3.Row
    return conn
