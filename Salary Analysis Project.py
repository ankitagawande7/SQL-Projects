import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",
                             password="root",database="test") 
mycursor=mydb.cursor()
mycursor.execute("show tables")
mycursor.execute("select * from jobs")

mycursor.execute("select * from companies")
myresult=mycursor.fetchall()

mycursor.execute("delete from data_company_name where company='company_name'")
mycursor.execute("commit")

mycursor.execute("delete from ds_salaries where jobtitle='job_title'")

l=[]
for i in myresult:
    l.append(list(i))
import numpy as np
main=np.array(l)    
main

#Q(1)-- What is the Average Salary for All The Jobs in the Dataset?
sql="select avg(salary) as avg_salary from jobs"
mycursor.execute(sql)

myresult=mycursor.fetchall()

#Q(2)-- What is the Highest Salary in the dataset & What job Role does it Currespond too?
sql="select jobtitle,max(salary) as highest_salary from jobs\
    group by jobtitle order by highest_salary desc limit 1"
mycursor.execute(sql)
myresult=mycursor.fetchall() 

#Q(3)--what is the Average salary for data scientist in US?
sql="select avg(salary) from jobs where jobtitle='Data Scientist' and employee_residence='US'"

#Q(4)--What are the Number of jobs Available for each job title?
sql="select jobtitle,count(*) as Number_of_jobs from jobs group by jobtitle"

#Q(5)--What is the Total Salary Paid For All data Analyst Jobs in DE?
sql="select sum(salary) as Total_salary from jobs where jobtitle='Data Analyst' and company_location='DE'"
mycursor.execute(sql)
myresult=mycursor.fetchall() 


l=[]
for i in myresult:
    l.append(list(i))
import numpy as np
main=np.array(l)    
main

#Q(6)--What are the Top 5 Highest Paying Job Titles and Their Curresponding Average salaries?
sql="select jobtitle, avg(salary) as average_salary from jobs group by jobtitle order by average_salary desc limit 5 "

#Q(7)--What are the numbers of jobs available in each compay location?
sql="select company_location,count(*) as number_of_job from ds_salaries group by company_location"

#Q(8)--Top 3 job Titles that have most jobs available in dataset?
sql="select jobtitle,count(jobtitle) as number_of_job from jobs group by jobtitle order by number_of_job desc limit 3 "

#Q(9)--what is the Average salary for ML Engineer in US?
sql="select jobtitle,company_location, avg(salary) as average_salary from jobs where jobtitle='ML Engineer' and company_location='US'"

#Q(10)--What are the Top 5 Cities with the Highest Average Salaries?
sql="select company_location, avg(salary) as average_salary from jobs group by company_location order by average_salary desc limit 5"

#Q(11)--What is the Average salary for each job title and what are the Total number of jobs avalilable for each job title?
sql="select jobtitle,avg(salary) as average_salary, count(*) as Number_of_jobs from jobs group by jobtitle"
mycursor.execute(sql)
myresult=mycursor.fetchall() 


l=[]
for i in myresult:
    l.append(list(i))
import numpy as np
main=np.array(l)    
main

#Q(12)--What are the top 5 job Titles With The Highest Total Salaries and what are the No. of Jobs
#       Available for Each Job Title?
sql="select jobtitle, max(salary) as highest_salary, count(*) as Number_of_jobs from jobs group by jobtitle order by highest_salary desc limit 5"
mycursor.execute(sql)
myresult=mycursor.fetchall() 


l=[]
for i in myresult:
    l.append(list(i))
import numpy as np
main=np.array(l)    
main
#Q(13)--Which are the Top 5 Locations with Highest total salary Which are the total number of jobs available for each location?
sql="select company_location,max(salary) as highest_salary,count(jobtitle) from jobs\
    group by company_location order by highest_salary desc limit 5"

#Q(14)--Which are Average salary for each job title in each location and Which are the total number of jobs available for All job title in each location?
sql="select jobtitle,company_location,avg(salary) as average_salary,count(*) as Numb_of_jobs from jobs \
    group by jobtitle,company_location"

#Q(15)--How much is the average salary for each job title in each location,and 
#        what are the percentage of jobs for each job title in each location?
sql="select jobtitle,company_location,avg(salary) as average_salary,(count(*) *100/ (select count(*) from jobs )) as percentage from jobs\
    group by jobtitle,company_location "


#Q(16)--What is the Avg salary for each job title and percentage of jobs for each job title?
sql="select jobtitle,avg(salary) as average_salary,(count(*) * 100/ (select count(*)from jobs))\
    as percentage from jobs group by jobtitle "

#Q(17)--What are the Top 5 job Titles with  Highest Average Salary in each location?
sql="select jobtitle,company_location, avg(salary) as average_salary from jobs where jobtitle in (select jobtitle from jobs group by jobtitle) group by jobtitle,company_location order by average_salary desc limit 5"

mycursor.execute(sql)
myresult=mycursor.fetchall() 


l=[]
for i in myresult:
    l.append(list(i))
import numpy as np
main=np.array(l)    
main
 
mycursor.execute("alter table ds_salaries rename jobs")
mycursor.execute("alter table data_company_name rename companies")
            


#Q(18)--Which are the Top 5 Job Titles with the Highest Salaries,and what is the company name that offers highest salaries for each job title?

sql="select jobtitle,max(salary) as highest_salary,company_name from jobs\
    inner join companies on jobs.id=companies.id group by jobtitle order by highest_salary desc limit 5"
   
         

#Q(19)--Total no. of jobs available for each job title and what is the company name that offers highest salary for each job title?
sql="select jobtitle,count(*) as num_of_jobs,max(salary),\
    company_name from jobs inner join companies on jobs.id=companies.id\
    where salary=(select max(salary)from jobs where jobtitle=jobtitle)group by jobtitle,company_name"

#Q(20)--Top 5 cities with highest average salaries & name of companies that offers highest salaries for each city?####
sql="SELECT company_location, AVG(salary) AS average_salary, company_name FROM jobs\
    INNER JOIN companies ON jobs.id = companies.id \
    GROUP BY company_location ORDER BY average_salary DESC LIMIT 5"
     
mycursor.execute(sql)

myresult=mycursor.fetchall() 


l=[]
for i in myresult:
    l.append(list(i))
import numpy as np
main=np.array(l)    
main
#Q(21)--Avg salary for each job title in each company & Rank Of each job title within each company based on average salary?
sql="SELECT jobtitle,company_name,AVG(salary) as avg_salary, \
    RANK()OVER (partition by company_name ORDER BY AVG(salary)DESC)AS salary_rank from jobs \
        INNER JOIN companies on jobs.id=companies.id GROUP BY jobtitle,company_name"
        
 #partition---It is used to define which Record To make part of the window frame associate with each record of the result.       
#Rank--Assign the No. to Each Row within the partition of An Output


#Q(22)--which are the top 5 companies with highest avg salary for data scientist & what is rank of each company based on avg salary?
sql="SELECT jobtitle,company_name,AVG(salary) as avg_salary,\
    RANK()OVER (ORDER BY AVG(salary)DESC)AS salary_rank from jobs \
        INNER JOIN companies on jobs.id=companies.id WHERE jobtitle='Data Scientist'\
            GROUP by company_name ORDER BY avg_salary DESC LIMIT 5"






