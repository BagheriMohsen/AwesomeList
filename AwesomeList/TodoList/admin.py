from django.contrib import admin

# Register your models here.
from .models import Desk
from .models import TodoList


@admin.register(Desk)
class DeskAdmin(admin.ModelAdmin):
    list_display    =   ['title','created_at','updated_at']
    list_filter     =   ['created_at','updated_at']
    search_fields   =   ['title',]


    
@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display    =   ['desk','task','created_at','updated_at']
    list_filter     =   ['created_at','updated_at']
    search_fields   =   ['task']

    def desk(self,obj):
        return ' ' .join([desk.title for desk in obj])