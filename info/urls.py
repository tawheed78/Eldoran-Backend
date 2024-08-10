from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all', views.all_info),
    path('get/<int:info_id>', views.get_info),
    path('update/<int:info_id>', views.update_info),
    path('add/', views.add_info),
    path('delete/<int:info_id>', views.delete_info),
    path('search', views.search, name="search"),   
]
