import sqlite3
import sys

conn  = sqlite3.connect("tasks.db")
cur = conn.cursor()

sql = sys.argv[1]

cur.execute(sql)

conn.commit()