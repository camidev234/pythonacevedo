import mysql.connector 

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pruebaProyecto2"
)
cursor=db.cursor()
