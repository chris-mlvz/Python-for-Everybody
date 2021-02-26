SELECT Album.title, Artist.name FROM Album JOIN Artist 
    ON Album.artist_id = Artist.id;

SELECT Album.title, Album.artist_id, Artist.id, Artist.name 
    FROM Album JOIN Artist ON Album.artist_id = Artist.id;

SELECT Track.title, Track.genre_id, Genre.id, Genre.name 
    FROM Track JOIN Genre; 

SELECT Track.title, Track.genre_id, Genre.id, Genre.name 
    FROM Track JOIN Genre ON Track.genre_id = Genre.id; 

SELECT Track.title, Genre.name FROM Track JOIN Genre 
    ON Track.genre_id = Genre.id;

SELECT Track.title, Artist.name, Album.title, Genre.name 
FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.id AND Track.album_id = Album.id 
    AND Album.artist_id = Artist.id;