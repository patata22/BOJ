with j as (select flavor,sum(total_order) as total from july
group by flavor)

select f.flavor
from first_half f
join j on f.flavor= j.flavor
order by j.total+f.total_order desc
limit 3;
