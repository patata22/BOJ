select p.product_code, sum(o.sales_amount*p.price) t from product p
join offline_sale o on p.product_id = o.product_id
group by p.product_id
order by t desc, product_code;