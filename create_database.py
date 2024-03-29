from connect import connect_mysql

conn = connect_mysql()
if conn != -1:
    cursor = conn.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS walmartSales"
    try:
        cursor.execute(sql)
        cursor.close()
        print("Query Executed Successfully")
    except Exception as e:
        print(e)
else:
    print("Could't Connect to the Database")

