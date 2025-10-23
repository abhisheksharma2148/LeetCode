-- Write your PostgreSQL query statement below
select department, employee, salary from (
select d.name as department, e.name as employee, e.salary as salary,
dense_rank() over (partition by e.departmentId order by salary desc) as rnk
from employee e
left join department d
on e.departmentId = d.id
)
where rnk <=3
