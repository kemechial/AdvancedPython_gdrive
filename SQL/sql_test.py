import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="ialdeu377",
    database="shopdb"
)

print(db)
cursor=db.cursor()
"""
cursor.execute("SHOW DATABASES")

for i in cursor:
    print(i)
"""
cursor.execute("SHOW TABLES")

for i in cursor:
    print(i)