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
    try:
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

         main_data={
            "rd":rd,
            "fd":fd
         }
    except Exception as e:
        print(e)

    return render(request,"main/home.html",main_data)
    #return JsonResponse(main_data)
