import sqlite3

def create():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (\
                 id INTEGER PRIMARY KEY AUTOINCREMENT,\
                 item TEXT UNIQUE,\
                 quantity INTEGER,\
                 price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store (item,quantity,price) VALUES (?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    #for v in cur.execute("SELECT * FROM store"):
    #    print(v)
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?", (item,))
    conn.commit()
    conn.close()

def update(quantity,item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ? WHERE item = ?", (quantity, item))
    conn.commit()
    conn.close()

def drop_table(name):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS " + name )
    conn.close()

drop_table('store')
create()
insert('car',1,123.1)
print(view())
