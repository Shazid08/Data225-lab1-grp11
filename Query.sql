-- 1 
SELECT * FROM movies;

-- 2
SELECT title, revenue
FROM movies
ORDER BY revenue DESC
LIMIT 10;

-- 3
UPDATE movies SET title = 'Updated Title' WHERE id = 1;

-- 4
DELETE FROM movies WHERE id = 1;

-- 5
SELECT COUNT(*) FROM movies;

-- 6
SELECT m.title, g.genre_name 
FROM movies m 
INNER JOIN genre g ON m.id = g.movie_id;

-- 7
SELECT title, release_date
FROM movies;



-- 8
SELECT genre_id, COUNT(*) FROM genre GROUP BY genre_id;

-- 9
SELECT * FROM movies ORDER BY release_date DESC;

-- 10
SELECT title, 
       CASE 
           WHEN revenue > 1000000 THEN 'Blockbuster' 
           ELSE 'Average'
       END AS movie_type
FROM movies;
