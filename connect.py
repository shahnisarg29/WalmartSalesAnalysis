import mysql.connector
from getpass import getpass
def connect_mysql():
    try:
        connection = mysql.connector.connect(user='root', password=getpass("Enter Password : "), host='127.0.0.1')
        return connection
    except Exception as e:
        print(e)
        return -1
    

