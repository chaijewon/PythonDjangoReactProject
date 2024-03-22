from django.http import JsonResponse
from django.shortcuts import render,redirect
from web import recipe_models

#render => forward => "경로명/jsp명" => request로 HTML에 값을 전송
#순서 => 언어 문법
"""
  C/C++  = Java = C# = Python = 스칼라 = 코틀린 
  int a=10 int a=10  int a=10 
  a=10 , a=10 
  var a=10
  @RequestMapping("/recipe/list")
  public String recipe_list(HttpServletRequest request){}
  
  app.get('/recipe/list',(request,response)=>{})
"""
def recipe_list_view(request):
    return render(request,"recipe/list.html")
def recipe_list(request):
    try:
          page=request.GET['page']
    except Exception as e:
          page="1"

    curpage=int(page)
    recipeList=recipe_models.recipeListData(curpage)
    totalpage=recipe_models.recipeTotalPage()

    BLOCK=10
    startPage=((curpage-1)/BLOCK*BLOCK)+1
    endPage=((curpage-1)/BLOCK*BLOCK)+BLOCK
    #[1]........[10]
    startPage=int(startPage)
    endPage=int(endPage)
    if endPage>totalpage:
        endPage=totalpage

    # no,title,poster,chef [{},{},{}...]
    rd=[]
    for recipe in recipeList:
        rdata={"no":recipe[0],"title":recipe[1],"poster":recipe[2],"chef":recipe[2]}
        rd.append(rdata)

    recip_data={
        "recipe_list":rd,
        "curpage":int(curpage),
        "totalpage":int(totalpage),
        "startPage":int(startPage),
        "endPage":int(endPage)
    }

    return JsonResponse(recip_data)

def recipe_find_view(request):
    return render(request,"recipe/find.html")

def recipe_find(request):
    try:
          page=request.GET['page']
    except Exception as e:
          page="1"

    try:
         fd=request.GET['fd']
    except Exception as e:
         fd="감자"

    curpage=int(page)
    recipeList=recipe_models.recipeFindData(curpage,fd)
    totalpage=recipe_models.recipeFindTotalPage(fd)

    BLOCK=10
    startPage=((curpage-1)/BLOCK*BLOCK)+1
    endPage=((curpage-1)/BLOCK*BLOCK)+BLOCK
    #[1]........[10]
    startPage=int(startPage)
    endPage=int(endPage)
    if endPage>totalpage:
        endPage=totalpage

    # no,title,poster,chef [{},{},{}...]
    rd=[]
    for recipe in recipeList:
        rdata={"no":recipe[0],"title":recipe[1],"poster":recipe[2],"chef":recipe[2]}
        rd.append(rdata)

    recip_data={
        "recipe_list":rd,
        "curpage":int(curpage),
        "totalpage":int(totalpage),
        "startPage":int(startPage),
        "endPage":int(endPage),
        "fd":fd
    }

    return JsonResponse(recip_data)

def recipe_chef_view(request):
    return render(request,"recipe/chef.html")

def recipe_chef(request):
    try:
         page=request.GET['page']
    except Exception as e:
         page="1"

    curpage = int(page)
    chefList = recipe_models.recipeChefList(curpage)
    totalpage = recipe_models.recipeChefTotalPage()


    # cno,chef,poster,mem_cont1,mem_cont2,mem_cont3,mem_cont7
    cd = []
    for chef in chefList:
        rdata = {"cno": chef[0], "chef": chef[1],
                 "poster": chef[2], "mem_cont1": chef[3],
                 "mem_cont2": chef[4],"mem_cont3": chef[5],
                 "mem_cont7": chef[6]
                 }
        cd.append(rdata)

    chef_data = {
        "chef_list": cd,
        "curpage": int(curpage),
        "totalpage": int(totalpage)
    }
    return JsonResponse(chef_data)




