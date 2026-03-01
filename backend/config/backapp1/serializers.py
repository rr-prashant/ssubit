from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import AnalysisModel, PostAnalysedModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ["id", "username", "email", "groups"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]

class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisModel
        fields = ["__all__"]

class PostAnalysedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAnalysedModel
        fields = ["__all__"]