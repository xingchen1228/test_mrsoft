#_*_coding: utf-8 _*_
#开发团队：舒逸
#开发人员：15332
#开发时间：2020/12/12 0:00
#文件名称： insert.py
#开发工具：PyCharm


#1.导入pymysql模块
import pymysql
#2.调用connect()函数生成connection连接对象 （连接对象）
db=pymysql.connect(host="localhost",port=3306,user="root",password="",database="mingrisoft",charset="utf8")
#3.调用cursor()方法，创建Cursor对象  （游标对象）
cursor=db.cursor()
data=[('唐诗三百首','唐诗',15.39,"2016-10-15"),('Python从入门到项目实践','python',78.69,"2020-08-15"),('未来的你一定会感谢现在拼命的自己','鸡汤',23.39,"2017-10-15")]

try:
    #4.执行SQL语句
    sql="insert into books(name,category,price,publish_time) values(%s,%s,%s,%s)"

    #cursor.execute(sql,data)  #插入一条数据
    cursor.executemany(sql,data)
    db.commit()  #提交
except:
    db.rollback()    #如果执行失败则回滚
#5.关闭连接
cursor.close()  #关闭游标对象
db.close()  #关闭连接