import sqlite3

def create_table():
    con=sqlite3.connect("myDB.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, qtd INTEGER, price REAL)")
    con.commit()
    con.close()

def insert(item,qtd,price):
    con=sqlite3.connect("myDB.db")
    cur=con.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,qtd,price))
    con.commit()
    con.close()

def select_store():
    con=sqlite3.connect("myDB.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    con.close()
    return rows

def delete(item):
    con=sqlite3.connect("myDB.db")
    cur=con.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    con.commit()
    con.close()

def update(item,qtd,price):
    con=sqlite3.connect("myDB.db")
    cur=con.cursor()
    cur.execute("UPDATE store SET qtd=?, price=? WHERE item=?",(qtd,price,item))
    con.commit()
    con.close()

#create_table()
#insert("coffe", 10, 5)
#insert("chocolate",5,20)
delete("coffe")
update("chocolate",2,2)
print(select_store())