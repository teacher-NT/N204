
from mysql import connector

db = connector.connect(
    user="root",
    password="1234",
    host="localhost",
    database="dars_db"
)

cursor = db.cursor()

query1 = f"""
    UPDATE users
    SET user_id=31,
    followers=551234234
    WHERE username='saidaloxon911';
"""

query2 = f"""
    DELETE FROM users
    WHERE followers < 200000000;
"""

cursor.execute(query2)
db.commit()
print(cursor.rowcount, "ta qator o'zgardi")

