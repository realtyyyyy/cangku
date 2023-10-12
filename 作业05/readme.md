##7.5课后践习题

#第四题

SELECT * FROM user WHERE age >= 20 AND age <= 30;

#第五题

DELETE FROM user WHERE name LIKE '%张%';

#第六题

SELECT AVG(age) AS average_age FROM user;

#第七题

SELECT * FROM user WHERE age >= 20 AND age <= 30 AND name LIKE '%张%' ORDER BY age DESC;

#第九题

SELECT * FROM user WHERE teamName = 'ECNU' AND age < 20;

#第十题

SELECT COALESCE(SUM(score), 0) AS total_score FROM user WHERE teamName = 'ECNU';

