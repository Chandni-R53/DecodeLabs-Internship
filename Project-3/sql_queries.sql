-- Count total number of records
SELECT COUNT(*) FROM ecommerce_orders;
-- Observation:
-- The dataset contains 1200 records

SELECT * FROM ecommerce_orders LIMIT 5;
-- Observation:
-- Each row represents an order and contains customer,
-- product, payment, quantity and revenue information

SELECT DISTINCT Product FROM ecommerce_orders;
-- Observation:
-- The dataset contains 7 unique product categories
-- that can be used for further sales analysis

SELECT Product, COUNT(*) AS OrderCount
FROM ecommerce_orders
GROUP BY Product
ORDER BY OrderCount DESC;
-- Observation:
-- Printer appears most frequently in the dataset,
-- while Phone has the lowest number of orders

SELECT Product, SUM(TotalPrice) AS Revenue
FROM ecommerce_orders
GROUP BY Product
ORDER BY Revenue DESC;
-- Observation:
-- Chair generated the highest revenue,
-- while Phone generated the lowest revenue

SELECT Product, AVG(TotalPrice) AS AvgOrderValue
FROM ecommerce_orders
GROUP BY Product
ORDER BY AvgOrderValue DESC;
-- Observation:
-- Laptop has the highest average order value,
-- while Phone has the lowest average order value

SELECT PaymentMethod, COUNT(*) AS OrderCount
FROM ecommerce_orders
GROUP BY PaymentMethod
ORDER BY OrderCount DESC;
-- Observation:
-- Online is the most frequently used payment method,
-- while Gift Card is the least used

SELECT PaymentMethod, SUM(TotalPrice) AS Revenue
FROM ecommerce_orders
GROUP BY PaymentMethod
ORDER BY Revenue DESC;
-- Observation:
-- Credit Card generated the highest revenue,
-- while Debit Card generated the lowest revenue

SELECT ReferralSource, COUNT(*) AS OrderCount
FROM ecommerce_orders
GROUP BY ReferralSource
ORDER BY OrderCount DESC;
-- Observation:
-- Instagram has the highest number of orders,
-- while Referral has the lowest

SELECT ReferralSource, SUM(TotalPrice) AS Revenue
FROM ecommerce_orders
GROUP BY ReferralSource
ORDER BY Revenue DESC;
-- Observation:
-- Instagram generated the highest revenue,
-- while Referral generated the lowest revenue

SELECT OrderStatus, COUNT(*) AS OrderCount
FROM ecommerce_orders
GROUP BY OrderStatus
ORDER BY OrderCount DESC;
-- Observation:
-- Cancelled orders appear most frequently,
-- while Delivered orders have the lowest count

SELECT Month, COUNT(*) AS OrderCount
FROM ecommerce_orders
GROUP BY Month
ORDER BY Month;
-- Observation:
-- Orders increased until Month 6 and then
-- generally declined afterwards

SELECT Month, SUM(TotalPrice) AS Revenue
FROM ecommerce_orders
GROUP BY Month
ORDER BY Month;
-- Observation:
-- Revenue increased until Month 6 and then
-- generally declined afterwards

SELECT CustomerID, COUNT(*) AS OrderCount
FROM ecommerce_orders
GROUP BY CustomerID
ORDER BY OrderCount DESC;
-- Observation:
-- Most customers placed only one order,
-- while only a few customers placed two orders

SELECT * FROM ecommerce_orders
WHERE Product = 'Laptop';
-- Observation:
-- Displays only Laptop orders

SELECT * FROM ecommerce_orders
WHERE Product = 'Laptop'
AND TotalPrice > 1000;
-- Observation:
-- Many Laptop orders have a TotalPrice greater than 1000

SELECT * FROM ecommerce_orders
WHERE Product = 'Laptop'
OR Product = 'Phone';
-- Observation:
-- Displays orders belonging to Laptop and Phone categories

SELECT OrderID, Product, TotalPrice
FROM ecommerce_orders
ORDER BY TotalPrice DESC LIMIT 5;
-- Observation:
-- The highest-value order belongs to a Tablet,
-- followed by Monitor and Laptop orders

SELECT COUNT(*) AS TotalOrders,
SUM(TotalPrice) AS TotalRevenue,
AVG(TotalPrice) AS AvgOrderValue
FROM ecommerce_orders;
-- Observation:
-- The dataset contains 1200 orders with a total
-- revenue of 1264761.96 and an average order
-- value of 1053.97