#_*_coding: utf-8 _*_
#开发团队：舒逸
#开发人员：15332
#开发时间：2020/12/9 22:55
#文件名称： updateusers.py
#开发工具：PyCharm

#创建SQLite数据库文件
#1.导入模块
import  sqlite3
#2.创建连接对象
conn=sqlite3.connect("mrsoft.db")

#3.创建游标对象
cursor=conn.cursor()
#4.执行SQL语句
sql="update user set name= ? where id=?"  #使用占位符，预处理 避免sql注入
cursor.execute(sql,("MR",1))

#5.关闭游标
cursor.close()
#6.提交事务
conn.commit()
#7.关闭连接
conn.close()