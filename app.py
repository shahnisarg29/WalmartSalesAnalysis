# calling all the queries from this page
from connect import connect_mysql
from queries import *

conn = connect_mysql()
if conn != -1:
    conn.database = "walmartSales"
    table_name = "sales"
    # Just Change the Function Below and you can easily get every query to run without much hassle
    sql = time_of_day(table_name=table_name)
    print(sql)
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        conn.close()
    except Exception as e:
        print(e)
else:
    print("Cannot Connect to Database")