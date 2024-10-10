# 小黎专属python固定模板
# 开发时间：2024/7/12 15:32

from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456"
)

cursor = conn.cursor()
conn.select_db("test")
cursor.execute("insert into test_pymysql values (5)")
conn.commit()
conn.close()