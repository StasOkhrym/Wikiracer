-- 1. Top 5 most popular articles (those with the most links to themselves):

SELECT
    name,
    (SELECT COUNT(link) FROM articles WHERE name=articles.name) as link_count
FROM articles
GROUP BY name
ORDER BY link_count DESC
LIMIT 5;

-- 2. Top 5 articles with the most links to other articles:

SELECT name, COUNT(link) as link_count
FROM articles
GROUP BY link
ORDER BY link_count DESC
LIMIT 5;

-- 3. For a given article, find the average number of descendants of the second level: