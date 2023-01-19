-- 1. Top 5 most popular articles (those with the most links to themselves):

SELECT
    name,
    (SELECT COUNT(link) FROM articles WHERE link=articles.name) as link_count
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

WITH first_level_links AS (
    SELECT link
    FROM articles
    WHERE name = 'article.name'
), second_level_links AS (
    SELECT COUNT(second.link) AS descendant_count
    FROM articles first
    JOIN articles second ON first.link = second.name
    WHERE first.name IN (SELECT link FROM first_level_links)
    GROUP BY first.link
)
SELECT AVG(descendant_count) AS avg_descendants
FROM second_level_links;