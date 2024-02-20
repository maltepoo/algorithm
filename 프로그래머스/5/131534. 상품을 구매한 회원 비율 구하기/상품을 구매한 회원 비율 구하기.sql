select
    year(b.sales_date) as YEAR,
    month(b.sales_date) as MONTH,
    count(distinct a.user_id) as PUCHASED_USERS,
    round(
        count(distinct a.user_id) / 
        (select 
            count(distinct c.user_id) 
         from user_info c
         where year(c.joined) = '2021'), 1) 
        as PUCHASED_RATIO
from user_info a
inner join online_sale b on a.user_id = b.user_id
where year(a.joined) = '2021'
group by year, month
order by year, month;