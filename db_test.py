import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='alechansumo13',
    database='sales_management'
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM sales;")
rows = cursor.fetchall()
print(rows)
cursor.close()
conn.close()
