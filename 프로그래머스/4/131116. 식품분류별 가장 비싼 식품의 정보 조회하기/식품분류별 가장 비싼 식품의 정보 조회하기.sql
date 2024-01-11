
select b.category, b.price, p.product_name 
from food_product p
join (SELECT category, max(price) as price
from food_product
where category in ('과자', '국', '김치', '식용유')
group by category) as b 
on b.category=p.category
where p.price = b.price
order by b.price desc;
