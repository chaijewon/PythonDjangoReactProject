from django.http import JsonResponse
from django.shortcuts import render,redirect
from web import food_models

def food_list(request):
    try:
         page=request.GET['page'] # request.getParameter("paga")
    except Exception as e:
         page="1"

    curpage=int(page)
    food_list=food_models.foodListData(curpage) # ()
    totalpage=food_models.foodTotalPage()
    count=food_models.foodCount()
    BLOCK=10
    startPage=((curpage-1)/BLOCK*BLOCK)+1
    endPage=((curpage-1)/BLOCK*BLOCK)+BLOCK

    if endPage > totalpage :
        endPage=totalpage
    fl=[]
    for f in food_list:
        fdata = {"fno": f[0], "name": f[1], "poster": f[2]}
        fl.append(fdata)

    food_data={
             "food_list":fl,
             "curpage":int(curpage),
             "totalpage":int(totalpage),
             "startPage":int(startPage),
             "endPage":int(endPage),
             "count":int(count),
             "range":range(int(startPage),int(endPage))
    }
    return render(request,"food/list.html",food_data)
    #return JsonResponse(food_data)

def food_find(request):
    try:
          page=request.GET['page']
    except Exception as e:
          page="1"
    try:
          address = request.GET['address']
    except Exception as e:
          address = "마포"

    curpage = int(page)
    food_list = food_models.foodFindData(curpage,address)  # ()
    totalpage = food_models.foodFindTotalPage(address)
    count = food_models.foodFindCount(address)
    BLOCK = 10
    startPage = ((curpage - 1) / BLOCK * BLOCK) + 1
    endPage = ((curpage - 1) / BLOCK * BLOCK) + BLOCK

    if endPage > totalpage:
        endPage = totalpage
    fl = []
    for f in food_list:
        fdata = {"fno": f[0], "name": f[1], "poster": f[2]}
        fl.append(fdata)

    food_data = {
        "food_list": fl,
        "curpage": int(curpage),
        "totalpage": int(totalpage),
        "startPage": int(startPage),
        "endPage": int(endPage),
        "count": int(count),
        "range": range(int(startPage), int(endPage)),
        "address":address
    }
    return render(request, "food/find.html", food_data)

