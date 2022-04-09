import sqlite3
from sqlite3 import Error
import modSQL

#conn = None
#try:
#    conn = sqlite3.connect("ddi.db")
#except Error as e:
#    print(e)

conn = modSQL.create_connection("ddi.db")


#cursor = conn.cursor()

#cursor.execute("DROP TABLE IF EXISTS MESSAGES")
#sql = 'CREATE TABLE MESSAGES(id integer PRIMARY KEY, msg text NOT NULL,status char(1) DEFAULT 1)'
#sql2 = '''CREATE TABLE MESSAGES(
# id integer PRIMARY KEY,
# msg text NOT NULL,
# status char(1) DEFAULT 1
#)'''
#cursor.execute(sql)
#print("table created")
modSQL.create_tables(conn)

#cur = conn.cursor()
#sql3 = 'INSERT INTO MESSAGES (msg) VALUES ("test6"), ("test7"), ("test8")'
#cur.execute(sql3)
#conn.commit()
msg = "test9"

modSQL.insert_msg(conn, msg, "MESSAGES")

msg = ""
modSQL.insert_msg(conn, msg, "MESSAGES")

modSQL.insert_msg(conn, "test10")

#CREATE TABLE MESSAGES(id integer PRIMARY KEY, msg text NOT NULL,status char(1) DEFAULT 1)
#INSERT INTO MESSAGES (msg) VALUES ("test1")
#select * from MESSAGES


rows = modSQL.select_msg(conn, """select * from MESSAGES""")
for row in rows:
    print(row)

rows = modSQL.select_msg(conn, "select * from MESSAGES limit 3")
for row in rows:
    print(row)

#sql4 = """select * from MESSAGES"""

#rows = conn.execute(sql4).fetchall()
#for row in rows:
#    print(row)
modSQL.close_connection(conn)
#conn.close()
