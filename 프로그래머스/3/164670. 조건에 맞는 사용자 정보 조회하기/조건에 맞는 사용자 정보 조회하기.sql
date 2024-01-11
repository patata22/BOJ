select u.user_id, u.nickname, concat(u.city, ' ', u.street_address1,' ', u.street_address2) 'as 전체주소', concat(substr(u.tlno,1,3),'-',substr(u.tlno,4,4),'-',substr(u.tlno, 8,4)) as '전화번호'
from used_goods_user u
join (
    select writer_id
    from used_goods_board
    group by writer_id
    having count(writer_id)>2) b 
    on u.user_id=b.writer_id
order by user_id desc;