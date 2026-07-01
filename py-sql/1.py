
from mysql import connector

db = connector.connect(
    user="root",
    password="1234",
    host="localhost"
)

cursor = db.cursor()

cursor.execute("SHOW DATABASES;")
print(list(cursor))
# for i in cursor:
#     print(i)