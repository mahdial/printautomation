import json
from os.path import relpath

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import HttpResponse, redirect, render
from jalali_date import date2jalali, datetime2jalali
from django.forms.models import model_to_dict

from .forms import Order_Form
from .models import DasteMahsool, Material, Templates, customers, orders
from datatables_ajax.datatables import DjangoDatatablesServerProc
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
        jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
        return render(request, 'orders/order.html', {'order_form': OrderForm, 'JoinDateJalali': jalali_join})        

        # student_form = StudentForm(request.POST)
        # if user_form.is_valid() and student_form.is_valid():
        #     user_form.save()
        #     student_form.save()


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
  return JsonResponse(results)     


def TemplatesToJason(request):
  if request.is_ajax():
    q1 = request.GET.get('dastemahsool', '')
    q1 = q1.replace("ي", "ی")
    q1 = q1.replace("ك", "ک")

    object_list = Templates.objects.filter(Daste_mahsool=q1)
    n = [{'id': blog.id, 'Code_ghalebe_asli': blog.Code_ghalebe_asli, 'Boresh_pish_az_Chap': blog.Boresh_pish_az_Chap, 'Toole_Sheete_Chapi': blog.Toole_Sheete_Chapi, 'Arze_sheete_chapi': blog.Arze_sheete_chapi, 'tedad_dar_ghaleb': blog.tedad_dar_ghaleb, 'Boresh_pas_az_chap': blog.Boresh_pas_az_chap, 'folder_link': blog.folder_link, 'Formoole_name_mahsool': blog.Formoole_name_mahsool} for blog in object_list]
    data = {"data": list(n)}
  else:
    data='fail'
  return JsonResponse(data, safe=False)  
