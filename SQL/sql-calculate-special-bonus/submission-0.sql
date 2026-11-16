Select employee_id ,
case 
    when employee_id % 2 = 1 AND name NOT like 'M%' Then salary
    else 0
end bonus
from employees
order by employee_id;

