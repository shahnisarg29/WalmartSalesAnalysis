import pandas as pd
from connect import connect_mysql

table = pd.read_csv('WalmartSalesData.csv.csv')
conn = connect_mysql()
if conn != -1:
    try:
        conn.database = "walmartSales"
        cursor = conn.cursor()
        table_name = "sales"
        placeholders = ', '.join(['%s'] * len(table.columns))
        columns = "invoice_id, branch, city, customer_type, gender, product_line, unit_price, quantity, tax_pct, total, date, time, payment, cogs, gross_margin_pct, gross_income, rating"
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        for index, row in table.iterrows():
            val = tuple(row)
            print(val)
            cursor.execute(sql, val)
            conn.commit()
        conn.close()
    except Exception as e:
        print(e)
else:
    print("Cannot Connect to Database")
