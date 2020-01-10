from django.urls import path

from TodoList.api import views


urlpatterns =[
    path('',views.DeskDetails.as_view(),name="desk_details"),
]
