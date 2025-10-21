select c.name as Customers 
from orders o 
right join customers c 
on o.customerId = c.id 
where o.customerId is null
