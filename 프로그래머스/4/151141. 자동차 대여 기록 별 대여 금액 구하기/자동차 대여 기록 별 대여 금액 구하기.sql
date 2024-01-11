
select h.history_id,
( case
    when datediff(h.end_date, h.start_date)>=89
    then cast(c.daily_fee*(datediff(h.end_date, h.start_date)+1)
        *(100-(select discount_rate d from car_rental_company_discount_plan
        where car_type like '트럭' and duration_type like '90%'))/100 as signed)
    when datediff(h.end_date, h.start_date)>=29
    then cast(c.daily_fee*(datediff(h.end_date, h.start_date)+1)
        *(100-(select discount_rate d from car_rental_company_discount_plan
        where car_type like '트럭' and duration_type like '30%'))/100 as signed)
    when datediff(h.end_date, h.start_date)>=6
    then cast(c.daily_fee*(datediff(h.end_date, h.start_date)+1)
        *(100-(select discount_rate d from car_rental_company_discount_plan
        where car_type like '트럭' and duration_type like '7%'))/100 as signed)
    else c.daily_fee*(datediff(h.end_date, h.start_date)+1)
    end
) as fee
from car_rental_company_car c
join car_rental_company_rental_history h
on c.car_id = h.car_id
where c.car_type like '트럭'
order by fee desc, history_id desc;