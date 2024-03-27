from django.db import models
import pymysql
"""
NO int 
GOODS_NAME text 
GOODS_SUB text 
GOODS_PRICE text 
GOODS_DISCOUNT int 
GOODS_FIRST_PRICE text 
GOODS_DELIVERY text 
GOODS_POSTER text 
HIT int
"""
def goodsListData(page,tname):
    conn=pymysql.connect(host='localhost',user='root',password='root',db='mydb',charset='utf8')
    cursor=conn.cursor()
    rowSize=20
    start=(rowSize*page)-(rowSize-1)
    sql=f"""
         SELECT no,goods_name,goods_price,goods_poster
         FROM {tname} 
         ORDER BY no ASC
         LIMIT {start},20
        """
    cursor.execute(sql)
    goods_data=cursor.fetchall()
    cursor.close()
    cursor=conn.cursor()
    sql=f"""
          SELECT COUNT(*) FROM {tname}
        """
    cursor.execute(sql)
    count=cursor.fetchone()
    cursor.close()
    conn.close()
    return goods_data,count[0]


