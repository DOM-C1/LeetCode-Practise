-- Meh solution to this LeetCode medium problem
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | country       | varchar |
-- | state         | enum    |
-- | amount        | int     |
-- | trans_date    | date    |
-- +---------------+---------+
-- id is the primary key of this table.
-- The table has information about incoming transactions.
-- The state column is an enum of type ["approved", "declined"].
 

-- Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

-- Return the result table in any order.




WITH TOTAL AS (
    SELECT 
        DATE_FORMAT(trans_date, '%Y-%m') AS month, 
        country,
        SUM(amount) AS trans_total_amount,
        COUNT(*) AS trans_count
    FROM 
        Transactions
    GROUP BY 
        month, 
        country
),
APPROVED AS (
    SELECT 
        DATE_FORMAT(trans_date, '%Y-%m') AS month, 
        country,
        SUM(amount) AS approved_total_amount,
        COUNT(state) AS approved_count
    FROM 
        Transactions
    WHERE state = 'approved'
    GROUP BY 
        month, 
        country
)
SELECT 
    T.month, 
    T.country,
    T.trans_count,
    COALESCE(A.approved_count, 0) AS approved_count,
    T.trans_total_amount,
    COALESCE(A.approved_total_amount, 0) AS approved_total_amount
FROM 
    TOTAL AS T
LEFT JOIN 
    APPROVED AS A 
ON 
    T.month = A.month AND (T.country = A.country OR (T.country IS NULL AND A.country IS NULL))
ORDER BY 
    T.month, 
    T.country;