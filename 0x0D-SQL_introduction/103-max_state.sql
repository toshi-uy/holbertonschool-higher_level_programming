-- Write a script that displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending).
SELECT state, MAX(value) AS max_temp FROM temperatures ORDER BY state DESC;
