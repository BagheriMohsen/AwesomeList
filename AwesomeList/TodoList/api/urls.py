from django.urls import path

from TodoList.api import views


urlpatterns =[
    #Desk URL
    path('',views.DeskCreateList.as_view(),name="desk_create_details"),
    path('<pk>',views.DeskUpdateDestroy.as_view(),name="desk_update_destroy"),
    #TodoList URL
    path('todo/',views.TodoCreateList.as_view(),name="todo_create_details"),
    path('todo/<pk>',views.TodoUpdateDestroy.as_view(),name="todo_update_destroy"),
]
