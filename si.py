import sqlite3
import sys


conn = sqlite3.connect("tasks.db")
cur = conn.cursor()

type_of_opr = sys.argv[1] 
schema = "(Taskname varchar, type of task; long/short, priority, Date of entry, week num, date of completion, description)"
print(schema)

if type_of_opr.lower() == "all":
  
  for row in cur.execute("SELECT * FROM tasks"):
    print(row)

elif type_of_opr.lower() == "pen":
  
  for row in cur.execute("SELECT * FROM tasks WHERE Status == 'pending'"):
    print(row)
    
elif type_of_opr.lower() == "done":
  
  for row in cur.execute("SELECT * FROM tasks WHERE Status == 'done'"):
    print(row)
  
conn.commit()
