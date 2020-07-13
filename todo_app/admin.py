from django.contrib import admin
from .models import ToDoList, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'todolist', 'id',)


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'id')


admin.site.register(ToDoList, ToDoListAdmin)
admin.site.register(Item, ItemAdmin)
