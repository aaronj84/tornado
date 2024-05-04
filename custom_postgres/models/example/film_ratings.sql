WITH films_with_ratings AS (
    SELECT 
        film_id,
        title,
        release_date,
        price,
        rating,
        user_rating,
        CASE 
            WHEN user_rating::numeric >= 4.5 THEN 'Excellent'
            WHEN user_rating::numeric >= 4.0 THEN 'Good'
            WHEN user_rating::numeric >= 3.0 THEN 'Average'
            ELSE 'Poor'
        END AS rating_category
    FROM films
),


films_with_actors AS (
    SELECT
        f.film_id,
        f.title,
        STRING_AGG(a.actor_name, ',') AS actors
    FROM films f 
    LEFT JOIN film_actors fa ON f.film_id = fa.film_id
    LEFT JOIN actors a ON fa.actor_id = a.actor_id
    GROUP BY f.film_id, f.title  
)

SELECT 
    fwr.*,
    fwa.actors
FROM films_with_ratings fwr
JOIN films_with_actors fwa ON fwr.film_id = fwa.film_id
