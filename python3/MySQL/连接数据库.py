import pymysql
db = pymysql.connect('localhost', 'root', 'yaya159456', 'yaya_demo')

cursor = db.cursor()

sql = '''insert into demo1 ( name, score) values ('小刚', 90)'''
cursor.execute(sql)

cursor.execute("select * from demo1")
data = cursor.fetchall()
print(data)

db.commit()# 将更改保存到mysql中
cursor.close()
db.close()