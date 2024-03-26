from django.db import models
import oracledb
import os
import sys
import urllib.request
import json
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
              WHERE rownum<=5
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
              WHERE rownum<=8
             """
         cursor.execute(sql)
         food_list=cursor.fetchall() #fetchall(Tuple 여러개) , fetchone(Tuple 1개)
         cursor.close()
         conn.close()
    except Exception as e:
         print(e)
    return food_list

def chefMainData():
    conn=getConnection()
    cursor=conn.cursor()
    sql="""
         SELECT chef,poster,mem_cont1,mem_cont2,mem_cont3,mem_cont7,rownum
         FROM chef
         WHERE rownum<=1
        """
    cursor.execute(sql)
    chef_one=cursor.fetchone()
    cursor.close()
    conn.close()
    return chef_one
def todayFoodData():
    conn=getConnection()
    cursor=conn.cursor()
    sql="""
          SELECT poster,name,jjimcount,hit,theme,rownum
          FROM food_menu_house
          WHERE rownum<=1
        """
    cursor.execute(sql)
    today_house=cursor.fetchone()
    cursor.close()
    conn.close()
    return today_house
def newsData(fd):
    client_id = "ATsye14KFNTQUc8OcBlA"
    client_secret = "ACZc2lTqWI"
    encText = urllib.parse.quote(fd)
    url = "https://openapi.naver.com/v1/search/news.json?query=" + encText  # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read() #unicode
        print(response_body.decode('utf-8'))
        news_data=json.loads(response_body.decode('utf-8'))
        #eval => dict형으로 변경 => dict(JSON) {}
        #json.dumps , json.loads , eval ....
        return news_data
    else:
        print("Error Code:" + rescode)




