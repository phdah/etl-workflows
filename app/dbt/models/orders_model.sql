-- models/orders_model.sql
select
    id,
    created_at,
    updated_at,
    content::jsonb ->> 'Row ID' as row_id,
    content::jsonb ->> 'Order ID' as order_id,
    content::jsonb ->> 'Order Date' as order_date,
    content::jsonb ->> 'Ship Date' as ship_date,
    content::jsonb ->> 'Ship Mode' as ship_mode,
    content::jsonb ->> 'Customer ID' as customer_id,
    content::jsonb ->> 'Customer Name' as customer_name,
    content::jsonb ->> 'Segment' as segment,
    content::jsonb ->> 'Country/Region' as country_region,
    content::jsonb ->> 'City' as city,
    content::jsonb ->> 'State/Province' as state_province,
    content::jsonb ->> 'Postal Code' as postal_code,
    content::jsonb ->> 'Region' as region,
    content::jsonb ->> 'Product ID' as product_id,
    content::jsonb ->> 'Category' as category,
    content::jsonb ->> 'Sub-Category' as sub_category,
    content::jsonb ->> 'Product Name' as product_name,
    content::jsonb ->> 'Sales' as sales,
    content::jsonb ->> 'Quantity' as quantity,
    content::jsonb ->> 'Discount' as discount,
    content::jsonb ->> 'Profit' as profit
from
    public.orders
