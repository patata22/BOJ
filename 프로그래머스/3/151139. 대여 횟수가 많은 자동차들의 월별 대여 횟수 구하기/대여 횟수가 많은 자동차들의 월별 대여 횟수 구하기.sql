select month(start_date) as MONTH, CAR_ID, count(*) as RECORDS
from car_rental_company_rental_history
where car_id in (
    select car_id from car_rental_company_rental_history
    where year(start_date) = 2022 and month(start_date) in (8,9,10)
    group by car_id
    having count(history_id)>4
    ) and month(start_date) in (8,9,10)
group by month,car_id
having RECORDS>0
order by month, car_id desc;
    
