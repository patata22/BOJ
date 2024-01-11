
SELECT a.author_id, a.author_name, b.category, sum(b.price*s.total) TOTAL_SALES
from book b
join author a on a.author_id = b.author_id
join (select book_id, sum(sales) as total from book_sales
      where date_format(sales_date, '%Y-%m') = '2022-01'
      group by book_id) s on b.book_id = s.book_id
group by a.author_id, b.category
order by a.author_id, b.category desc