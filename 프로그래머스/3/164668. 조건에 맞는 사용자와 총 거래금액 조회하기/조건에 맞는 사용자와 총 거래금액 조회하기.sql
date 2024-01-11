

select u.user_id, u.nickname, sum(b.price) as total_sales from used_goods_user u
join (select * from used_goods_board 
where status like 'done') b on u.user_id = b.writer_id
group by u.user_id
having total_sales>=700000
order by total_sales;