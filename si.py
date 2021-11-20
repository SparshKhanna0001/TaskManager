import sqlite3
import sys


conn = sqlite3.connect("tasks.db")
cur = conn.cursor()

type_of_opr = sys.argv[1] 

if type_of_opr.lower() == "all":
  
  for row in cur.execute("SELECT * FROM tasks"):
    #print(f"""(SerialNum = {row[0]}, taskname={row[1]},type={row[2]},Subject={row[3]}, priorityType={row[4]}, description={row[5]},Status={row[6]},DateOfEntry = {row[7]}, weeknum={row[8]},DateCompletion={row[9]},estimatedType = {row[10]})""")
    print(f'''(SerialNum = {row[0]}''')
    print(f'''taskname={row[1]}''')
    print(f'''type={row[2]}''')
    print(f'''Subject={row[3]}''')
    print(f'''priorityType={row[4]}''')
    print(f'''description={row[5]}''')
    print(f'''Status={row[6]}''')
    print(f'''DateOfEntry = {row[7]}''')
    print(f'''weeknum={row[8]}''')
    print(f'''DateCompletion={row[9]}''')
    print(f'''estimatedType = {row[10]})''')
    print('\n')

elif type_of_opr.lower() == "pen":
  
  for row in cur.execute("SELECT * FROM tasks WHERE Status == 'pending'"):
    #print(f"""(SerialNum = {row[0]}, taskname={row[1]},type={row[2]},Subject={row[3]}, priorityType={row[4]}, description={row[5]},Status={row[6]},DateOfEntry = {row[7]}, weeknum={row[8]},DateCompletion={row[9]},estimatedType = {row[10]})""")
    print(f'''(SerialNum = {row[0]}''')
    print(f'''taskname={row[1]}''')
    print(f'''type={row[2]}''')
    print(f'''Subject={row[3]}''')
    print(f'''priorityType={row[4]}''')
    print(f'''description={row[5]}''')
    print(f'''Status={row[6]}''')
    print(f'''estimatedType = {row[10]})''')
    
elif type_of_opr.lower() == "done":
  
  for row in cur.execute("SELECT * FROM tasks WHERE Status == 'done'"):
    print(f"""(SerialNum = {row[0]}, taskname={row[1]},type={row[2]},Subject={row[3]}, priorityType={row[4]}, description={row[5]},Status={row[6]},DateOfEntry = {row[7]}, weeknum={row[8]},DateCompletion={row[9]},estimatedType = {row[10]})""")
  
conn.commit()
