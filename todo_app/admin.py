from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'todolist')


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')


admin.site.register(ToDoList, ToDoListAdmin)
admin.site.register(Item, ItemAdmin)
