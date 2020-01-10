from rest_framework import generics 
#Model
from TodoList.models import Desk
from TodoList.models import TodoList
#Serializers Model
from TodoList.api.serializers import DeskSerializer
from TodoList.api.serializers import TodoListSerializer
#start class and func

class DeskCreateList(generics.ListCreateAPIView):
    queryset = Desk.objects.all()
    serializer_class = DeskSerializer

class DeskUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Desk.objects.all()
    serializer_class    =   DeskSerializer


class TodoCreateList(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class    =   TodoListSerializer

class TodoUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer