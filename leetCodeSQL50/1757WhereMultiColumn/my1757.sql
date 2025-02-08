# Write your MySQL query statement below
With p as (SELECT * from Products
where low_fats="Y" and recyclable="Y")

select product_id from p
