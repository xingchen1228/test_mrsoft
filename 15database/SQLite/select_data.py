#_*_coding: utf-8 _*_
#开发团队：舒逸
#开发人员：15332
#开发时间：2020/12/9 22:45
#文件名称： select_data.py
#开发工具：PyCharm

'''
查询数据的3种方式
    fetchone(): 获取查询结果集中的下一条记录
    fetchmany(size):  获取指定数量的记录
    fetchall(): 获取结果集的所有记录
'''

#创建SQLite数据库文件
#1.导入模块
import  sqlite3
#2.创建连接对象
conn=sqlite3.connect("mrsoft.db")

#3.创建游标对象
cursor=conn.cursor()
#4.执行SQL语句
sql="select * from user where id >=3"
cursor.execute(sql)
# cursor.fetchone()  #etchone(): 获取查询结果集中的下一条记录
# result1= cursor.fetchone()
# print(result1)

# result2= cursor.fetchmany(3)
# print(result2)

result3=cursor.fetchall()
print(result3)
#5.关闭游标
cursor.close()

#6.关闭连接
conn.close()