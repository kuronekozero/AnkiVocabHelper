import sqlite3
from datetime import datetime

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('../gui/words.db')  # создает файл базы данных с именем 'words.db'
        return conn
    except Exception as e:
        print(e)

def create_table(conn):
    try:
        sql = '''CREATE TABLE IF NOT EXISTS words (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    word TEXT NOT NULL,
                    frequency REAL,
                    date_added TEXT DEFAULT '01-01-1970'
                );'''
        conn.execute(sql)
    except Exception as e:
        print(e)

def delete_word(conn, word):
    sql = '''DELETE FROM words WHERE word = ?'''
    cur = conn.cursor()
    cur.execute(sql, (word,))
    conn.commit()

def add_word(conn, word, frequency):
    word = word.lower()
    sql = '''INSERT INTO words(word, frequency, date_added) VALUES(?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, (word, float(frequency), datetime.now().strftime("%d-%m-%Y")))
    conn.commit()

def add_column(conn):
    try:
        sql = '''ALTER TABLE words ADD COLUMN date_added TEXT;'''
        conn.execute(sql)
    except Exception as e:
        print(e)

def column_exists(conn, column_name):
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info(words)")
    return any(row[1] == column_name for row in cur.fetchall())

def get_all_words(conn):
    sql = '''SELECT id, word, frequency, date_added FROM words ORDER BY frequency DESC'''
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def update_word_frequency(conn, word, frequency):
    sql = '''UPDATE words SET frequency = ? WHERE word = ?'''
    cur = conn.cursor()
    cur.execute(sql, (frequency, word))
    conn.commit()

def word_exists(conn, word):
    word = word.lower()
    sql = '''SELECT * FROM words WHERE word = ?'''
    cur = conn.cursor()
    cur.execute(sql, (word,))
    return cur.fetchone() is not None

def main():
    conn = create_connection()

    if conn is not None:
        create_table(conn)
    else:
        print("Error! Couldn't connect to Data Base.")

if __name__ == '__main__':
    main()
