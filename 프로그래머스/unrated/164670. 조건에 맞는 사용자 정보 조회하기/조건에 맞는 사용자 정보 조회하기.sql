select 
    a.USER_ID,
    a.NICKNAME,
    concat(a.city, ' ', a.street_address1, ' ', a.street_address2) as '전체주소',
    concat(substr(a.tlno, 1, 3), '-', substr(a.tlno, 4, 4), '-', substr(a.tlno, 8, 4)) as '전화번호'
from used_goods_user a
inner join (select count(board_id) as board_cnt, writer_id from USED_GOODS_BOARD group by writer_id having board_cnt >= 3) b on a.user_id = b.writer_id
order by user_id desc;