from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('create/', views.todo_create, name='todo_create'),
    path('<int:id>/', views.todo_list, name='todo_list'),
    path('view/', views.view, name='view'),

]
