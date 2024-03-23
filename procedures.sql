-- 1
DELIMITER //

CREATE PROCEDURE add_movie (
    IN title VARCHAR(255),
    IN release_date DATE,
    IN budget DECIMAL(10,2),
    IN revenue DECIMAL(10,2),
    IN status VARCHAR(50)
)
BEGIN
    INSERT INTO movies (title, release_date, budget, revenue, status)
    VALUES (title, release_date, budget, revenue, status);
END //

DELIMITER ;

-- 2
DELIMITER //

CREATE PROCEDURE update_movie_revenue (
    IN movie_id INT,
    IN new_revenue DECIMAL(10,2)
)
BEGIN
    UPDATE movies SET revenue = new_revenue WHERE id = movie_id;
END //

DELIMITER ;

-- 3
DELIMITER //

CREATE PROCEDURE delete_movie (
    IN movie_id INT
)
BEGIN
    DELETE FROM movies WHERE id = movie_id;
END //

DELIMITER ;

-- 4
DELIMITER //

CREATE PROCEDURE get_movie_details (
    IN movie_id INT,
    OUT movie_title VARCHAR(255),
    OUT release_date DATE,
    OUT budget DECIMAL(10,2),
    OUT revenue DECIMAL(10,2),
    OUT status VARCHAR(50)
)
BEGIN
    SELECT title, release_date, budget, revenue, status
    INTO movie_title, release_date, budget, revenue, status
    FROM movies WHERE id = movie_id;
END //

DELIMITER ;

-- 5
DELIMITER //

CREATE PROCEDURE calculate_average_rating (
    INOUT avg_rating DECIMAL(3,2)
)
BEGIN
    SELECT AVG(rating) INTO avg_rating FROM ratings;
END //

DELIMITER ;
