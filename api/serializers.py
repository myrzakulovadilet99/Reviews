from rest_framework import serializers
from api.models import Review, Account
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields =('id', 'username', 'email')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name')

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id','rating', 'title', 'text', 'date', 'company', 'ip_address')

