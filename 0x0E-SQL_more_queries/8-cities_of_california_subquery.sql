-- CALIFORNIA
SELECT id, name FROM cities WHERE state_id = (
SELECT id FROM states where name = "California") ORDER BY id;
