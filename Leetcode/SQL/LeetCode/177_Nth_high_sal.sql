CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS INT AS $$
BEGIN
  RETURN (
    -- Write your PostgreSQL query statement below.
        select distinct a.salary from (select salary,DENSE_RANK() over (order by salary desc) as rnk from Employee)a where rnk=N
      
  );
END;
$$ LANGUAGE plpgsql;