SELECT film,rating FROM film
GROUP BY rating,film ;

SELECT replacement_cost, COUNT(film) FROM film
GROUP BY replacement_cost 
HAVING COUNT(film) > 50
ORDER BY COUNT(film) DESC;

SELECT store_id ,COUNT(customer_id) FROM customer
GROUP BY store_id;

SELECT country_id ,COUNT(city) FROM city
GROUP BY country_id
ORDER BY COUNT(city) DESC
LIMIT 1;