import mysql.connector

# 创建连接
connection = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database'
)

# 检查连接
if connection.is_connected():
    print("成功连接到数据库")

# 创建游标
cursor = connection.cursor()

# 插入数据
insert_query = """INSERT INTO your_table (column1, column2) VALUES (%s, %s)"""
data_to_insert = ("value1", "value2")
cursor.execute(insert_query, data_to_insert)

# 提交事务
connection.commit()
print(cursor.rowcount, "条记录插入成功。")

# 查询数据
select_query = "SELECT * FROM your_table"
cursor.execute(select_query)
result = cursor.fetchall()
for row in result:
    print(row)

# 更新数据
update_query = """UPDATE your_table SET column1 = %s WHERE column2 = %s"""
data_to_update = ("new_value1", "value2")
cursor.execute(update_query, data_to_update)

# 提交事务
connection.commit()
print(cursor.rowcount, "条记录更新成功。")

# 删除数据
delete_query = """DELETE FROM your_table WHERE column1 = %s"""
data_to_delete = ("new_value1",)
cursor.execute(delete_query, data_to_delete)

# 提交事务
connection.commit()
print(cursor.rowcount, "条记录删除成功。")

# 关闭游标和连接
cursor.close()
connection.close()
print("连接关闭")