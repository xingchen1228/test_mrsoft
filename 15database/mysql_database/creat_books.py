#_*_coding: utf-8 _*_
#开发团队：舒逸
#开发人员：15332
#开发时间：2020/12/11 22:26
#文件名称： creat_books.py
#开发工具：PyCharm

#1.导入pymysql模块
import pymysql
#2.调用connect()函数生成connection连接对象 （连接对象）
db=pymysql.connect(host="localhost",port=3306,user="root",password="",database="mingrisoft")
#3.调用cursor()方法，创建Cursor对象  （游标对象）
cursor=db.cursor()
#4.执行SQL语句
sql='''
CREATE TABLE books(
    id int(8) NOT NULL AUTO_INCREMENT,   
    name varchar(50) NOT NULL,
    category varchar(50) NOT NULL,
    price  decimal(10,2)  DEFAULT NULL,
    publish_time date DEFAULT NULL,
    PRIMARY KEY(id)
) ENGINE=MYISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

'''
cursor.execute(sql)

#5.关闭连接
cursor.close()  #关闭游标对象
db.close()  #关闭连接