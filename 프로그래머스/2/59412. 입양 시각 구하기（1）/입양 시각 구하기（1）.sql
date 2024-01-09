select extract(hour from datetime), count(extract(hour from datetime)) from animal_outs

where extract(hour from datetime)>=9
and extract(hour from datetime)<=20
group by extract(hour from datetime)
order by extract(hour from datetime)