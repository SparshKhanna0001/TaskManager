# TaskManager
Add, view and manage tasks basically a database 

##Way to use different programs:-
* ai.py : (add tasks) (number of enteries)
* si.py : (show tasks)  (all pen done) 
* up.py : (mark done tasks) (criteria) (value)
* cm.py : (pass sql commands to db) (sql command) 


* tasks.db : database with relation tasks
    * tasks : relation 
        * schema: (SerialNum INT NOT NULL UNIQUE, taskname VARCHAR(150) NOT NULL, type VARCHAR(5) NOT NULL, Subject VARCHAR(150) NO T NULL, Priority VARCHAR(100), description VARCHAR (1000), Status VARCHAR(8) NOT NULL, DateOfEntry DA TE, weeknum INT(2), DateCompletion DATE, estimatedTime INT)
