select p.id, p.name, p.host_id from places p
join (select host_id, count(host_id) as co from places group by host_id) c on p.host_id = c.host_id
where co>1




