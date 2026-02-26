from django.contrib.auth.models import Group, User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from config.backapp1.serializers import UserSerializer, GroupSerializer, ItemsSerializer
from .models import Items

@api_view(["GET"])
def UserView(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def GroupView(request):
    queryset = Group.objects.all()
    serializer = GroupSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def ItemView(request):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer(queryset, many= True)
    return Response(serializer_class.data)