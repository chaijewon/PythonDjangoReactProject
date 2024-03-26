from django.shortcuts import render,redirect
from django.http import JsonResponse
"""
   render(request,"url",{키:값,......}) => forward
   redirect("url") => sendRedirect
   JsonRespones({}) => JSON만 전송 ==> Vue/React => Rest
   => CrossOrigin
"""
from web import models
# Create your views here.
def main_page(request):
         recipe_data=models.mainRecipeData()
         """
           [
              (1,"aaa","http")
              (1,"aaa","http")
              (1,"aaa","http")
              (1,"aaa","http")
           ]
         """
         food_data=models.mainFoodData()
         rd=[]
         for r in recipe_data:
             rdata={"no":r[0],"title":r[1],"poster":r[2],"chef":r[3]}
             rd.append(rdata)
         fd=[]
         for f in food_data:
             fdata={"fno":f[0],"name":f[1],"poster":f[2]}
             fd.append(fdata)
         #chef,poster,mem_cont1,mem_cont2,mem_cont3,mem_cont7 => Tuple ()
         cdata=models.chefMainData()
         cd={
              "chef":cdata[0],
              "poster":cdata[1],
              "mc1":cdata[2],
              "mc2": cdata[3],
              "mc3": cdata[4],
              "mc7": cdata[5]
         }
         #(poster,name,jjimcount,hit,theme)
         tdata=models.todayFoodData()
         td={
             "poster":tdata[0],
             "name":tdata[1],
             "jjimcount":tdata[2],
             "hit":tdata[3],
             "theme":tdata[4]
         }
         """
           1. list => []
           2. Tuple => (1,"aaa"...)
           3. Dict  => {키:값} => JSON , Map
         """
         news_data=models.newsData("맛집")
         #print(news_data.encode('utf-8'))
         main_data={
            "rd":rd,
            "fd":fd,
            "cd":cd,
            "td":td,
            "nd":news_data['items']
         }
         """
           list  =>  배열 [] = arraylist
           tuple => () = 데이터베이스 연결 
           dict => {} = map
         """
    #return render(request,"main/home.html",main_data)
         return JsonResponse(main_data)
