CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    select (
        select t.salary  from (
            select e.salary,dense_rank() over (order by e.salary desc) as rnk
            from employee e) t where rnk= N limit 1
        ) 

    
      
  );
END;
$$ LANGUAGE plpgsql;
