from django.shortcuts import render

# Create your views here.
def Show_List(request):
    return render(request, 'orders/list.html')