from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('toggle/<int:item_id>/', views.toggle_complete, name='toggle_complete'),
    path('delete/<int:item_id>/', views.delete_todo, name='delete_todo'),
]