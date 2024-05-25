from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),  #empty space that indicate there is no url after food that write in project urls if you write after project 
                                       # file then you write in empty place just like "hello/".
    path('item/',views.item,name="item"),  
    path('<int:item_id>/',views.detail,name="detail"),                          
]
