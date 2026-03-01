from django.contrib.auth.models import Group, User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from config.backapp1.serializers import UserSerializer, GroupSerializer, AnalysisSerializer, PostAnalysedModel
from .models import AnalysisModel, PostAnalysedModel

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

def get_mock_posts():
    return [
        {"reddit_id": "abc123", "title": "How I got my first customer", "body": "...", "score": 150, "num_comments": 23},
        {"reddit_id": "def456", "title": "Struggling with pricing", "body": "...", "score": 89, "num_comments": 12},
    ]

# @api_view(["POST"])
# def analysisView(request):
