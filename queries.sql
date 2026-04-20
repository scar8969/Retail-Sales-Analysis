show databases;
create database data_fund;
use data_fund;
CREATE TABLE sales (
    order_id INT,
    order_date DATE,
    city VARCHAR(50),
    product VARCHAR(50),
    category VARCHAR(50),
    quantity INT,
    price INT
);

select * from sales;

INSERT INTO sales VALUES
(1001,'2025-01-10','Pune','Laptop','Electronics',2,50000),
(1002,'2025-01-11','Mumbai','Mobile','Electronics',3,20000),
(1003,'2025-01-11','Pune','Headphones','Accessories',5,2000),
(1004,'2025-01-12','Nagpur','Keyboard','Accessories',4,1500),
(1005,'2025-01-13','Mumbai','Laptop','Electronics',1,50000),
(1006,'2025-01-14','Pune','Mobile','Electronics',2,22000),
(1007,'2025-01-15','Nagpur','Laptop','Electronics',1,52000),
(1008,'2025-01-30','Mumbai','Headphones','Accessories',6,1800),
(1009,'2025-01-02','Bangalore','Mobile','Electronics',3,22000),
(1010,'2025-01-28','Guwahati','Laptop','Electronics',4,52000),
(1011,'2025-01-22','Ahmedabad','Headphones','Accessories',10,1800);


SELECT * FROM sales;


# Total revenue 

SELECT SUM(quantity * price) AS total_revenue FROM sales;

# Top-selling product (by quantity)

SELECT product, SUM(quantity) AS total_qty FROM sales GROUP BY product ORDER BY total_qty DESC LIMIT 1;

# Revenue by city

SELECT city, SUM(quantity * price) AS revenue FROM sales GROUP BY city;

# Category-wise revenue

SELECT category, SUM(quantity * price) AS revenue FROM sales GROUP BY category;

# Highest value order

SELECT *, (quantity * price) AS total FROM sales ORDER BY total DESC LIMIT 1;

# Average product price

SELECT AVG(price) AS avg_price FROM sales;
