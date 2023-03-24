-- 코드를 입력하세요
select * from (SELECT car_id, round(avg(datediff(end_date, start_date)+1),1) as average_duration
from car_rental_company_rental_history
group by car_id) as sub where sub.average_duration>=7
order by average_duration desc, car_id desc
