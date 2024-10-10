# 小黎专属python固定模板
# 开发时间：2024/7/12 15:22

from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456"
)
# 打印mysql版本
print(conn.get_server_info())

# 执行非查询性质SQL
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("test")
# 执行sql
# cursor.execute("create table test_pymysql(id int);")

# 执行查询性质SQL
cursor.execute("select * from account")
results = cursor.fetchall()
print(results)
for r in results:
    print(r)
# 关闭连接
conn.close()
