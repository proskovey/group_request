from sqlalchemy import create_engine
engine = create_engine('postgresql://proskovey:123456@localhost:5432/music_db') 
print(engine)

connection = engine.connect()

print(connection.execute("""SELECT genre_name, COUNT(executor_id) FROM genre g
JOIN executor_genre e ON g.id = e.genre_id
GROUP BY genre_name;""").fetchall())

print(connection.execute("""SELECT name, COUNT(track_name) FROM album a
JOIN track t ON t.id = a.id
WHERE year BETWEEN '2019-01-01' and '2020-01-01'
GROUP BY name;""").fetchall())

print(connection.execute("""SELECT name, ROUND(AVG(lenght),2) FROM album a
JOIN track t ON t.id = a.id
GROUP BY name;""").fetchall())

print(connection.execute("""SELECT nickname FROM executor e
JOIN album a ON a.id = album_id
WHERE year NOT BETWEEN '2020-01-01' and '2020-01-01';""").fetchall())

print(connection.execute("""SELECT name FROM collection c
JOIN track_collection ON collection_id = c.id
JOIN track t ON t.id = track_id
JOIN genre a ON a.track_id = t.id
JOIN executor_genre eg ON genre_id = a.id
JOIN executor e ON e.id = executor_id
WHERE e.nickname = 'Prodigy';""").fetchall())

print(connection.execute("""SELECT DISTINCT name FROM album a
JOIN executor e ON album_id = a.id
JOIN executor_genre eg ON executor_id = e.id
JOIN genre gg ON gg.id = genre_id 
WHERE executor_id IN (
    SELECT executor_id FROM executor_genre
    GROUP BY executor_id
    HAVING COUNT(genre_id) >= 2);""").fetchall())

print(connection.execute("""SELECT track_name FROM track t
LEFT JOIN track_collection ON track_id = t.id
WHERE track_id IS NULL;""").fetchall())

print(connection.execute("""SELECT nickname FROM executor e
JOIN executor_genre eg ON executor_id = e.id
JOIN genre g ON g.id = genre_id 
JOIN track t ON g.track_id = t.id
WHERE t.lenght in (SELECT MIN(lenght) FROM track);""").fetchall())

print(connection.execute("""SELECT a.name, COUNT(t.track_name) FROM album a
JOIN executor e ON album_id = a.id
JOIN executor_genre eg ON executor_id = e.id
JOIN genre g ON g.id = genre_id 
JOIN track t ON t.id = track_id
GROUP BY a.name
HAVING COUNT(t.track_name) = (
	SELECT MIN(count) FROM (
		SELECT a.name, COUNT(t.track_name) FROM album a
		JOIN executor e ON album_id = a.id
        JOIN executor_genre eg ON executor_id = e.id
        JOIN genre g ON g.id = genre_id 
        JOIN track t ON t.id = track_id
		GROUP BY a.name) AS foo);""").fetchall())