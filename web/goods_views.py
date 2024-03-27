from django.http import JsonResponse
from django.shortcuts import render,redirect
from web import goods_models

#연결 => 요청처리
def goods_list(request):
    try:
         page=request.GET['page']
    except Exception as e:
         page="1"
    type=request.GET['type']
    tname_data=['','goods_all','goods_best','goods_new','goods_special']
    tname=tname_data[int(type)]
    #no,goods_name,goods_price,goods_poster
    goods_data,count=goods_models.goodsListData(int(page),tname)
    gd=[]
    for data in goods_data:
        gdata={"no":data[0],"name":data[1],"price":data[2],"poster":data[3]}
        gd.append(gdata)

    goods={
        "gd":gd,
        "count":int(count),
        "curpage":int(page)
    }

    return JsonResponse(goods)

def goods_detail(request):
    no=request.GET.get('no')
    type = request.GET['type']
    tname_data = ['', 'goods_all', 'goods_best', 'goods_new', 'goods_special']
    tname = tname_data[int(type)]
    #request.GET['no']
    g_detail=goods_models.goodsDetailData(int(no),tname)
    """
     no,goods_name,goods_sub,goods_price,
     goods_discount,goods_first_price,goods_delivery,goods_poster,hit
     () => {}
    """
    gd={
        "no":g_detail[0],
        "name":g_detail[1],
        "sub":g_detail[2],
        "price":g_detail[3],
        "discount":g_detail[4],
        "fprice":g_detail[5],
        "delivery":g_detail[6],
        "poster":g_detail[7],
        "hit":g_detail[8]
    }

    return JsonResponse(gd)





