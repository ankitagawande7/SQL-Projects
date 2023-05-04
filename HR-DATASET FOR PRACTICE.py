import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="analysis")

mycursor=mydb.cursor()

mycursor.execute("show tables")
#mycursor.fetchall()
mycursor.execute("select * from hr11")

myresult=mycursor.fetchall()

l=[]
for i in myresult:
    l.append(list(i))
    
import numpy as np
array=np.array(l)
array   
 


array[1:10,] 
#select the candidate id  who are all from noida
sql="select candidata from hr11 where Location='Noida'"

mycursor.execute(sql)

myresult=mycursor.fetchall()

#2. find out the total count you want to relocate ='yes'
sql="select count(candidata) from hr11 where Candidate_relocate='yes'"
mycursor.execute(sql)

myresult=mycursor.fetchall()



l=[]
for i in myresult:
    l.append(list(i))
    
import numpy as np
array=np.array(l)
array   

   
#3.fine out total Percent.hike.expected.in.CTC
sql="select sum(Pecent_hike_expected_CTC) from hr11"
mycursor.execute(sql)
myresult=mycursor.fetchall()

#4.find out min and max Pecent.hike.expected.in.CTC
sql="select min(Pecent_hike_expected_CTC)from hr11"
mycursor.execute(sql)
myresult=mycursor.fetchall()

sql="select max(Pecent_hike_expected_CTC)from hr11"
mycursor.execute(sql)
myresult=mycursor.fetchall()

#5.find out the total employee has joined or not joined
sql="select count(candidata) from hr11 where Status='Joined'" 
mycursor.execute(sql) 
myresult=mycursor.fetchall()

sql="select count(candidata)from hr11 where Status='Not Joined'"


#6.find out total male and females are there
sql="select count(candidata)from hr11 where Gender='Female'"
mycursor.execute(sql)
myresult=mycursor.fetchall()

l=[]
for i in myresult:
    l.append(list(i))
    
import numpy as np
array=np.array(l)
array 

sql="select count(candidata)from hr11 where Gender='Male'" 
 
#7.find out the employee whose are directly coming
sql="select count(candidata)from hr11 where Candidate_Source='Direct'"
mycursor.execute(sql)
myresult=mycursor.fetchall()



#8.find out the employees youngest and oldest age
sql="select min(Age) from hr11"
mycursor.execute(sql)
myresult=mycursor.fetchall()

sql="select max(Age) from hr11"

#9.what is the average Duration.to.accept.offer
sql="select avg(Duration_to_accept_offer) from hr11"
mycursor.execute(sql)
myresult=mycursor.fetchall()



#10.find out the number of employee whose having notice period >30 ,<30 or = 30 days
sql="select count(candidata)from hr11 where Notice_period>=30"
mycursor.execute(sql)
myresult=mycursor.fetchall()

sql="select count(candidata)from hr11 where Notice_period<30"








