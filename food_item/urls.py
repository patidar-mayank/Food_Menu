from django.urls import path
from . import views
app_name='food'

urlpatterns = [
    path('',views.index,name="index"),  #empty space that indicate there is no url after food that write in project urls if you write after project 
                                       # file then you write in empty place just like "hello/".
    path('item/',views.item,name="item"),  
    path('<int:item_id>/',views.detail,name="detail"),  
    path('add',views.create_item,name='create_item'),  
    path('update/<int:item_id>/',views.update_item,name='update_item'),
    path('delete/<int:item_id>',views.delete_item,name="delete_item"),                      
]