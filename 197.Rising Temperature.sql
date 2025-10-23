-- Write your PostgreSQL query statement below
select id from (
    select id,recordDate-lag(recordDate) over(order by recordDate asc) as datediff,temperature - lag(temperature) over () as diff
    from weather
) where diff >0 and datediff=1
