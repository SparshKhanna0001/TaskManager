import sys
import sqlite3
import datetime

conn = sqlite3.connect("tasks.db")
cur = conn.cursor()

criteria = sys.argv[1]      #ex: serialnum, subject 
value = sys.argv[2]


def validation_func(argv,valid_list,excp):
   
  argv_valid = True
  if argv not in valid_list:
    raise Exception (excp)
''
validation_func(criteria,["Subject","SerialNum","taskname"],"Invalid type!\nValid types:-\n\tFor bulk use:Subject\n\tFor single use: taskname, SerialNum")

date_today = datetime.date.today()

cur.execute(f"""UPDATE tasks SET Status='done', DateCompletion='{date_today}' WHERE {criteria} == '{value}'""")

conn.commit()
