#_*_coding: utf-8 _*_
#开发团队：舒逸
#开发人员：15332
#开发时间：2020/12/9 22:17
#文件名称： createSQLite.py
#开发工具：PyCharm

'''
增删改查  查询不需要提交事务，其他三种均需要


'''
#创建SQLite数据库文件
#1.导入模块
import  sqlite3
#2.创建连接对象
conn=sqlite3.connect("mrsoft.db")

#3.创建游标对象
cursor=conn.cursor()
#4.执行SQL语句
cursor.execute("create table  user(id int(10) primary key,name varchar(20))")
#5.关闭游标
cursor.close()
#6.关闭连接
conn.close()

