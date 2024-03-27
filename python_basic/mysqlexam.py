import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', db='mydb', charset='utf8')
cursor=conn.cursor()
sql="""
     SELECT * FROM music 
    """
cursor.execute(sql)
music=cursor.fetchall()
print(music)
cursor.close()
conn.close()