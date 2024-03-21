from django.db import models
import oracledb
# Create your models here.
def getConnection():
    try:
         conn=oracledb.connect(user="hr",password="happy",dsn="localhost:1521/XE")
    except Exception as e:
         print(e)
    return conn

def mainRecipeData():
    try:
         conn=getConnection() #Connection
         cursor=conn.cursor() #PreparedStatement => SQL전송 => 결과값 받기
         sql="""
              SELECT no,title,poster,chef,rownum
              FROM (SELECT no,title,poster,chef 
              FROM recipe ORDER BY no ASC)
              WHERE rownum<=12
             """
         cursor.execute(sql)
         recipe_list=cursor.fetchall()
         cursor.close()
         conn.close()
    except Exception as e:
         print(e)
    return recipe_list

def mainFoodData():
    try:
         conn=getConnection() #Connection
         cursor=conn.cursor() #PreparedStatement => SQL전송 => 결과값 받기
         sql="""
              SELECT fno,name,poster,rownum
              FROM (SELECT fno,name,poster 
              FROM food_menu_house ORDER BY fno ASC)
              WHERE rownum<=12
             """
         cursor.execute(sql)
         food_list=cursor.fetchall() #fetchall(Tuple 여러개) , fetchone(Tuple 1개)
         cursor.close()
         conn.close()
    except Exception as e:
         print(e)
    return food_list


