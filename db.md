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



12. Using HAVING, list the last names that appear more than once, from highest to lowest frequency.
13. Which actor has appeared in the most films?

SELECT a.first_name, a.last_name FROM actor a WHERE a.actor_id = (
  SELECT fa.actor_id FROM film_actor fa GROUP BY fa.actor_id ORDER BY COUNT(fa.film_id) DESC LIMIT 1
);

14. When is 'Academy Dinosaur' due?

SELECT release_year FROM film WHERE title="Academy Dinosaur";

15. What is the average runtime of all films?

SELECT AVG(length) from film;

16. List the average runtime for every film category.

SELECT AVG(length) from film;

SELECT DISTINCT name from category JOIN film.length on category_id;

List all movies featuring a robot.
How many movies were released in 2010?
Find the titles of all the horror movies.
List the full name of the staff member with the ID of 2.
List all the movies that Fred Costner has appeared in.
How many distinct countries are there?
List the name of every language in reverse-alphabetical order.
List the full names of every actor whose surname ends with '-son' in alphabetical order by their forename.
Which category contains the most films?