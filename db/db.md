## Sakila

1. List all actors.

SELECT * FROM actor;

2. Find the surname of the actor with the forename 'John'.

SELECT last_name from actor WHERE first_name="John";

3. Find all actors with surname 'Neeson'.

SELECT * FROM actor WHERE last_name="Neeson";

4. Find all actors with ID numbers divisible by 10.

SELECT * from actor WHERE actor_id % 10=0;

5. What is the description of the movie with an ID of 100?

SELECT description FROM film where film_id=100;

6. Find every R-rated movie.

SELECT title FROM film WHERE rating="R";

7. Find every non-R-rated movie.

SELECT title FROM film WHERE rating !="R";

8. Find the ten shortest movies.

SELECT title,length FROM film ORDER BY length LIMIT 10;

9. Find the movies with the longest runtime, without using LIMIT.

SELECT title, length FROM film ORDER BY length DESC;

10. Find all movies that have deleted scenes.

SELECT title FROM film WHERE special_features="Deleted Scenes";

11. Using HAVING, reverse-alphabetically list the last names that are not repeated.

SELECT last_name FROM actor GROUP BY last_name HAVING COUNT(last_name) = 1 ORDER BY last_name DESC;

12. Using HAVING, list the last names that appear more than once, from highest to lowest frequency.

SELECT last_name, COUNT(last_name) FROM actor GROUP BY last_name HAVING COUNT(last_name) >1 ORDER BY COUNT(last_name) DESC;

13. Which actor has appeared in the most films?

SELECT a.first_name, a.last_name FROM actor a WHERE a.actor_id = (
  SELECT fa.actor_id FROM film_actor fa GROUP BY fa.actor_id ORDER BY COUNT(fa.film_id) DESC LIMIT 1
);

14. When is 'Academy Dinosaur' due?

SELECT release_year FROM film WHERE title="Academy Dinosaur";

15. What is the average runtime of all films?

SELECT AVG(length) from film;

16. List the average runtime for every film category.

SELECT c.category_id, c.name, AVG(f.length) AS average_runtime FROM film_category fc JOIN film f ON fc.film_id = f.film_id JOIN category c ON fc.category_id = c.category_id GROUP BY c.category_id, c.name;

17. List all movies featuring a robot.

SELECT title FROM film WHERE description LIKE "%robot%";

18. How many movies were released in 2010?

SELECT COUNT(film_id) from film WHERE release_year=2010;

19. Find the titles of all the horror movies.

SELECT f.title FROM film f JOIN film_category fc ON f.film_id = fc.film_id JOIN category c ON fc.category_id = c.category_id WHERE c.name = 'Horror';

20. List the full name of the staff member with the ID of 2.

SELECT first_name,last_name from staff where staff_id=2;

21. List all the movies that Fred Costner has appeared in.

select f.title from film f where f.film_id IN (select fa.film_id from film_actor fa where fa.actor_id=(select a.actor_id from actor a where a.first_name="fred" AND a.last_name="costner"));

22. How many distinct countries are there?

SELECT DISTINCT count(country) from country;

23. List the name of every language in reverse-alphabetical order.

SELECT DISTINCT name FROM language ORDER BY name DESC;

24. List the full names of every actor whose surname ends with '-son' in alphabetical order by their forename.

SELECT first_name,last_name FROM actor WHERE last_name LIKE "%son%";

25. Which category contains the most films?

SELECT fc.category_id,c.name, COUNT(fc.film_id) AS most_films from film_category fc JOIN category c on fc.category_id = c.category_id GROUP BY fc.category_id, c.name ORDER BY most_films DESC;