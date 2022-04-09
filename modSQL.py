#modSQL
import sqlite3
from sqlite3 import Error

#("ddi.db")
def close_connection(conn):
    return conn.close()

def create_connection(db_file = "ddi.db"):
    conn = None
    try:
        db_conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return db_conn

def create_tables(conn):

    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS MESSAGES")

    sql = 'CREATE TABLE MESSAGES(id integer PRIMARY KEY, msg text NOT NULL,status char(1) DEFAULT 1)'

    cursor.execute(sql)

    conn.commit()

    return -1


def insert_msg(conn, message, table ='MESSAGES'):
    cur = conn.cursor()

    if message:
        #sql3 = 'INSERT INTO MESSAGES (msg) VALUES ("'+message+'")'
        #sql3 = 'INSERT INTO MESSAGES (msg) VALUES (?)'
        #cur.execute(sql3, (message,))
        cur.execute('INSERT INTO MESSAGES (msg) VALUES (?)', (message,))
    else:
        sql3 = 'INSERT INTO MESSAGES (msg) VALUES ("test6"), ("test7"), ("test8")'
        cur.execute(sql3)
    conn.commit()
    return -1

def select_msg(conn, sql):
    if sql:
        records = conn.execute(sql).fetchall()
        return records

    else:
        return -1


print("Module SQL: " + __name__)
if __name__ == '__main__':
    create_connection("ddi.db")
