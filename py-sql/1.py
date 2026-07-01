
from mysql import connector

db = connector.connect(
    user="root",
    password="1234",
    host="localhost",
    database="dars_db"
)

cursor = db.cursor()

cursor.execute("SELECT ism, followers, posts_count FROM users;")
# jadval = cursor.fetchall()
# for i in jadval:
#     print(i)

# qator = cursor.fetchone()
# print(qator)

# jadval = cursor.fetchmany(5)
# for i in jadval:
#     print(i)

# print(list(cursor))
# for i in cursor:
#     print(i)