SELECT A.book_id, B.author_name, DATE_FORMAT(A.published_date, '%Y-%m-%d') from book A
INNER JOIN author B ON A.author_id = B.author_id
WHERE A.category = '경제'
ORDER BY A.published_date asc;