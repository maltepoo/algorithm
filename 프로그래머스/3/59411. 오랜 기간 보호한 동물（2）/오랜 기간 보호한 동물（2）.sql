SELECT
    a.animal_id as ANIMAL_ID
    ,a.name as NAME
from animal_outs a
inner join animal_ins b on a.animal_id = b.animal_id
order by a.datetime - b.datetime desc
limit 2;