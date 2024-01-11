with M as (SELECT cart_id, 1 as MILK from cart_products p
where p.name like 'Milk'
group by cart_id)

select cart_id from (select cart_id, 1 as Yogurt from cart_products p
where p.name like 'Yogurt'
group by cart_id) Y join M using(cart_id)
order by cart_id


