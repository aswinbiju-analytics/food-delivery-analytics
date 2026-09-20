USE food_delivery_analytics;


SELECT 
    COUNT(*) AS total_orders
FROM food_delivery;

SELECT 
    ROUND(SUM(order_value), 2) AS total_revenue
FROM food_delivery;


SELECT 
    ROUND(AVG(order_value), 2) AS average_order_value
FROM food_delivery;

SELECT
    food_item,
    COUNT(*) AS total_orders
FROM food_delivery
GROUP BY food_item
ORDER BY total_orders DESC;

SELECT
    location,
    COUNT(*) AS total_orders
FROM food_delivery
GROUP BY location
ORDER BY total_orders DESC;

SELECT
    location,
    ROUND(SUM(order_value), 2) AS total_revenue
FROM food_delivery
GROUP BY location
ORDER BY total_revenue DESC;

SELECT
    location,
    COUNT(*) AS total_orders,
    ROUND(SUM(order_value), 2) AS total_revenue,
    ROUND(AVG(order_value), 2) AS average_order_value
FROM food_delivery
GROUP BY location
ORDER BY total_revenue DESC;

SELECT
    location,
    ROUND(SUM(order_value), 2) AS total_revenue
FROM food_delivery
GROUP BY location
ORDER BY total_revenue DESC
LIMIT 5;

SELECT
    delivery_method,
    COUNT(*) AS total_orders,
    ROUND(AVG(delivery_delay), 2) AS average_delay,
    ROUND(AVG(delivery_distance), 2) AS average_distance,
    ROUND(AVG(customer_rating), 2) AS average_rating,
    ROUND(AVG(customer_satisfaction), 2) AS average_satisfaction
FROM food_delivery
GROUP BY delivery_method
ORDER BY total_orders DESC;

SELECT
    traffic_condition,
    COUNT(*) AS total_orders,
    ROUND(AVG(delivery_delay), 2) AS average_delay,
    ROUND(AVG(customer_satisfaction), 2) AS average_satisfaction
FROM food_delivery
GROUP BY traffic_condition
ORDER BY average_delay DESC;

SELECT
    weather_condition,
    COUNT(*) AS total_orders,
    ROUND(AVG(delivery_delay), 2) AS average_delay,
    ROUND(AVG(customer_satisfaction), 2) AS average_satisfaction
FROM food_delivery
GROUP BY weather_condition
ORDER BY average_delay DESC;

SELECT
    loyalty_program,
    COUNT(*) AS total_orders,
    ROUND(SUM(order_value), 2) AS total_revenue,
    ROUND(AVG(order_value), 2) AS average_order_value,
    ROUND(AVG(customer_rating), 2) AS average_rating,
    ROUND(AVG(customer_satisfaction), 2) AS average_satisfaction
FROM food_delivery
GROUP BY loyalty_program;

SELECT
    customer_satisfaction,
    COUNT(*) AS total_orders,
    ROUND(AVG(customer_rating), 2) AS average_rating,
    ROUND(AVG(delivery_delay), 2) AS average_delay,
    ROUND(AVG(order_value), 2) AS average_order_value
FROM food_delivery
GROUP BY customer_satisfaction
ORDER BY customer_satisfaction;

SELECT
    food_condition,
    COUNT(*) AS total_orders,
    ROUND(AVG(customer_rating), 2) AS average_rating,
    ROUND(AVG(customer_satisfaction), 2) AS average_satisfaction,
    ROUND(AVG(delivery_delay), 2) AS average_delay
FROM food_delivery
GROUP BY food_condition
ORDER BY average_satisfaction DESC;

SELECT
    MONTH(order_time) AS order_month,
    COUNT(*) AS total_orders,
    ROUND(SUM(order_value), 2) AS total_revenue,
    ROUND(AVG(order_value), 2) AS average_order_value
FROM food_delivery
GROUP BY MONTH(order_time)
ORDER BY order_month;

SELECT
    restaurant_id,
    COUNT(*) AS total_orders,
    ROUND(SUM(order_value), 2) AS total_revenue,
    ROUND(AVG(order_value), 2) AS average_order_value
FROM food_delivery
GROUP BY restaurant_id
ORDER BY total_orders DESC
LIMIT 10;

SELECT
    restaurant_id,
    COUNT(*) AS total_orders,
    ROUND(SUM(order_value), 2) AS total_revenue,
    ROUND(AVG(order_value), 2) AS average_order_value
FROM food_delivery
GROUP BY restaurant_id
ORDER BY total_revenue DESC
LIMIT 10;

SELECT
    CASE
        WHEN delivery_delay < 0 THEN 'Early'
        WHEN delivery_delay = 0 THEN 'On Time'
        ELSE 'Delayed'
    END AS delivery_status,
    COUNT(*) AS total_orders
FROM food_delivery
GROUP BY
    CASE
        WHEN delivery_delay < 0 THEN 'Early'
        WHEN delivery_delay = 0 THEN 'On Time'
        ELSE 'Delayed'
    END;
    
    
SELECT
    traffic_condition,
    COUNT(*) AS total_orders,
    ROUND(AVG(delivery_delay), 2) AS average_delay,
    ROUND(AVG(customer_satisfaction), 2) AS average_satisfaction
FROM food_delivery
GROUP BY traffic_condition
ORDER BY average_delay DESC;

SELECT
    weather_condition,
    COUNT(*) AS total_orders,
    ROUND(AVG(delivery_delay), 2) AS average_delay,
    ROUND(AVG(customer_satisfaction), 2) AS average_satisfaction
FROM food_delivery
GROUP BY weather_condition
ORDER BY average_delay DESC;

SELECT
    loyalty_program,
    COUNT(*) AS total_orders,
    ROUND(SUM(order_value), 2) AS total_revenue,
    ROUND(AVG(order_value), 2) AS average_order_value,
    ROUND(AVG(customer_satisfaction), 2) AS average_satisfaction
FROM food_delivery
GROUP BY loyalty_program
ORDER BY total_orders DESC;

SELECT
    customer_satisfaction,
    COUNT(*) AS total_orders,
    ROUND(AVG(delivery_delay), 2) AS average_delay,
    ROUND(AVG(order_value), 2) AS average_order_value
FROM food_delivery
GROUP BY customer_satisfaction
ORDER BY customer_satisfaction;

SELECT
    MONTH(order_time) AS order_month,
    COUNT(*) AS total_orders,
    ROUND(SUM(order_value), 2) AS total_revenue,
    ROUND(AVG(order_value), 2) AS average_order_value
FROM food_delivery
GROUP BY MONTH(order_time)
ORDER BY order_month;
