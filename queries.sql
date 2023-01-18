-- 1. Top 5 most popular articles (those with the most links to themselves):

SELECT parent, COUNT(*) as count
FROM article
GROUP BY parent
ORDER BY count DESC
LIMIT 5

-- 2. Top 5 articles with the most links to other articles:

-- 3. For a given article, find the average number of descendants of the second level: