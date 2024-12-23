from rest_framework import serializers
from .models import AuthorsModel

class AuthorSerializer(serializers.ModelSerializer):
    class Meta :
        model = AuthorsModel
        fields = "__all__"