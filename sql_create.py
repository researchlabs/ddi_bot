import sqlite3
from sqlite3 import Error
import modSQL

#conn = modSQL.create_connection("ddi.db")
conn = modSQL.create_connection()
modSQL.create_tables(conn)
modSQL.close_connection(conn)


#msg = "test9"
#modSQL.insert_msg(conn, msg, "MESSAGES")
#msg = ""
#modSQL.insert_msg(conn, msg, "MESSAGES")
#modSQL.insert_msg(conn, "test10")
#modSQL.insert_msg(conn, 'test11')

#CREATE TABLE MESSAGES(id integer PRIMARY KEY, msg text NOT NULL,status char(1) DEFAULT 1)
#INSERT INTO MESSAGES (msg) VALUES ("test1")
#select * from MESSAGES


###rows = modSQL.select_msg(conn, """select * from MESSAGES""")
###for row in rows:
###    print(row)

###rows = modSQL.select_msg(conn, "select * from MESSAGES limit 3")
###for row in rows:
###    print(row)

#sql4 = """select * from MESSAGES"""
