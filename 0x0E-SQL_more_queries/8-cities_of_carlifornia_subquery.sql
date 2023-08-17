-- Lists all the cities of california
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'Carlifornia') ORDER BY id ASC;
