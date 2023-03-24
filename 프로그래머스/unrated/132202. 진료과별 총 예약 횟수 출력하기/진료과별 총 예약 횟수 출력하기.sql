SELECT mcdp_cd as 진료과코드, count(apnt_no) as 5월예약건수
from appointment
where left(apnt_ymd,7)='2022-05'
group by mcdp_cd
order by 5월예약건수, 진료과코드