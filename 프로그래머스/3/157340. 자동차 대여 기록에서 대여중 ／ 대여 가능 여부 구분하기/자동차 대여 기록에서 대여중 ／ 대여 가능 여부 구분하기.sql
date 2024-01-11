with used as (
    select car_id,
    '대여중' as A
    from car_rental_company_rental_history
    where '2022-10-16' between start_date and end_date)
    
select distinct car_id, ifnull(A, '대여 가능') as AVAILABILITY
from car_rental_company_rental_history c
left join used using(car_id)
order by car_id desc;