from django.db import models
from web import models
import oracledb

def foodListData(page):
    try:
         conn=models.getConnection()
         cursor=conn.cursor()
         rowSize=20
         start=(rowSize*page)-(rowSize-1)
         end=rowSize*page

         sql=f"""
               SELECT fno,name,poster,num
               FROM (SELECT fno,name,poster,rownum as num
               FROM (SELECT fno,name,poster 
               FROM food_menu_house ORDER BY fno ASC))
               WHERE num BETWEEN {start} AND {end}
              """
         #실행
         cursor.execute(sql)
         #데이터 받기
         food_list=cursor.fetchall()
         cursor.close()
         conn.close()
    except Exception as e:
         print(e)
    return food_list

def foodTotalPage():
    try:
         conn=models.getConnection()
         cursor=conn.cursor()
         sql="""
               SELECT CEIL(COUNT(*)/20.0) FROM food_menu_house
             """
         cursor.execute(sql)
         total=cursor.fetchone() #(10)
         cursor.close()
         conn.close()
    except Exception as e:
         print(e)
    return total[0] #()

def foodCount():
    try:
         conn=models.getConnection()
         cursor=conn.cursor()
         sql="""
               SELECT COUNT(*) FROM food_menu_house
             """
         cursor.execute(sql)
         total=cursor.fetchone() #(10)
         cursor.close()
         conn.close()
    except Exception as e:
         print(e)
    return total[0] #()

# 검색
def foodFindData(page,address):
    try:
         conn=models.getConnection()
         cursor=conn.cursor()
         rowSize=20
         start=(rowSize*page)-(rowSize-1)
         end=rowSize*page

         sql=f"""
               SELECT fno,name,poster,num
               FROM (SELECT fno,name,poster,rownum as num
               FROM (SELECT fno,name,poster 
               FROM food_menu_house
               WHERE address LIKE '%'||'{address}'||'%' 
               ORDER BY fno ASC))
               WHERE num BETWEEN {start} AND {end}
              """
         #실행
         cursor.execute(sql)
         #데이터 받기
         food_list=cursor.fetchall()
         print(food_list)
         cursor.close()
         conn.close()
    except Exception as e:
         print(e)
    return food_list

def foodFindTotalPage(address):
    try:
         conn=models.getConnection()
         cursor=conn.cursor()
         sql=f"""
               SELECT CEIL(COUNT(*)/20.0) FROM food_menu_house
               WHERE address LIKE '%'||'{address}'||'%'
             """
         cursor.execute(sql)
         total=cursor.fetchone() #(10)
         cursor.close()
         conn.close()
    except Exception as e:
         print(e)
    return total[0] #()

def foodFindCount(address):
    try:
         conn=models.getConnection()
         cursor=conn.cursor()
         sql=f"""
               SELECT COUNT(*) FROM food_menu_house
               WHERE address LIKE '%'||'{address}'||'%'
             """
         cursor.execute(sql)
         total=cursor.fetchone() #(10)
         cursor.close()
         conn.close()
    except Exception as e:
         print(e)
    return total[0] #()

"""
  FNO                                       NOT NULL NUMBER
 POSTER                                    NOT NULL VARCHAR2(1000)
 NAME                                      NOT NULL VARCHAR2(300)
 TYPE                                      NOT NULL VARCHAR2(100)
 ADDRESS                                   NOT NULL VARCHAR2(500)
 PHONE                                     NOT NULL VARCHAR2(100)
 SCORE                                              NUMBER(2,1)
 THEME                                     NOT NULL VARCHAR2(4000)
 PRICE                                              VARCHAR2(100)
 TIME                                               VARCHAR2(200)
 SEAT                                               VARCHAR2(100)
 CONTENT                                            CLOB
 LINK                                               VARCHAR2(300)
 HIT                                                NUMBER
 JJIMCOUNT                                          NUMBER
 LIKECOUNT                                          NUMBER
"""
def foodDetailData(fno):
    conn=models.getConnection()
    cursor=conn.cursor()
    sql=f"""
               SELECT 'http://www.menupan.com'||poster,name,type,address,phone,score,theme,price,time,seat
               FROM food_menu_house
               WHERE fno={fno}
        """
    cursor.execute(sql)
    food_detail=cursor.fetchone()
    cursor.close()
    conn.close()
    return food_detail


