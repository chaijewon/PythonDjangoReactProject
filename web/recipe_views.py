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
    recipe_count=recipe_models.recipeRowCount()
    """
    recip_data={
        "recipe_list":rd,
        "curpage":int(curpage),
        "totalpage":int(totalpage),
        "startPage":int(startPage),
        "endPage":int(endPage)
    }
    """
    recipe_data={
        "recipe_list": rd,
        "curpage": int(curpage),
        "count":int(recipe_count)
    }

    return JsonResponse(recipe_data)

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

    chef_count=recipe_models.recipeChefRowCount()
    """
    chef_data = {
        "chef_list": cd,
        "curpage": int(curpage),
        "totalpage": int(totalpage)
    }
    """
    chef_data = {
        "chef_list": cd,
        "curpage": int(curpage),
        "count": int(chef_count)
    }
    return JsonResponse(chef_data)

"""
     POSTER                                    NOT NULL VARCHAR2(300)
     TITLE                                     NOT NULL VARCHAR2(1000)
     CHEF                                      NOT NULL VARCHAR2(200)
     CHEF_POSTER                                        VARCHAR2(300)
     CHEF_PROFILE                                       VARCHAR2(1000)
     INFO1                                              VARCHAR2(100)
     INFO2                                              VARCHAR2(100)
     INFO3                                              VARCHAR2(100)
     CONTENT                                            VARCHAR2(4000)
     FOODMAKE                                            CLOB
     STUFF                                              CLOB
"""
def recipeDetailView(request):
    no=request.GET['no']
    return render(request,"recipe/detail.html",{"no":no})
def recipeDetail(request):
    no=request.GET['no']
    rd,rfood,rstuff=recipe_models.recipe_detail(int(no))
    re_detail={
        "no":int(rd[0]),
        "poster":rd[1],
        "title":rd[2],
        "chef":rd[3],
        "chef_poster":rd[4],
        "chef_profile":rd[5],
        "info1":rd[6],
        "info2":rd[7],
        "info3":rd[8],
        "content":rd[9]
    }

    stuff=rstuff.split(",")
    rdata=rfood.split("\n")
    posters=[]
    make=[]

    for data in range(len(rdata)-1):
        temp=rdata[data].split("^")
        make.append(temp[0])
        posters.append(temp[1])

    detail={
        "detail":re_detail,
        "posters":posters,
        "make":make,
        "stuff":stuff
    }
    print(re_detail)
    print(posters)
    print(make)
    print(stuff)
    return JsonResponse(detail)





