from rest_framework import serializers

from TodoList.models import Desk
from TodoList.models import TodoList

class DeskSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Desk
        fields  = '__all__'


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   TodoList
        fields  =   '__all__'
