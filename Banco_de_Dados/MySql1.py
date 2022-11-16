import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'northwind'
)
cursor = conn.cursor()

Empresa = "Company A"

select_statement = f"select * from customers where company = '{Empresa}';"
cursor.execute(select_statement)
orders = cursor.fetchall()

for order in orders:
    print(order)

#update, delete, insert e drop precisa do comando commit
