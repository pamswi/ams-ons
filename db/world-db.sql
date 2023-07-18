Using COUNT, get the number of cities in the USA.

SELECT COUNT(id) FROM city WHERE countryCode="USA";

Find out the population and life expectancy for people in Argentina.

SELECT population,lifeexpectancy FROM country WHERE name= "argentina";

Using IS NOT NULL, ORDER BY, and LIMIT, which country has the highest life expectancy?

SELECT name,lifeexpectancy FROM country WHERE lifeexpectancy IS NOT NULL ORDER BY lifeexpectancy DESC LIMIT 1;

Using JOIN ... ON, find the capital city of Spain.

SELECT city.name from country JOIN city ON country.capital = city.id where country.name="spain";

Using JOIN ... ON, list all the languages spoken in the Southeast Asia region.

SELECT country.code FROM country JOIN country ON countrylanguage.

Using a single query, list 25 cities around the world that start with the letter F.
Using COUNT and JOIN ... ON, get the number of cities in China.
Using IS NOT NULL, ORDER BY, and LIMIT, which country has the lowest population? Discard non-zero populations.
Using aggregate functions, return the number of countries the database contains.
What are the top ten largest countries by area?
List the five largest cities by population in Japan.
List the names and country codes of every country with Elizabeth II as its Head of State. You will need to fix the mistake first!
List the top ten countries with the smallest population-to-area ratio. Discard any countries with a ratio of 0.
List every unique world language.
List the names and GNP of the world's top 10 richest countries.
List the names of, and number of languages spoken by, the top ten most multilingual countries.
List every country where over 50% of its population can speak German.
Which country has the worst life expectancy? Discard zero or null values.
List the top three most common government forms.
How many countries have gained independence since records began?