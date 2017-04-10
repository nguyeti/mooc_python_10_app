import sqlite3 as sql

def connect():
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                title text UNIQUE,\
                author text,\
                year integer,\
                isbn integer UNIQUE)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book (title, author, year, isbn) values \
                (?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def drop_db():
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS book")
    conn.close()

def search(title="", author="", year="", isbn=""):
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book where title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book where id=?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author,year,isbn):
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book set title=?,\
                                 author=?,\
                                 year=?,\
                                 isbn=? where id=?", (title, author,year,isbn,id))
    conn.commit()
    conn.close()

# drop_db()
# connect()
# insert("The Sun","John Smith",1918,913123131)
# insert("The Moon","John Smith",1918,913123132)
# insert("The Earth","John Smith",1918,913123133)
