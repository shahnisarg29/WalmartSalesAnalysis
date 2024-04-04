# Number of sales made in each time of the day per weekday
def sales_time_of_day(table_name):
    sql = f"""
    SELECT day_name, time_of_day, COUNT(*) as total_sales
    FROM {table_name}
    GROUP BY day_name, time_of_day
    ORDER BY total_sales DESC;
    """
    return sql

# Which of the customer types brings the most revenue?
def most_revenue_by_customer_type(table_name):
    sql = f"""
    SELECT customer_type, SUM(total) as revenue
    FROM {table_name}
    GROUP BY customer_type
    ORDER BY revenue DESC;
    """
    return sql

# Which city has the largest tax percent/ VAT (**Value Added Tax**)?

def avg_vat_by_city(table_name):
    sql = f"""
    SELECT city, ROUND(AVG(tax_pct), 2) as vat
    FROM {table_name}
    GROUP BY city
    ORDER BY vat DESC;
    """
    return sql

# Which customer type pays the most in VAT?
def avg_vat_by_customer(table_name):
    sql = f"""
    SELECT customer_type, ROUND(AVG(tax_pct), 2) as vat
    FROM {table_name}
    GROUP BY customer_type
    ORDER BY vat DESC;
    """
    return sql