# Write your MySQL query statement below

# select e1 from employee e1 

# group by and sort well do

# select * from employee GROUPBY(salary) limit 2 where ;

SELECT MAX(salary) 
AS SecondHighestSalary
FROM Employee 
WHERE salary 
NOT IN ( 
    SELECT MAX(salary) 
    FROM Employee)




# select
# (select distinct Salary 
# from Employee order by salary desc 
# limit 1 offset 1) 
# as SecondHighestSalary;
