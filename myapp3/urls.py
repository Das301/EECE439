from django.urls import path
from . import views

urlpatterns = [path('add_book/', views.add_page, name='add'), path('', views.main_page, name='home'),
               path('search_book/', views.search_page, name='search'),
               path('update_book/<int:id>/', views.update_page, name="update")]
