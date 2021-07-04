import sqlite3
import sys
import datetime


enteries = int(sys.argv[1])


def get_week_num(date : datetime.date):
  
  date = str(date)
  date = date.split("-")
  
  date_obj = datetime.date(
    int(date[0]),
    int(date[1]),
    int(date[2])
    )
  
  week_num = date_obj.isocalendar()[1]
  return week_num 

con = sqlite3.connect("tasks.db")
cur = con.cursor()

for entry in range(enteries):
  
  for row in cur.execute("SELECT MAX(SerialNum) FROM tasks"):
    print("Last Serial Num : ",row[0])
  
 
  SerialNum = int(input("SerialNum: "))
  taskname= input("taskname: ")
  type = input("type long;short :  ")
  priorityType = input("priorityType :  ")
  dateOfEntry = datetime.date.today()
  weekNo = get_week_num(dateOfEntry)
  DateCompletion = None 
  description = input("Description:  ")
  status = "pending"
  subject = input("Subject: ")
  
  data_entry = [SerialNum, taskname, type, priorityType.upper(), description, dateOfEntry, weekNo, DateCompletion, status,subject.upper()]
  data_entry = tuple(data_entry)
  
  sql = "INSERT INTO tasks VALUES (?,?,?,?,?,?,?,?,?,?)"
  
  cur.execute(sql, data_entry)
  
  
con.commit()
  