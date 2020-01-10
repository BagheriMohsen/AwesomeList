from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
#Model
from TodoList.models import Desk
from TodoList.models import TodoList
#Serializers Model
from TodoList.api.serializers import DeskSerializer
from TodoList.api.serializers import TodoListSerializer
#start class and func

class DeskDetails(APIView):

    def get(self , request):
        desks = Desk.objects.all()
        serializer = DeskSerializer(desks , many = True)
        return Response(serializer.data)
