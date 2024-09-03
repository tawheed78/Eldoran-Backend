# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index),
#     path('all', views.all_info),
#     path('get/<int:info_id>', views.get_info),
#     path('update/<int:info_id>', views.update_info),
#     path('add/', views.add_info),
#     path('delete/<int:info_id>', views.delete_info),
#     path('search', views.search, name="search"),   
# ]
from django.urls import path
from .views import InfoList, InfoDetail, Trends, SearchView

urlpatterns = [
    path('infos/', InfoList.as_view(), name='info-list'),
    path('infos/<int:pk>/', InfoDetail.as_view(), name='info-detail'),
    path('infos/search/', SearchView.as_view(), name='search'),
    path('infos/trending', Trends.as_view(), name='trending-nft'),
]
