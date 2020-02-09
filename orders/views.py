from django.shortcuts import render
from .models import orders, customers, Material, DasteMahsool, Templates
from .forms import Order_Form
from jalali_date import datetime2jalali, date2jalali
from django.shortcuts import HttpResponse, redirect, render
from django.core import serializers
from django.http import JsonResponse
import json

# Create your views here.
def Show_List(request):
        OrderList = orders.objects.all()
        return render(request, 'orders/list.html', {'Order_List': OrderList})


def OrderF(request):
    if request.method == "POST":
        cus = customers.objects.get(name_tafzili_shenavar=request.POST.get("Name_Moshtari"))
        das = DasteMahsool.objects.get(DasteMahsool=request.POST.get("Daste_Mahsool"))
        mav = Material.objects.get(NameKala=request.POST.get("MavadAvaliye1"))
        cg = Templates.objects.get(Code_ghalebe_asli=request.POST.get("CodeGhaleb"))
        orders.objects.create(Name_Moshtari=cus, Daste_Mahsool=das, MavadAvaliye1=mav, Name_Project=request.POST.get("Name_Project"), NoeFactor=request.POST.get("NoeFactor"), Tirazh=request.POST.get("Tirazh"), SharheMavadAvaliye1=request.POST.get("SharheMavadAvaliye1"), IsBehdashti=request.POST.get("IsBehdashti"), CodeGhaleb=cg, user=request.user)
        return redirect('orders:orderlist')
    else:
        OrderForm = Order_Form()
        TemplatesAll = Templates.objects.all()
        jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
        return render(request, 'orders/order.html', {'order_form': OrderForm, 'TemplatesAll': TemplatesAll, 'JoinDateJalali': jalali_join})        




def get_name_tafzili_shenavar(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    q2 = request.GET.get('elementname', '')
    places = []
    if ('Moshtari' in q2):
      places = customers.objects.filter(name_tafzili_shenavar__icontains=q)
    elif ('Mahsool' in q2):
      places = DasteMahsool.objects.filter(DasteMahsool__icontains=q)
    elif ('Mavad' in q2):
      places = Material.objects.filter(NameKala__icontains=q)
    elif ('CodeGh' in q2):
      places = Templates.objects.filter(Code_ghalebe_asli__icontains=q)      
    results = []
    for pl in places:
      place_json = {}
      if ('Moshtari' in q2):
        place_json = pl.name_tafzili_shenavar
      elif ('Mahsool' in q2):
        place_json = pl.DasteMahsool
      elif ('Mavad' in q2):      
        place_json = pl.NameKala
      elif ('CodeGh' in q2):      
        place_json = pl.Code_ghalebe_asli        
      results.append(place_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)  
  

def get_template(request):
  #if request.is_ajax():
  bid = request.GET.get('bid', '')
  tmp = Templates.objects.get(id=bid)
  results = {
        'tj': tmp.toole_mahsool,
        'aj': tmp.arze_mahsool,
        'ej': tmp.ertefa_mahsool,
        'td': tmp.tedad_dar_ghaleb,
        'aaj': tmp.Toole_Sheete_Chapi,
        'eej': tmp.Arze_sheete_chapi,
        'cga': tmp.Code_ghalebe_asli,
    }
    # data = JsonResponse(results)
  #   print(data)
  # #else:
  #   #data = 'fail'
  # mimetype = 'application/json'
  return JsonResponse(results)         