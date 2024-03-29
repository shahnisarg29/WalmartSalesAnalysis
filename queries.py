def time_of_day(table_name):
    sql = f""" SELECT time, (CASE 
    WHEN time BETWEEN '00:00:00' AND '12:00:00' THEN 'Morning'
    WHEN time BETWEEN '12:00:01' AND '16:00:00' THEN 'Afternoon'
    ELSE 'Evening'
    END) AS time_of_day
    FROM {table_name};
"""
    return sql;