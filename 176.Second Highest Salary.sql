select (select distinct salary as SecondHighestSalary from employee 
order by salary 
limit 1 offset 1)
