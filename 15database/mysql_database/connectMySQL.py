#_*_coding: utf-8 _*_
#开发团队：舒逸
#开发人员：15332
#开发时间：2020/12/9 23:25
#文件名称： connectMySQL.py
#开发工具：PyCharm


#1.导入pymysql模块
import pymysql
#2.调用connect()函数生成connection连接对象 （连接对象）
db=pymysql.connect(host="localhost",port=3306,user="root",password="",database="mysql")
#3.调用cursor()方法，创建Cursor对象  （游标对象）
cursor=db.cursor()
#4.执行SQL语句

cursor.execute("select version()")
data= cursor.fetchone()
print(data)
#5.关闭连接
cursor.close()  #关闭游标对象
db.close()  #关闭连接