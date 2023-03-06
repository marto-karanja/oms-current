from django.urls import path
from main_oms import views
 
urlpatterns = [
    path('', views.orders_list),
    path('api/tutorials', views.orders_list),
    path('api/tutorials/<int:pk>', views.tutorial_detail),
    path('api/tutorials/published', views.tutorial_list_published)
]