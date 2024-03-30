def add_time_of_day(table_name):
    sql = f""" 
    ALTER TABLE {table_name}
    ADD COLUMN time_of_day VARCHAR(20);
    """
    return sql;

def insert_time_of_day_data(table_name):
    sql = f"""
    UPDATE {table_name} 
    SET time_of_day = (
    CASE 
        WHEN time BETWEEN '00:00:00' AND '12:00:00' THEN 'Morning'
        WHEN time BETWEEN '12:00:01' AND '16:00:00' THEN 'Afternoon'
        ELSE 'Evening'
    END);
    """
    return sql

def add_day_name(table_name):
    sql = f""" 
    ALTER TABLE {table_name}
    ADD COLUMN day_name VARCHAR(20);
    """
    return sql;

def insert_day_name_data(table_name):
    sql = f"""
    UPDATE {table_name} 
    SET day_name = DAYNAME(date);
    """
    return sql

def add_month_name(table_name):
    sql = f""" 
    ALTER TABLE {table_name}
    ADD COLUMN month_name VARCHAR(20);
    """
    return sql;

def insert_month_name_data(table_name):
    sql = f"""
    UPDATE {table_name} 
    SET month_name = MONTHNAME(date);
    """
    return sql