
from mysql import connector

db = connector.connect(
    user="root",
    password="1234",
    host="localhost",
    database="dars_db"
)

cursor = db.cursor()

query1 = f"""
    INSERT INTO users (username, ism, last_name, posts_count, followers, followings, joined_date)
    VALUES
    ('{input()}', '{input()}', '{input()}', {input()}, {input()}, {input()}, '{input()}')
"""

cursor.execute(query1)
db.commit()
print(cursor.rowcount, "ta qator o'zgardi")

