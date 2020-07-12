from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'todolist')


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
