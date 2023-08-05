import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
)


cursor = conexion.cursor()
cursor.execute('SHOW DATABASES')

for db in cursor:
    print(db)