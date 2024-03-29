# Select the Database First and then Create table
from connect import connect_mysql

conn = connect_mysql()
if conn != -1:
    conn.database = "walmartSales"
    cursor = conn.cursor()
    sql = """CREATE TABLE IF NOT EXISTS sales(
                invoice_id VARCHAR(30) NOT NULL PRIMARY KEY,
                branch VARCHAR(5) NOT NULL,
                city VARCHAR(30) NOT NULL,
                customer_type VARCHAR(30) NOT NULL,
                gender VARCHAR(30) NOT NULL,
                product_line VARCHAR(100) NOT NULL,
                unit_price DECIMAL(10,2) NOT NULL,
                quantity INT NOT NULL,
                tax_pct FLOAT(6,4) NOT NULL,
                total DECIMAL(12, 4) NOT NULL,
                date DATETIME NOT NULL,
                time TIME NOT NULL,
                payment VARCHAR(15) NOT NULL,
                cogs DECIMAL(10,2) NOT NULL,
                gross_margin_pct FLOAT(11,9),
                gross_income DECIMAL(12, 4),
                rating FLOAT(2, 1)
            )"""
    try:
        cursor.execute(sql)
        cursor.close()
        print("Query Executed Successfully")
    except Exception as e:
        print(e)
else:
    print("Could't Connect to the Database")