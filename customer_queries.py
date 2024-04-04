# How many unique customer types does the data have?
def unique_customer_types(table_name):
    sql = f"""
    SELECT DISTNCT customer_type
    FROM {table_name};
    """
    return sql

# How many unique payment methods does the data have?
def unique_payment_method(table_name):
    sql = f"""
    SELECT DISTNCT payment
    FROM {table_name};
    """
    return sql

# What is the most common customer type?
def common_customer_type(table_name):
    sql = f"""
    SELECT customer_type, COUNT(customer_type) as customer_cnt
    FROM {table_name}
    GROUP BY customer_type
    ORDER BY customer_cnt DESC;
    """
    return sql

# What is the gender of most of the customers?
def customer_gender(table_name):
    sql = f"""
    SELECT gender, COUNT(*) as customer_cnt
    FROM {table_name}
    GROUP BY gender
    ORDER BY customer_cnt DESC;
    """
    return sql

# What is the gender distribution per branch
def customer_gender_branchwise(table_name):
    sql = f"""
    SELECT branch, gender, COUNT(*) as customer_cnt
    FROM {table_name}
    GROUP BY branch, gender
    ORDER BY branch, customer_cnt DESC;
    """
    return sql

# Which time of the day do customers give most ratings
def ratings_time_of_day(table_name):
    sql = f"""
    SELECT time_of_day, AVG(rating) as avg_rating, COUNT(rating) as rating_count
    FROM {table_name}
    GROUP BY time_of_day
    ORDER BY avg_rating DESC;
    """
    return sql

# Which time of the day do customers give most ratings per branch
def ratings_time_of_day_branchwise(table_name):
    sql = f"""
    SELECT branch, time_of_day, AVG(rating) as avg_rating, COUNT(rating) as rating_count
    FROM {table_name}
    GROUP BY branch, time_of_day
    ORDER BY branch, avg_rating DESC;
    """
    return sql

# Which day fo the week has the best avg ratings?
def avg_rating_daywise(table_name):
    sql = f"""
    SELECT day_name, AVG(rating) as avg_rating, COUNT(rating) as rating_count
    FROM {table_name}
    GROUP BY day_name
    ORDER BY avg_rating DESC;
    """
    return sql

# Which day of the week has the best average ratings per branch?
def avg_rating_daywise_branchwise(table_name):
    sql = f"""
    SELECT branch, day_name, AVG(rating) as avg_rating, COUNT(rating) as rating_count
    FROM {table_name}
    GROUP BY branch, day_name
    ORDER BY branch, avg_rating DESC;
    """
    return sql
