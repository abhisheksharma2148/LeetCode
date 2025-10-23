-- Write your PostgreSQL query statement below
select department, employee, salary from
(select d.name as department , e.name as employee, e.salary as salary,
dense_rank() over (partition by e.departmentId order by e.salary desc) as rnk
from department d 
right join employee e
on d.id = e.departmentId)
where rnk=1
