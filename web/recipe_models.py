from django.db import models
#VueJS
import oracledb
from web import models
def recipeListData(page):
    try:
         conn=models.getConnection()
         cursor=conn.cursor()
         rowSize=20
         start=(rowSize*page)-(rowSize-1)
         end=rowSize*page
         sql=f"""
               SELECT no,title,poster,chef,num
               FROM (SELECT no,title,poster,chef,rownum as num 
               FROM (SELECT no,title,poster,chef 
               FROM recipe WHERE no IN(SELECT no FROM recipe
               INTERSECT SELECT no FROM recipeDetail)
               ORDER BY no ASC))
               WHERE num BETWEEN {start} AND {end}
              """
         cursor.execute(sql)
         recipe_list=cursor.fetchall() #() => 여러개 , ()한개면 fetchone()
         # selectList / selectOne => MyBatis,JPA(X) => ORM
         cursor.close()
         conn.close()
    except Exception as e:
         print(e)
    #지역변수의 scope가 명확하지 않는다  (var => let)
    return recipe_list

def recipeTotalPage():
    try:
          conn=models.getConnection()
          cursor=conn.cursor()
          sql="""
                SELECT CEIL(COUNT(*)/20.0) 
                FROM recipe
                WHERE no IN(SELECT no FROM recipe
                INTERSECT SELECT no FROM recipeDetail)
              """
          cursor.execute(sql)
          total=cursor.fetchone()
          cursor.close()
          conn.close()
    except Exception as e:
          print(e)
    return total[0] #(10)

def recipeFindData(page,fd):
    try:
         conn=models.getConnection()
         cursor=conn.cursor()
         rowSize=20
         start=(rowSize*page)-(rowSize-1)
         end=rowSize*page
         sql=f"""
               SELECT no,title,poster,chef,num
               FROM (SELECT no,title,poster,chef,rownum as num 
               FROM (SELECT no,title,poster,chef 
               FROM recipe WHERE no IN(SELECT no FROM recipe
               INTERSECT SELECT no FROM recipeDetail)
               AND title LIKE '%'||'{fd}'||'%'
               ORDER BY no ASC))
               WHERE num BETWEEN {start} AND {end}
              """
         cursor.execute(sql)
         recipe_list=cursor.fetchall() #() => 여러개 , ()한개면 fetchone()
         # selectList / selectOne => MyBatis,JPA(X) => ORM
         cursor.close()
         conn.close()
    except Exception as e:
         print(e)
    #지역변수의 scope가 명확하지 않는다  (var => let)
    return recipe_list

def recipeFindTotalPage(fd):
    try:
          conn=models.getConnection()
          cursor=conn.cursor()
          sql=f"""
                SELECT CEIL(COUNT(*)/20.0) 
                FROM recipe
                WHERE no IN(SELECT no FROM recipe
                INTERSECT SELECT no FROM recipeDetail)
                AND title LIKE '%'||'{fd}'||'%'
              """
          cursor.execute(sql)
          total=cursor.fetchone()
          cursor.close()
          conn.close()
    except Exception as e:
          print(e)
    return total[0] #(10)

def recipeChefList(page):
    try:
         conn=models.getConnection()
         cursor=conn.cursor()
         rowSize = 20
         start = (rowSize * page) - (rowSize - 1)
         end = rowSize * page
         """
             CNO                                       NOT NULL NUMBER
             CHEF                                      NOT NULL VARCHAR2(100)
             POSTER                                    NOT NULL VARCHAR2(500)
             MEM_CONT1                                          NUMBER
             MEM_CONT2                                          NUMBER
             MEM_CONT3                                          NUMBER
             MEM_CONT7                                          NUMBER
         """
         sql=f"""
                SELECT cno,chef,poster,mem_cont1,mem_cont2,mem_cont3,mem_cont7,num
                FROM (SELECT cno,chef,poster,mem_cont1,mem_cont2,mem_cont3,mem_cont7,rownum as num
                FROM (SELECT cno,chef,poster,mem_cont1,mem_cont2,mem_cont3,mem_cont7
                FROM chef ORDER BY cno ASC))
                WHERE num BETWEEN {start} AND {end}
              """
         cursor.execute(sql)
         chef_list=cursor.fetchall()
         cursor.close()
         conn.close()
    except Exception as e:
         print(e)
    return chef_list

def recipeChefTotalPage():
    try:
         conn=models.getConnection()
         cursor=conn.cursor()
         sql="""
             SELECT CEIL(COUNT(*)/20.0) FROM chef 
             """
         cursor.execute(sql)
         total=cursor.fetchone()
         cursor.close()
         conn.close()
    except Exception as e:
         print(e)
    return total[0]