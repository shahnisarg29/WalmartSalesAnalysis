# How many unique product lines does the data have?
def unique_product_lines(table_name):
    sql = f"""
    SELECT COUNT(DISTINCT product_line)
    FROM {table_name};
    """
    return sql

# What is the most common payment method?
def common_payment_method(table_name):
    sql = f"""
    SELECT payment, COUNT(payment) AS cnt
    FROM {table_name}
    GROUP BY payment
    ORDER BY cnt DESC;
    """
    return sql

# What is the most selling product line?
def most_selling_product_line(table_name):
    sql = f"""
    SELECT product_line, COUNT(product_line) AS cnt
    FROM {table_name}
    GROUP BY product_line
    ORDER BY cnt DESC;
    """
    return sql

# What is the total revenue by month?
def revenue_by_month(table_name):
    sql = f"""
    SELECT month_name, SUM(total) AS total_revenue
    FROM {table_name}
    GROUP BY month_name
    ORDER BY total_revenue DESC;
    """
    return sql

# What month had the largest COGS?
def largest_cogs_month(table_name):
    sql = f"""
    SELECT month_name, SUM(cogs) AS total_cogs
    FROM {table_name}
    GROUP BY month_name
    ORDER BY total_cogs DESC;
    """
    return sql

# What product line had the largest revenue?
def largest_revenue_product_line(table_name):
    sql = f"""
    SELECT product_line, SUM(total) AS total_revenue
    FROM {table_name}
    GROUP BY product_line
    ORDER BY total_revenue DESC;
    """
    return sql

# What is the city with the largest revenue?
def largest_revenue_city(table_name):
    sql = f"""
    SELECT city, SUM(total) AS total_revenue
    FROM {table_name}
    GROUP BY city
    ORDER BY total_revenue DESC;
    """
    return sql

# What product line had the largest VAT?
def largest_vat_product_line(table_name):
    sql = f"""
    SELECT product_line, AVG(tax_pct) AS avg_tax
    FROM {table_name}
    GROUP BY product_line
    ORDER BY avg_tax DESC;
    """
    return sql

# Fetch each product line and add a column to those product line showing "Good", "Bad". Good if its greater than average sales
def product_line_sales_performance(table_name):
    sql = f"""
    SELECT product_line, ROUND(SUM(total),2) AS total_sales, 
    (CASE 
    WHEN SUM(total) > (SELECT AVG(revenue)
        FROM (
            SELECT SUM(total) AS revenue
            FROM {table_name}
            GROUP BY product_line
        ) temp) THEN 'Good'
    ELSE 'Bad'
    END
    ) AS performance
    FROM {table_name}
    GROUP BY product_line;
    """
    return sql

# Which branch sold more products than average product sold?
def above_avg_sales_branch(table_name):
    sql = f"""
    SELECT branch, SUM(quantity) as qty
    FROM {table_name}
    GROUP BY branch 
    HAVING qty > (
        SELECT AVG(products_sold)
        FROM (
            SELECT SUM(quantity) AS products_sold
            FROM {table_name}
            GROUP BY branch
        )
    );
"""
    return sql

# What is the most common product line by gender?

def common_product_line_gender(table_name):
    sql = f"""
    SELECT gender, product_line, COUNT(product_line) AS cnt
    FROM {table_name}
    GROUP BY gender, product_line
    ORDER BY gender, cnt DESC
    """
    return sql

# What is the average rating of each product line?
def avg_rating_product_line(table_name):
    sql = f"""
    SELECT product_line, ROUND(AVG(rating), 2) AS avg_rating
    FROM {table_name}
    GROUP BY product_line
    ORDER BY avg_rating;
    """
    return sql