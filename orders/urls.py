from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('', views.OrderF, name="order"),
    path('list/', views.Show_List, name="orderlist"),
    path('api/get_places/', views.get_name_tafzili_shenavar, name='get_places'),
    path('api/get_template/', views.get_template, name='get_template'),
    path('api/templatestojason/', views.TemplatesToJason, name='templates_tojason'),
]