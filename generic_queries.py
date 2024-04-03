# How many unique cities does the data have.
def unique_cities(table_name):
    sql = f"""
        SELECT DISTINCT city 
        FROM {table_name};
    """
    return sql

# Branches are in Which City

def view_branches(table_name):
    sql = f"""
        SELECT DISTINCT city, branch
        FROM {table_name};
    """
    return sql
