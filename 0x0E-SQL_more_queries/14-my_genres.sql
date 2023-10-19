-- my genres
SELECT tv_genres.name FROM tv_genres
JOIN tv_show_genres
ON tv_show_genres.genres_id = tv_genres.id
JOIN tv_shows
ON tv_shows.id = tv_show_genres.genres_id
WHERE tv_shows.name = 'Dexter'
ORDER BY tv_genres.name
