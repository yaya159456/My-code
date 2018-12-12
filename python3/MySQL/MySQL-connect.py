'''python3和mysql连接的一些动作演示，在python中输入sql语句就行 感叹：人生苦短 我用python！
1.从数据库中读取数据
2.将数据上传到mysql中
3.执行sql其他语句（需要啥你就写啥 随你~）
'''

import pymysql
import pandas as pd
from pandas import DataFrame, Series
from sqlalchemy import create_engine

#读取mysql中的数据
# engine = create_engine('mysql+pymysql://root:yaya159456@localhost:3306/yaya_demo_3')
# sql = '''select * from demo_1;'''
# df2 = pd.read_sql_query(sql, engine)
# print(df2)

#将数据存储到mysql表中
engine = create_engine('mysql+pymysql://root:yaya159456@localhost:3306/yaya_demo_3')
df = pd.read_excel('demo1.xlsx')
df.to_sql('demo2', engine)

#逐行写入数据
# db = pymysql.connect('localhost', 'root', 'yaya159456', 'yaya_demo_3')
# cursor = db.cursor()
# cursor.execute('''insert into demo_1 (NAME, HEIGHT, WEIGHT) values ('Jim', 160, 130)''')
#
# sql = '''SELECT * FROM demo_1'''#定义sql语句 需要啥写啥
# data = cursor.execute(sql)
#
# rows = cursor.fetchall()
# print(rows)

# db.commit()#将结果保留
# cursor.close()
# db.close()