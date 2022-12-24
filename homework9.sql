SELECT city , country FROM country
INNER JOIN city ON city.country_id=country.country_id;

SELECT customer.first_name , customer.last_name,payment.payment_id  FROM customer
INNER JOIN payment ON customer.customer_id= payment.customer_id;

SELECT rental.rental_id , customer.first_name , customer.last_name FROM rental
INNER JOIN customer ON customer.customer_id = rental.customer_id;

