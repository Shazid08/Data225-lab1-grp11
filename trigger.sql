
-- 1
CREATE TRIGGER audit_movie_changes
AFTER UPDATE ON movies
FOR EACH ROW
INSERT INTO audit_log (action, movie_id, INSERTED_AT)
VALUES ('Update', OLD.id, NOW());

-- 2
CREATE TRIGGER auto_increment_movie_id
BEFORE INSERT ON movies
FOR EACH ROW
SET NEW.id = (SELECT MAX(id) + 1 FROM movies);

-- 3
delimiter //
CREATE TRIGGER prevent_movie_deletion
BEFORE DELETE ON movies
FOR EACH ROW
BEGIN
    IF OLD.status = 'Released' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete released movie';
    END IF;
END//
delimiter ;

-- 4
CREATE TRIGGER log_rating_changes
AFTER INSERT ON ratings
FOR EACH ROW
INSERT INTO rating_log (movie_id, new_rating, timestamp)
VALUES (NEW.movieId, NEW.rating, NOW());

-- 5
delimiter //
CREATE TRIGGER cascade_update_genre
AFTER UPDATE ON movies
FOR EACH ROW
BEGIN
    UPDATE genre SET genre_name = NEW.title WHERE movie_id = NEW.id;
END;
delimiter ;
